title: Video Agent
emoji: 🎬
colorFrom: blue
colorTo: purple
sdk: docker
app_file: app.py
pinned: false
🎬 AI Video Assistant
An intelligent meeting analysis tool that transcribes, summarizes, and lets you chat with your video content using RAG (Retrieval-Augmented Generation).
✨ Features

🔊 Audio Processing — Supports YouTube URLs and local video/audio files
📝 Transcription — Whisper (English) + Sarvam AI Saaras v2.5 (Hinglish)
📋 Summarization — AI-powered meeting summaries
✅ Action Items — Automatically extracts action items
🔑 Key Decisions — Identifies important decisions made
❓ Open Questions — Highlights unresolved questions
💬 RAG Chat — Chat with your meeting transcript using natural language

🛠️ Tech Stack
ComponentTechnologyUIStreamlitSpeech-to-Text (English)OpenAI Whisper (local)Speech-to-Text (Hinglish)Sarvam AI — Saaras v2.5LLMMistral AIRAG PipelineLangChain + ChromaDBEmbeddingsSentence TransformersAudio Downloadyt-dlpAudio Processingpydub + ffmpeg
🚀 Getting Started (Local)
Prerequisites

Python 3.10+
ffmpeg installed on your system

Installation
bash# Clone the repo
git clone https://github.com/Tushar6405/video-agent.git
cd video-agent

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
Environment Variables
Create a .env file in the root directory:
MISTRAL_API_KEY=your_mistral_api_key_here
SARVAM_API_KEY=your_sarvam_api_key_here
Get your Sarvam API key at dashboard.sarvam.ai.
Run the app
bashstreamlit run app.py
Then open http://localhost:8501 in your browser.
☁️ Deploy on Hugging Face Spaces

Go to huggingface.co/spaces and create a new Space
Select Docker → Streamlit template
Connect your GitHub repo or push directly
Go to Settings → Variables and Secrets and add:

   MISTRAL_API_KEY = your_mistral_api_key_here
   SARVAM_API_KEY = your_sarvam_api_key_here

Your app will be live at:

   https://huggingface.co/spaces/Tushar2005Bhadane/video-agent
🌐 Transcription Details
LanguageEngineModelNotesEnglishOpenAI WhisperbaseRuns locallyHinglishSarvam AIsaaras:v2.5Cloud API, handles code-mixed speech natively
📁 Project Structure
video-agent/
├── app.py                 # Main Streamlit UI
├── main.py                # CLI entry point
├── requirements.txt       # Python dependencies
├── packages.txt           # System dependencies (ffmpeg)
├── README.md
├── .gitignore
├── core/
│   ├── transcriber.py     # Whisper (English) + Sarvam (Hinglish)
│   ├── summarizer.py      # LLM summarization
│   ├── extractor.py       # Action items, decisions, questions
│   ├── rag_engine.py      # RAG pipeline
│   └── vector_store.py    # ChromaDB vector store
├── utils/
│   └── audio_processor.py # Audio download & chunking
└── downloads/             # Temporary audio files (gitignored)
💡 Usage

Paste a YouTube URL or local file path in the sidebar
Select your language (English or Hinglish)
Click Analyse
View transcript, summary, action items, decisions and questions
Chat with your meeting using the RAG chatbot

⚙️ CLI Usage
bashpython main.py
📄 License
MIT License
🙏 Acknowledgements

OpenAI Whisper
Sarvam AI — Saaras v2.5 for Hinglish transcription
LangChain
Mistral AI
Streamlit