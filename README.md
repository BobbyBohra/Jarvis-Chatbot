# 🤖 J.A.R.V.I.S — HUD Voice Assistant

An Iron Man inspired AI Voice Assistant with a stunning HUD interface.
Talk to JARVIS using your voice or keyboard — powered by Offline AI + Live Google Search!

## 🎥 Preview
> Iron Man style HUD interface with glowing teal effects and voice interaction

## ✨ Features
- 🎤 Auto Voice Recognition — bolo aur JARVIS sun ta hai!
- 🖥️ Iron Man HUD UI — animated background, glowing chat bubbles
- 🧠 Offline AI — Ollama + Mistral model
- 🌐 Live Google Search — real-time answers
- 🔊 Voice + Text responses both
- ⌨️ Keyboard input bhi supported
- ⚡ Instant responses — time, date, greetings

## 🛠️ Tech Stack

| Technology | Use |
|---|---|
| **Flask** | Backend Server |
| **Ollama + Mistral** | Offline AI |
| **BeautifulSoup** | Live Google Scraping |
| **pyttsx3** | Text-to-Speech |
| **Web Speech API** | Voice Recognition |
| **HTML/CSS/JS** | HUD Frontend |
| **Orbitron Font** | Sci-fi Typography |

## 🧠 How It Works

User speaks or types
        ↓
Is it greeting/time/date?
        ↓ YES → Instant Response
        ↓ NO
Is it a live question?
(weather, price, score, aaj, abhi)
        ↓ YES → Google Search
        ↓ NO  → Ollama Mistral AI
        ↓
Voice + HUD Text Response

## ⚙️ Installation

1. Clone the repo
   git clone https://github.com/BobbyBohra/jarvis-chatbot.git

2. Install Python dependencies
   pip install flask pyttsx3 requests beautifulsoup4

3. Install Ollama
   https://ollama.com/download

4. Pull Mistral model
   ollama pull mistral

5. Run the app
   python app.py

6. Open browser
   http://localhost:5000

## 💬 Example Commands

| Command | Response |
|---|---|
| "Hello" | Greeting response |
| "What time is it?" | Current time |
| "Today's date" | Current date |
| "Today's weather" | Live Google answer |
| "What is AI?" | Mistral AI answer |

## 📁 Project Structure
```
jarvis-chatbot/
├── app.py          # Flask backend + AI logic
├── templates/
│   └── index.html  # HUD Frontend UI
└── README.md
```

## 🎨 UI Design
- Radial gradient dark background
- Rotating conic gradient animation
- Glowing teal chat container
- Animated typing indicator
- Fade-in message animations
- User messages in cyan
- JARVIS messages in gold

## 🙋‍♂️ Author
**Bobby Bohra**
- GitHub: https://github.com/BobbyBohra


## GitHub pe Add Karo:

Browser mein kholo:
```
https://github.com/BobbyBohra/jarvis-chatbot/new/main
