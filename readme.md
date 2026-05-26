# 🎬 AI Video Assistant

An intelligent meeting analysis tool that transcribes, summarizes, and lets you chat with your video content using RAG (Retrieval-Augmented Generation).

## ✨ Features

- 🔊 **Audio Processing** — Supports YouTube URLs and local video/audio files
- 📝 **Transcription** — Local Whisper-based speech-to-text (English & Hinglish)
- 📋 **Summarization** — AI-powered meeting summaries
- ✅ **Action Items** — Automatically extracts action items
- 🔑 **Key Decisions** — Identifies important decisions made
- ❓ **Open Questions** — Highlights unresolved questions
- 💬 **RAG Chat** — Chat with your meeting transcript using natural language

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| UI | Streamlit |
| Speech-to-Text | OpenAI Whisper (local) |
| LLM | Mistral AI |
| RAG Pipeline | LangChain + ChromaDB |
| Embeddings | Sentence Transformers |
| Audio Download | yt-dlp |
| Audio Processing | pydub + ffmpeg |

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- ffmpeg installed on your system

### Installation

```bash
# Clone the repo
git clone https://github.com/YOURUSERNAME/video-agent.git
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
└── downloades/            # Temporary audio files (gitignored)
```

## 💡 Usage

1. Paste a **YouTube URL** or local file path in the sidebar
2. Select your language (**English** or **Hinglish**)
3. Click **Analyse**
4. View transcript, summary, action items, decisions and questions
5. **Chat** with your meeting using the RAG chatbot

## ⚙️ CLI Usage

```bash
python main.py
```

## 🌐 Deployment

Deployed on Hugging Face Spaces — [Live Demo](https://huggingface.co/spaces/YOURUSERNAME/SPACENAME)

## 📄 License

MIT License

## 🙏 Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper)
- [LangChain](https://langchain.com)
- [Mistral AI](https://mistral.ai)
- [Streamlit](https://streamlit.io)
