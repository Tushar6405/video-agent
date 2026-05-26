# 🎬 AI Video Assistant

An intelligent meeting analysis tool that transcribes, summarizes, and lets you chat with your video content using RAG (Retrieval-Augmented Generation).

## ✨ Features

- 🔊 **Audio Processing** — Supports YouTube URLs and local video/audio files
- 📝 **Transcription** — Whisper (English) + Sarvam AI Saaras v3 (Hinglish)
- 📋 **Summarization** — AI-powered meeting summaries
- ✅ **Action Items** — Automatically extracts action items
- 🔑 **Key Decisions** — Identifies important decisions made
- ❓ **Open Questions** — Highlights unresolved questions
- 💬 **RAG Chat** — Chat with your meeting transcript using natural language

## 🛠️ Tech Stack

| Component        | Technology                          |
| ---------------- | ----------------------------------- |
| UI               | Streamlit                           |
| Speech-to-Text (English)  | OpenAI Whisper (local)     |
| Speech-to-Text (Hinglish) | Sarvam AI — Saaras v2.5     |
| LLM              | Mistral AI                          |
| RAG Pipeline     | LangChain + ChromaDB                |
| Embeddings       | Sentence Transformers               |
| Audio Download   | yt-dlp                              |
| Audio Processing | pydub + ffmpeg                      |

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

3. **Click "New app"** and fill in:
   - **Repository:** `Tushar6405/video-agent`
   - **Branch:** `main`
   - **Main file path:** `app.py`

4. **Add your secret keys:**
   - In the Streamlit Cloud dashboard, go to **Settings → Secrets**
   - Add the following:
     ```toml
     MISTRAL_API_KEY = "your_mistral_api_key_here"
     SARVAM_API_KEY = "your_sarvam_api_key_here"
     ```

5. **Add system packages** — Streamlit Cloud uses your `packages.txt` to install system-level dependencies. Make sure `packages.txt` contains:
   ```
   ffmpeg
   ```

6. **Click "Deploy"** — your app will be live at:
   ```
   https://your-app-name.streamlit.app
   ```

> ⚠️ **Note on Whisper:** Streamlit Cloud's free tier has limited RAM (~1GB). Use a smaller Whisper model (`tiny` or `base`) for English transcription to avoid memory errors. Hinglish uses Sarvam AI's cloud API so no RAM impact there.

## 🌐 Transcription Details

| Language  | Engine         | Model         | Notes                              |
| --------- | -------------- | ------------- | ---------------------------------- |
| English   | OpenAI Whisper | `base`        | Runs locally                       |
| Hinglish  | Sarvam AI      | `saaras:v2.5` | Cloud API, handles code-mixed speech natively |

Sarvam's **Saaras v2.5** is purpose-built for Indian languages and handles mid-sentence switching between Hindi and English (code-mixing) without any drops or accuracy loss.

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
│   ├── transcriber.py     # Whisper (English) + Sarvam (Hinglish)
│   ├── summarizer.py      # LLM summarization
│   ├── extractor.py       # Action items, decisions, questions
│   ├── rag_engine.py      # RAG pipeline
│   └── vector_store.py    # ChromaDB vector store
├── utils/
│   └── audio_processor.py # Audio download & chunking
└── downloades/             # Temporary audio files (gitignored)
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

## 📄 License

MIT License

## 🙏 Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper)
- [Sarvam AI](https://www.sarvam.ai) — Saaras v2.5 for Hinglish transcription
- [LangChain](https://langchain.com)
- [Mistral AI](https://mistral.ai)
- [Streamlit](https://streamlit.io)