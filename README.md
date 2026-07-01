# 🤖 J.A.R.V.I.S — HUD Voice Assistant

An Iron Man inspired AI Voice Assistant with a stunning HUD interface.
Talk to JARVIS using your voice or keyboard — powered by Groq AI + Live Weather + Live Google Search!

## 🎥 Preview
> Iron Man style HUD interface with glowing teal effects and voice interaction

## ✨ Features
- 🎤 Auto Voice Recognition — bolo aur JARVIS sun ta hai!
- 🖥️ Iron Man HUD UI — animated background, glowing chat bubbles
- 🧠 AI Chat — powered by Groq (Llama 3.1 8B Instant)
- 🌦️ Live Weather — real city-based weather via OpenWeatherMap
- 🌐 Live Google Search — real-time answers for news, prices, scores
- 🔊 Voice + Text responses both (Web Speech API)
- ⌨️ Keyboard input bhi supported
- ⚡ Instant responses — time, date, greetings
- 💻 Code responses rendered in proper monospace formatting

## 🛠️ Tech Stack

| Technology | Use |
|---|---|
| **Flask** | Backend Server |
| **Groq API (Llama 3.1 8B Instant)** | AI Chat & Code Generation |
| **OpenWeatherMap API** | Live Weather Data |
| **BeautifulSoup** | Live Google Scraping (news, prices, scores) |
| **Web Speech API** | Voice Recognition + Text-to-Speech (browser-based) |
| **python-dotenv** | Environment variable management |
| **HTML/CSS/JS** | HUD Frontend |
| **Orbitron Font** | Sci-fi Typography |

## 🧠 How It Works

```
User speaks or types
        ↓
Is it greeting/time/date?
        ↓ YES → Instant Response
        ↓ NO
Is it a weather question?
        ↓ YES → OpenWeatherMap API
        ↓ NO
Is it a live question?
(price, score, news, aaj, abhi)
        ↓ YES → Google Search
        ↓ NO  → Groq AI (Llama 3.1)
        ↓
Voice + HUD Text Response
```

## ⚙️ Installation

1. **Clone the repo**
   ```
   git clone https://github.com/BobbyBohra/jarvis-chatbot.git
   cd jarvis-chatbot
   ```

2. **Install Python dependencies**
   ```
   pip install flask groq requests beautifulsoup4 python-dotenv
   ```

3. **Get API keys**
   - Groq API key: https://console.groq.com/keys
   - OpenWeatherMap API key: https://openweathermap.org/api (free tier — note: new keys can take up to 2 hours to activate)

4. **Create a `.env` file** in the project root
   ```
   GROQ_API_KEY=your_groq_api_key_here
   WEATHER_API_KEY=your_openweathermap_key_here
   ```

5. **Run the app**
   ```
   python app.py
   ```

6. **Open browser**
   ```
   http://localhost:10000
   ```

## 💬 Example Commands

| Command | Response |
|---|---|
| "Hello" | Greeting response |
| "What time is it?" | Current time |
| "Today's date" | Current date |
| "Weather in Mumbai" | Live weather via OpenWeatherMap |
| "Latest news" | Live Google answer |
| "What is AI?" | Groq AI answer |
| "Write python code to reverse a string" | Formatted code block + explanation |

## 📁 Project Structure
```
jarvis-chatbot/
├── app.py          # Flask backend + AI + weather logic
├── templates/
│   └── index.html  # HUD Frontend UI
├── .env             # API keys (not committed to git)
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
- Code responses in monospace font blocks

## ⚠️ Known Limitations
- No calendar, smart home, or email access — JARVIS will not pretend to perform real-world actions it can't do
- Google search scraping can occasionally break if Google changes its HTML structure
- Voice recognition works best in Chrome/Edge (uses `webkitSpeechRecognition`)

## 🙋‍♂️ Author
**Bobby Bohra**
- GitHub: https://github.com/BobbyBohra
