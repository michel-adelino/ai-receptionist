# AI Receptionist for Systems Limited 🧠🎙️

A voice-enabled, company-aware AI receptionist built with OpenAI, Whisper, LangChain, FAISS, and ElevenLabs — all trained on over 100+ scraped pages from the Systems Limited website.

## 📽️ Demo

🎥 [Click here to watch the recorded demo](https://drive.google.com/file/d/1JInIiivD3RBrqDqMrg24oT3hcPp_cvXB/view)

This video shows the full AI receptionist in action — using voice input, responding intelligently, and speaking back in a natural voice.

## 🚀 Features

- 🎤 **Voice-to-Voice Interaction**: Speak to the AI and hear it respond.
- 🧠 **Knowledge-Rich Answers**: Powered by your own website data.
- 🔍 **LangChain + FAISS**: Retrieval-Augmented Generation for accurate responses.
- 🧾 **Whisper & ElevenLabs**: Best-in-class transcription + text-to-speech.
- 💻 **Streamlit Frontend**: Clean UI with text or speech input options.

## 🧩 How It Works

1. **Web Scraping**: 100+ pages from Systems Limited’s website were scraped into a CSV file.
2. **Data Embedding**: Content was embedded using Sentence Transformers via LangChain.
3. **FAISS Index**: All embeddings were stored in a FAISS vector database.
4. **Query Engine**: User questions are matched with relevant documents and answered using OpenAI’s LLM.
5. **Voice Interaction**: Whisper handles speech-to-text, and ElevenLabs converts responses back into speech.

## 📁 Project Structure

```
ai-receptionist/
├── app/
│   ├── main.py
│   ├── chatbot.py
│   ├── audio.py
│   ├── st_custom_components/
│   │   └── st_audiorec/
│   │       └── frontend/
│   │           └── build/
│   └── utils/
│       ├── scraper_example.py
│       └── concatenate.py
├── new_faiss_index/
├── requirements.txt
├── .env.example
├── README.md
```

## 🛠️ Setup

1. Clone the repo:
   ```
   git clone https://github.com/your-username/ai-receptionist.git
   cd ai-receptionist
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Add your API keys:
   ```
   cp .env.example .env
   ```

4. Run the app:
   ```
   streamlit run app/main.py
   ```

## 👨‍💻 Built By

**Mousa Pirzada** – Machine Learning Intern at Systems Limited  
Internship Project (Summer 2023)

## 🌐 License

Open-source under MIT License.
