import os
from pydub import AudioSegment

DOWNLOAD_DIR = 'downloades'
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def is_youtube_url(source: str) -> bool:
    return "youtube.com" in source or "youtu.be" in source


def get_youtube_transcript(url: str, language: str = "english") -> str:
    """
    Fetch transcript directly from YouTube using youtube-transcript-api.
    No audio download needed — works from any cloud IP.
    """
    from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
    from urllib.parse import urlparse, parse_qs

    # Extract video ID from URL
    parsed = urlparse(url)
    if parsed.hostname in ("youtu.be",):
        video_id = parsed.path.lstrip("/")
    else:
        video_id = parse_qs(parsed.query).get("v", [None])[0]

    if not video_id:
        raise ValueError(f"Could not extract video ID from URL: {url}")

    print(f"Fetching transcript for video ID: {video_id}")

    try:
        # Try to get transcript in preferred language order
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        if language.lower() == "hinglish":
            # Try Hindi first, then fall back to English
            try:
                transcript = transcript_list.find_transcript(["hi", "en"])
            except NoTranscriptFound:
                transcript = transcript_list.find_generated_transcript(["hi", "en"])
        else:
            # English first, then any auto-generated
            try:
                transcript = transcript_list.find_transcript(["en"])
            except NoTranscriptFound:
                transcript = transcript_list.find_generated_transcript(["en"])

        entries = transcript.fetch()
        full_text = " ".join([entry["text"] for entry in entries])
        print(f"Transcript fetched — {len(entries)} segments.")
        return full_text

    except TranscriptsDisabled:
        raise RuntimeError("This video has transcripts/captions disabled. Please upload the audio file instead.")
    except NoTranscriptFound:
        raise RuntimeError("No transcript found for this video. Please upload the audio file instead.")
    except Exception as e:
        raise RuntimeError(f"Failed to fetch YouTube transcript: {e}")


def convert_to_wav(input_path: str) -> str:
    """Convert any audio/video file to WAV format using pydub."""
    output_path = os.path.splitext(input_path)[0] + "_converted.wav"
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1).set_frame_rate(16000)  # 16khz mono
    audio.export(output_path, format="wav")
    return output_path


def chunk_audio(wav_path: str, chunk_minutes: int = 10) -> list:
    audio = AudioSegment.from_wav(wav_path)
    chunk_ms = chunk_minutes * 60 * 1000

    chunks = []
    for i, start in enumerate(range(0, len(audio), chunk_ms)):
        chunk = audio[start: start + chunk_ms]
        chunk_path = f"{wav_path}_chunk_{i}.wav"
        chunk.export(chunk_path, format="wav")
        chunks.append(chunk_path)

    return chunks


def process_input(source: str, language: str = "english"):
    """
    Returns either:
    - (mode="transcript", text=str)  for YouTube URLs
    - (mode="chunks",     chunks=list) for local file uploads
    """
    if is_youtube_url(source):
        print("Detected YouTube URL. Fetching transcript via YouTube API...")
        text = get_youtube_transcript(source, language=language)
        return {"mode": "transcript", "text": text}
    else:
        print("Detected local file. Converting to WAV...")
        wav_path = convert_to_wav(source)
        print("Chunking audio...")
        chunks = chunk_audio(wav_path)
        print(f"Audio ready — {len(chunks)} chunk(s) created.")
        return {"mode": "chunks", "chunks": chunks}