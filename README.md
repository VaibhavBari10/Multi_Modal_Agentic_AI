# 🤖 Multi Modal Agentic AI

> An AI-powered Multi-Modal Agent that enables seamless interaction through speech, text, translation, voice cloning, and avatar generation using modern Generative AI technologies.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Agent-green?style=for-the-badge)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</p>

---

# 📖 Overview

**Multi Modal Agentic AI** is an intelligent AI assistant that combines multiple AI capabilities into one application. Users can interact naturally through voice or text while leveraging state-of-the-art Large Language Models (LLMs), multilingual translation, speech synthesis, voice cloning, and avatar generation.

This project demonstrates how modern AI technologies can be integrated to build a complete multimodal conversational assistant with an intuitive user interface.

---

# ✨ Features

- 🎤 Speech-to-Text using Whisper
- 🤖 AI Chat powered by Google Gemini
- 🌍 Multilingual Language Translation
- 🔊 Text-to-Speech Conversion
- 🗣️ Voice Cloning
- 👤 AI Avatar Generation
- 🧠 Agentic AI Workflow
- 📄 PDF/Text Processing
- 🖼️ Image Understanding
- 💬 Conversational Memory
- ⚡ Interactive Streamlit Interface

---

# 🎥 Project Demo

Watch the complete testing video demonstrating the application's features.

▶️ **Demo Video:** [Watch Demo](demo/testing_video.mp4)

### Demo Includes

- Speech-to-Text
- AI Chat
- Language Translation
- Text-to-Speech
- Voice Cloning
- Avatar Generation
- End-to-End AI Workflow

---

# 🏗️ System Architecture

```text
                      User
                        │
        ┌───────────────┴───────────────┐
        │                               │
     Voice Input                    Text Input
        │                               │
        ▼                               ▼
 Speech-to-Text (Whisper)          User Prompt
                │                      │
                └──────────┬───────────┘
                           ▼
                 Google Gemini LLM
                           │
      ┌────────────────────┼─────────────────────┐
      │                    │                     │
      ▼                    ▼                     ▼
 Translation         AI Response         Image Analysis
      │                    │
      ▼                    ▼
 Text-to-Speech      Voice Cloning
      │
      ▼
 Avatar Generation
      │
      ▼
   Final Output
```

---

# 📂 Project Structure

```
Multi_Modal_Agentic_AI/
│
├── demo/
│   └── testing_video.mp4
│
├── app.py
├── main.py
├── requirements.txt
├── .env
├── README.md
│
├── audio/
├── avatars/
├── images/
├── models/
├── output/
├── static/
├── templates/
├── utils/
│
└── notebooks/
```

---

# 🛠️ Tech Stack

## Programming Language

- Python 3.11

## AI Models

- Google Gemini
- Whisper
- MarianMT
- XTTS

## Frameworks

- Streamlit
- LangChain
- Transformers
- PyTorch

## Libraries

- OpenCV
- Pillow
- NumPy
- Pandas
- python-dotenv
- TTS
- ffmpeg
- gTTS

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/VaibhavBari10/Multi_Modal_Agentic_AI.git

cd Multi_Modal_Agentic_AI
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

---

# ▶️ Run the Project

### Streamlit

```bash
streamlit run app.py
```

### Python

```bash
python main.py
```

---

# 🚀 Workflow

1. User provides speech or text input.
2. Whisper converts speech into text.
3. Google Gemini processes the request.
4. Optional language translation is performed.
5. AI generates an intelligent response.
6. Response is converted into speech.
7. Voice cloning generates personalized audio.
8. Avatar is created.
9. Final multimodal response is displayed.

---

# 📸 Screenshots

Add screenshots here.

```
screenshots/

home.png

chat.png

speech_to_text.png

translation.png

tts.png

avatar.png
```

Example:

```markdown
## Home Page

![Home](screenshots/home.png)

## Speech to Text

![Speech](screenshots/speech_to_text.png)

## AI Chat

![Chat](screenshots/chat.png)
```

---

# 🎯 Use Cases

- AI Virtual Assistant
- Smart Customer Support
- Language Learning
- Accessibility Applications
- Voice-Based Interaction
- Educational AI
- AI Avatar Demonstrations
- Multilingual Communication

---

# 📈 Future Enhancements

- RAG (Retrieval-Augmented Generation)
- Vector Database Integration
- Long-Term Memory
- Multi-Agent Collaboration
- Video Generation
- Face Animation
- Docker Deployment
- Cloud Deployment (AWS/Azure/GCP)
- REST API
- User Authentication

---

# 📚 Learning Outcomes

This project demonstrates practical implementation of:

- Generative AI
- Prompt Engineering
- Large Language Models
- LangChain
- Google Gemini API
- Speech Recognition
- NLP
- Translation Models
- Voice Cloning
- Streamlit Development
- AI Agent Workflows
- Multimodal AI Systems

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📋 Requirements

- Python 3.11+
- Google Gemini API Key
- FFmpeg Installed
- Microphone (for speech input)
- Internet Connection

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

## Vaibhav Bari

AI & Data Science Enthusiast

- GitHub: https://github.com/VaibhavBari10
- LinkedIn: https://www.linkedin.com/in/vaibhav-bari10/

---

# ⭐ Support

If you found this project useful, please consider:

⭐ Star this repository

🍴 Fork the repository

📢 Share it with others

---

## 🙏 Acknowledgements

Special thanks to the open-source community and the developers of:

- Google Gemini
- LangChain
- OpenAI Whisper
- Hugging Face Transformers
- Streamlit
- PyTorch

---

<p align="center">

### ⭐ If you like this project, don't forget to Star the Repository ⭐

Made with ❤️ by **Vaibhav Bari**

</p>
