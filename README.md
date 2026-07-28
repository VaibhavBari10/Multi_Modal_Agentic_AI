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

**Multi Modal Agentic AI** is an intelligent AI assistant that combines multiple AI capabilities into a single application. It enables users to communicate naturally using voice or text while leveraging state-of-the-art Large Language Models (LLMs), multilingual translation, speech synthesis, voice cloning, and avatar generation.

The project demonstrates how modern AI technologies can work together to build a complete multimodal conversational assistant with an interactive Streamlit interface.

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

🎬 **Demo Video:**  
https://drive.google.com/file/d/180lujuwtvPwdu2h4k2Clkef66pFRSDM9/view?usp=sharing

### Demo Includes

- 🎤 Speech-to-Text
- 🤖 AI Chat with Google Gemini
- 🌍 Language Translation
- 🔊 Text-to-Speech
- 🗣️ Voice Cloning
- 👤 AI Avatar Generation
- ⚡ End-to-End AI Workflow

---

# 📂 Dataset

The dataset used in this project is too large to be included in the GitHub repository.

📥 **Download Dataset:**  
https://drive.google.com/file/d/1sbAQl06N3gT4M-HkdHY0AeeMUcax3OXu/view?usp=sharing

> **Instructions**
>
> 1. Download the dataset from the link above.
> 2. Extract it if it is compressed.
> 3. Place the extracted files inside the `dataset/` directory.

Expected folder structure:

```text
Multi_Modal_Agentic_AI/
│
├── dataset/
│   ├── train/
│   ├── test/
│   ├── validation/
│   └── ...
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

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

```text
Multi_Modal_Agentic_AI/
│
├── app.py
├── main.py
├── requirements.txt
├── .env.example
├── README.md
├── LICENSE
│
├── audio/
├── avatars/
├── dataset/
├── images/
├── models/
├── notebooks/
├── output/
├── static/
├── templates/
├── utils/
│
└── screenshots/
```

---

# 🛠️ Tech Stack

## Programming Language

- Python 3.11

## AI Models

- Google Gemini
- OpenAI Whisper
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
- FFmpeg
- gTTS

---

# ⚙️ Installation

## Clone the Repository

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

## Configure Environment Variables

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

1. User provides voice or text input.
2. Whisper converts speech into text.
3. Google Gemini processes the request.
4. Optional language translation is performed.
5. AI generates an intelligent response.
6. Response is converted into speech.
7. Voice cloning creates personalized audio.
8. Avatar is generated.
9. Final multimodal output is displayed.

---

# 📸 Screenshots

Add screenshots inside the `screenshots/` folder.

```text
screenshots/
│
├── home.png
├── speech_to_text.png
├── translation.png
├── chat.png
├── tts.png
└── avatar.png
```

Example:

```markdown
## Home

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
- Accessibility Solutions
- Voice-Based Applications
- Educational AI Systems
- AI Avatar Demonstrations
- Multilingual Communication

---

# 📈 Future Enhancements

- Retrieval-Augmented Generation (RAG)
- Vector Database Integration
- Long-Term Memory
- Multi-Agent Collaboration
- Video Generation
- Face Animation
- Docker Support
- Cloud Deployment (AWS, Azure, GCP)
- REST API Development
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
- Natural Language Processing
- Translation Models
- Voice Cloning
- Streamlit Development
- AI Agent Workflows
- Multimodal AI Systems

---

# 🤝 Contributing

Contributions are welcome!

1. Fork this repository.
2. Create a new feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 📋 Requirements

- Python 3.11+
- Google Gemini API Key
- FFmpeg Installed
- Microphone (for Speech Input)
- Internet Connection

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## Vaibhav Bari

**AI & Data Science Enthusiast**

- GitHub: https://github.com/VaibhavBari10
- LinkedIn: https://www.linkedin.com/in/vaibhav-bari10/

---

# ⭐ Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork this repository
- 📢 Share it with others

---

# 🙏 Acknowledgements

Special thanks to the open-source community and the developers of:

- Google Gemini
- LangChain
- OpenAI Whisper
- Hugging Face Transformers
- Streamlit
- PyTorch

---

<p align="center">

## ⭐ If you like this project, don't forget to Star the Repository! ⭐

Made with ❤️ by <strong>Vaibhav Bari</strong>

</p>
