from flask import Flask, render_template, request, jsonify
from datetime import datetime
import requests
import re
from bs4 import BeautifulSoup
from groq import Groq
from dotenv import load_dotenv
import os

app = Flask(__name__)

# ---------- Groq AI Setup ----------
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---------- Weather Setup ----------
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
DEFAULT_CITY = "Delhi"  # <-- change to your default city

USER_NAME = "Bobby"  # <-- Your Name (keep in sync with index.html)

def ai_response(question):
    try:
        q = question.lower()

        coding_keywords = [
            "code", "program", "python", "java", "c++", "c", "html",
            "css", "javascript", "js", "sql", "php", "flask",
            "django", "reverse", "string", "array", "function",
            "algorithm", "leetcode"
        ]

        is_code = any(word in q for word in coding_keywords)

        if is_code:
            system_prompt = f"""
You are J.A.R.V.I.S., a personal AI assistant running as a simple text/voice chatbot.
You are currently assisting {USER_NAME}, NOT Tony Stark. Never refer to the user as Tony Stark or Sir Stark.
If you need to address the user by name, call them {USER_NAME}.
You have NO access to calendar, smart home devices, emails, or any real-world data. Do not invent schedules or actions.

If the user asks for a program:

1. Return properly formatted code with correct indentation and line breaks.
2. Wrap ONLY the code portion inside triple backticks, like this:
```python
your code here
```
3. Do not put the whole code on a single line.
4. After the closing triple backticks, write a short explanation in simple English (outside the backticks).
5. Do not wrap the explanation text in backticks, only the code.
"""

        else:
            system_prompt = f"""
You are J.A.R.V.I.S., a personal AI assistant running as a simple text/voice chatbot.
You are currently assisting {USER_NAME}, NOT Tony Stark. Never refer to the user as Tony Stark or Sir Stark.
If you need to address the user by name, call them {USER_NAME}.

IMPORTANT - Do not hallucinate capabilities you do not have:
- You have NO access to the user's calendar, schedule, meetings, or appointments.
- You have NO access to smart home devices (lights, coffee machine, TV, thermostat, etc).
- You have NO access to emails, contacts, investors, or any real-world data about the user's life.
- You CANNOT set reminders, alarms, or notifications.
- Do NOT invent or make up schedules, meetings, appointments, or events.
- Do NOT pretend to have started making coffee, turned on the TV, or performed any physical/smart-home action.
- If asked to do something you cannot actually do, honestly say you don't have that capability yet, in one short sentence.

How to answer:
- First, directly and accurately answer exactly what the user asked. Do not go off-topic.
- After answering, if relevant, you MAY add one short, useful suggestion, tip, or idea related to their question (like a smart assistant would). Keep it to 1 line, and only if it genuinely helps.
- Never add a suggestion that implies you performed a real-world action (like "I've already booked it" or "I've turned it on").

Answer naturally based only on the actual question asked.
Keep answers short.
Do not use markdown formatting like headings or bullet points.
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ],
            temperature=0.2,
            max_tokens=600
        )

        answer = response.choices[0].message.content
        return answer.strip()

    except Exception as e:
        return f"Sorry, I ran into an error: {e}"

# ---------- Rule-based Short Responses ----------
def local_commands(question):
    q = question.lower().strip()

    if q in ["hello", "hi", "hlo", "hey"]:
        return "Hello! How can I assist you?"

    elif q == "how are you":
        return "I'm doing great! How can I help you today?"

    elif q in ["time", "current time"]:
        return datetime.now().strftime("Current time is %H:%M:%S")

    elif q in ["date", "today", "today's date"]:
        return datetime.now().strftime("Today's date is %d-%m-%Y")

    return None

# ---------- Weather ----------
def extract_city(question):
    q = question.lower()

    # Pattern: "weather in X" / "weather of X" / "weather at X"
    match = re.search(r"weather\s+(?:in|of|at)\s+([a-zA-Z\s]+)", q)
    if match:
        return match.group(1).strip().title()

    # Pattern: "X ka weather" / "X ki weather" / "X mein weather"
    match = re.search(r"([a-zA-Z]+)\s*(?:ka|ki|mein|me)\s*weather", q)
    if match:
        return match.group(1).strip().title()

    return None

def get_weather(question):
    if not WEATHER_API_KEY:
        return "Weather API key is not set up yet, Bobby. Please add WEATHER_API_KEY in the .env file."

    city = extract_city(question) or DEFAULT_CITY

    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": WEATHER_API_KEY,
            "units": "metric"
        }
        r = requests.get(url, params=params, timeout=10)
        data = r.json()

        cod = str(data.get("cod"))

        if cod == "401":
            return "Your weather API key seems invalid or not activated yet, Bobby. New OpenWeatherMap keys can take up to 2 hours to activate."
        elif cod == "404":
            return f"I couldn't find a city called {city}, Bobby. Please check the spelling."
        elif cod != "200":
            return f"Weather service returned an error: {data.get('message', 'unknown error')}."

        temp = round(data["main"]["temp"])
        feels_like = round(data["main"]["feels_like"])
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        return (
            f"The weather in {city} is currently {description} with a temperature "
            f"of {temp} degrees Celsius, feels like {feels_like} degrees, "
            f"and humidity around {humidity} percent."
        )

    except Exception:
        return "Sorry, I couldn't fetch the weather right now. Please check your internet connection."

# ---------- Live Google ----------
def online_google(question):
    try:
        url = "https://www.google.com/search"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(
            url,
            params={"q": question},
            headers=headers,
            timeout=10
        )

        soup = BeautifulSoup(r.text, "html.parser")

        answer = soup.find("div", class_="BNeawe")

        if answer:
            return answer.get_text(strip=True)

        return ai_response(question)

    except Exception:
        return ai_response(question)

def is_live_question(q):
    live_words = [
        "today",
        "current",
        "live",
        "now",
        "weather",
        "price",
        "score",
        "rate",
        "news",
        "latest",
        "aaj",
        "abhi"
    ]

    q = q.lower()

    return any(word in q for word in live_words)

# ---------- Routes ----------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    question = data.get("question", "").strip()

    if not question:
        return jsonify({"answer": "Please enter a question."})

    answer = local_commands(question)

    if answer is None:
        if "weather" in question.lower():
            answer = get_weather(question)
        elif is_live_question(question):
            answer = online_google(question)
        else:
            answer = ai_response(question)

    return jsonify({"answer": answer})

# ---------- Run ----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
