from flask import Flask, render_template, request, jsonify
import subprocess
import pyttsx3
import threading
from datetime import datetime

app = Flask(__name__)

# ---------- Enhanced Voice ----------
engine = pyttsx3.init()
engine.setProperty('rate', 160)    # Normal speaking rate
engine.setProperty('volume', 1.0)  # Max volume
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Male voice (adjust as needed)

def speak(text):
    def run_speech():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run_speech).start()

# ---------- Rule-based Short Responses ----------
def local_commands(question):
    q = question.lower()
    if q in ["hello", "hi", "hlo"]:
        return "Hello! How can I assist you, Sir?"
    elif q in ["how are you"]:
        return "I am fully operational, ready to assist!"
    elif q in ["time", "current time"]:
        return datetime.now().strftime("Current time is %H:%M:%S")
    elif q in ["date", "today's date"]:
        return datetime.now().strftime("Today's date is %d-%m-%Y")
    return None

# ---------- AI / Ollama ----------
def offline_ai(question):
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral", question],
            capture_output=True,
            text=True,
            check=True
        )
        answer = result.stdout.strip()
        return answer if len(answer) <= 200 else answer[:200] + "..."
    except Exception:
        return "Offline AI error."

# ---------- Live Google ----------
import requests
from bs4 import BeautifulSoup

def online_google(question):
    try:
        url = f"https://www.google.com/search?q={question}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        answer_box = soup.find("div", class_="BNeawe")
        if answer_box:
            answer = answer_box.text.strip().split('.')[0] + "."
            return answer if len(answer) <= 200 else answer[:200] + "..."
        return "Live answer not found."
    except:
        return "Error fetching live answer."

def is_live_question(q):
    live_words = ["today","current","live","now","weather","price","score","rate","aaj","abhi"]
    return any(word in q.lower() for word in live_words)

# ---------- Routes ----------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    q = data.get("question", "")
    answer = local_commands(q)
    if not answer:
        if is_live_question(q):
            answer = online_google(q)
        else:
            answer = offline_ai(q)
    speak(answer)

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)  
