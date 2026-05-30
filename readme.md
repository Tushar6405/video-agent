# 🎬 AI Video Assistant

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://video-agent-k3rilwahvo58trtkucjfxz.streamlit.app)

An intelligent meeting analysis tool that transcribes, summarizes, and lets you chat with your video content using RAG (Retrieval-Augmented Generation).

## ✨ Features

- 🔊 **Audio Processing** — Supports YouTube URLs and local video/audio file uploads
- 📝 **Transcription** — Local Whisper-based speech-to-text (English & Hinglish)
- 📋 **Summarization** — AI-powered meeting summaries
- ✅ **Action Items** — Automatically extracts action items
- 🔑 **Key Decisions** — Identifies important decisions made
- ❓ **Open Questions** — Highlights unresolved questions
- 💬 **RAG Chat** — Chat with your meeting transcript using natural language

## ☁️ Live Demo

**Live at:** https://video-agent-k3rilwahvo58trtkucjfxz.streamlit.app

> ⚠️ Note: YouTube downloads may fail on cloud due to IP restrictions. Use the **file upload** option instead.

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| UI | Streamlit |
| Speech-to-Text | OpenAI Whisper (local) |
| Translation | Sarvam AI (Hinglish) |
| LLM | Mistral AI |
| RAG Pipeline | LangChain + ChromaDB |
| Embeddings | Sentence Transformers |
| Audio Download | yt-dlp |
| Audio Processing | pydub + ffmpeg |

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
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
WHISPER_MODEL=small
SARVAM_API_KEY=your_sarvam_api_key_here
SARVAM_STT_MODEL=saaras:v2.5
```

### Run the app

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

## 📁 Project Structure

```
video-agent/
├── app.py                 # Main Streamlit UI
├── main.py                # CLI entry point
├── requirements.txt
├── packages.txt
├── pyproject.toml
├── runtime.txt
├── README.md
├── .gitignore
├── core/
│   ├── transcriber.py     # Whisper transcription
│   ├── summarizer.py      # LLM summarization
│   ├── extractor.py       # Action items, decisions, questions
│   ├── rag_engine.py      # RAG pipeline
│   └── vector_store.py    # ChromaDB vector store
├── utils/
│   └── audio_processor.py # Audio download & chunking
├── downloades/            # Temporary audio files (gitignored)
└── vector_db/             # ChromaDB data (gitignored)
```

## 💡 Usage

1. Choose **YouTube URL** or **Upload File** in the sidebar
2. Paste a YouTube URL **or** upload a video/audio file (mp4, wav, mp3, m4a, webm)
3. Select your language (**English** or **Hinglish**)
4. Click **⚡ Analyse**
5. View transcript, summary, action items, decisions and questions
6. **Chat** with your meeting using the RAG chatbot

## ⚙️ CLI Usage

```bash
python main.py
```

## 📄 License

MIT License

## 🙏 Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper)
- [LangChain](https://langchain.com)
- [Mistral AI](https://mistral.ai)
- [Sarvam AI](https://sarvam.ai)
- [Streamlit](https://streamlit.io)
- [ChromaDB](https://www.trychroma.com)