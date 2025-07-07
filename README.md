# AI Receptionist 🧠🎙️

A voice-enabled, company-aware AI receptionist built with OpenAI, Whisper, LangChain, FAISS, and ElevenLabs — all trained on scraped website data.

## 📽️ Demo

<video src="showcase.mp4" controls width="100%"></video>

This video shows the full AI receptionist in action — using voice input, responding intelligently, and speaking back in a natural voice.

## 🚀 Features

- 🎙️ Voice-to-voice interaction (ask a question, hear a reply)
- 📚 Trained on 100+ webpages scraped from systems ltd
- 🧠 LangChain + GPT-3.5 for accurate retrieval and context
- 🗣️ ElevenLabs voice output with natural tone
- 💻 Built in Streamlit — no setup, just run and speak

---

## 🧰 Tech Stack

| Purpose            | Tools Used                        |
|-------------------|------------------------------------|
| Speech-to-Text     | [Whisper](https://github.com/openai/whisper) (OpenAI) |
| Knowledge Retrieval | FAISS + LangChain                |
| Text-to-Speech     | [ElevenLabs](https://www.elevenlabs.io) |
| Interface          | Streamlit                         |
| Language Model     | GPT-3.5 (via LangChain)           |
| Web Scraping       | BeautifulSoup                     |

## 🧠 How It Works

1. **Scrape company content** → chunk into documents  
2. **Embed content using OpenAI embeddings + FAISS index**  
3. **Capture voice via Whisper**, convert to text  
4. **Query LangChain’s retrieval chain** → generate response  
5. **Use ElevenLabs** to speak the result out loud  
6. **Streamlit UI** glues the entire experience together

## 📁 Project Structure

```
ai-receptionist/
├── app/
│ ├── main.py # Final Streamlit UI
│ ├── chatbot.py # Chat logic w/ LangChain
│ ├── audio.py # Whisper + ElevenLabs utils
│ ├── st_custom_components/
│ │ └── st_audiorec/
│ │ └── frontend/
│ │ └── build/ # Custom audio recorder component
│ └── utils/
│ ├── scraper_example.py # Scraping example (customize per site)
│ └── concatenate.py # Document concatenation utility
├── new_faiss_index/
│ ├── index.faiss # FAISS vector index
│ └── index.pkl # Pickled metadata index
├── .env.example # API key placeholders
├── requirements.txt # Python dependencies
├── README.md # Project overview and instructions
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

## 🌐 License

Open-source under MIT License.
