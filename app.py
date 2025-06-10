from model import start_chat, continue_chat, strip_json
from flask import Flask, render_template, request, jsonify, session


app = Flask(__name__)
app.secret_key = "secret_key"

# Render the chat.html
@app.route("/")
def index():
    session["messages"] = start_chat()
    return render_template("chat.html")

# Set up post requests for the chat method
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    messages = session.get("messages", start_chat())

    reply, updated_messages, finished, data = continue_chat(messages, user_input)
    session["messages"] = updated_messages

    reply_display = strip_json(reply)

    return jsonify({
        "reply": reply_display,
        "finished": finished,
        "data": data  # send JSON object to frontend
    })

    