# 🎬 AI Video Assistant

An intelligent meeting analysis tool that transcribes, summarizes, and lets you chat with your video content using RAG (Retrieval-Augmented Generation).

## ✨ Features

- 🔊 **Audio Processing** — Supports YouTube URLs and local video/audio files
- 📝 **Transcription** — YouTube Transcript API (YouTube) + Whisper (English files) + Sarvam AI Saaras v2.5 (Hinglish files)
- 📋 **Summarization** — AI-powered meeting summaries
- ✅ **Action Items** — Automatically extracts action items
- 🔑 **Key Decisions** — Identifies important decisions made
- ❓ **Open Questions** — Highlights unresolved questions
- 💬 **RAG Chat** — Chat with your meeting transcript using natural language

## 🛠️ Tech Stack

| Component                 | Technology                  |
| ------------------------- | --------------------------- |
| UI                        | Streamlit                   |
| YouTube Transcription     | youtube-transcript-api      |
| Speech-to-Text (English)  | OpenAI Whisper (local)      |
| Speech-to-Text (Hinglish) | Sarvam AI — Saaras v2.5     |
| LLM                       | Mistral AI                  |
| RAG Pipeline              | LangChain + ChromaDB        |
| Embeddings                | Sentence Transformers       |
| Audio Processing          | pydub + ffmpeg              |

## 🚀 Getting Started (Local)

### Prerequisites

- Python 3.10+
- ffmpeg installed on your system

### Installation

```bash
# Clone the repo
git clone https://github.com/Tushar6405/video-agent.git
cd video-agent

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root directory:

```
MISTRAL_API_KEY=your_mistral_api_key_here
SARVAM_API_KEY=your_sarvam_api_key_here
```

Get your Sarvam API key at [dashboard.sarvam.ai](https://dashboard.sarvam.ai).

### Run the app

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

## ☁️ Deploy on Streamlit Cloud

1. **Push your code to GitHub** (make sure `app.py` and `requirements.txt` are in the root).

2. **Go to [share.streamlit.io](https://share.streamlit.io)** and sign in with your GitHub account.

3. **Click "Create app"** and fill in:
   - **Repository:** `Tushar6405/video-agent`
   - **Branch:** `main`
   - **Main file path:** `app.py`

4. **Add your secret keys** — click "Advanced settings" and paste:
   ```toml
   MISTRAL_API_KEY = "your_mistral_api_key_here"
   SARVAM_API_KEY = "your_sarvam_api_key_here"
   ```

5. **Click Deploy** — your app will be live at:
   ```
   https://your-app-name.streamlit.app
   ```

> ⚠️ **Note:** Streamlit Cloud free tier has ~1GB RAM. Whisper `base` model is recommended for local file transcription.

## 🌐 Transcription Details

| Source         | Engine                  | Notes                                              |
| -------------- | ----------------------- | -------------------------------------------------- |
| YouTube URL    | youtube-transcript-api  | Fetches captions directly — no audio download      |
| File (English) | OpenAI Whisper          | Runs locally, `base` model recommended             |
| File (Hinglish)| Sarvam AI `saaras:v2.5` | Cloud API, handles code-mixed speech natively      |

> ℹ️ YouTube transcription works from any cloud IP. If a video has no captions, upload the audio file instead.

## 📁 Project Structure

```
video-agent/
├── app.py                 # Main Streamlit UI
├── main.py                # CLI entry point
├── requirements.txt       # Python dependencies
├── packages.txt           # System dependencies (ffmpeg)
├── readme.md
├── .gitignore
├── core/
│   ├── transcriber.py     # Whisper (English) + Sarvam (Hinglish) + YouTube passthrough
│   ├── summarizer.py      # LLM summarization
│   ├── extractor.py       # Action items, decisions, questions
│   ├── rag_engine.py      # RAG pipeline
│   └── vector_store.py    # ChromaDB vector store
├── utils/
│   └── audio_processor.py # YouTube transcript fetch & audio chunking
└── downloads/             # Temporary audio files (gitignored)
```

## 💡 Usage

1. Paste a **YouTube URL** or upload a local audio/video file
2. Select your language (**English** or **Hinglish**)
3. Click **Analyse**
4. View transcript, summary, action items, decisions and questions
5. **Chat** with your meeting using the RAG chatbot

## ⚙️ CLI Usage

```bash
python main.py
```

## 📄 License

MIT License

## 🙏 Acknowledgements

- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)
- [OpenAI Whisper](https://github.com/openai/whisper)
- [Sarvam AI](https://www.sarvam.ai) — Saaras v2.5 for Hinglish transcription
- [LangChain](https://langchain.com)
- [Mistral AI](https://mistral.ai)
- [Streamlit](https://streamlit.io)
