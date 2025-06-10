# GPT Community Builder Chatbot

## This app is a tech test for a Community Building Chatbot.

### This app uses the OpenAI API to ask the user (in a hypothetical app with communities) that helps users create their own communities within the app.

### The chatbot asks users questions about the community, (visibility, title, topic, description) and returns a JSON-formatted string that can be used in the background to develop the community from it.

### (Note: the JSON's parameters are set in the model's prompt, and can be easily changed to fit different apps by adding more questions and fields) 

## How to run (Linux instructions):

Start by generating a virtual environment on Python using:

```bash
python3 -m venv .venv
```

Then access that virtual environment with:

```bash
source .venv/bin/activate
```

Please install the necessary packages by running the following command

```bash
pip install -r requirements.txt
```

Make sure create a file called .env in the posts/ folder with the following API keys 

```.env
OPENAI_API_KEY
```

To run the Flask app, run app.py by running:

```bash
python3 app.py
```

The app will try to open on [loca](http://localhost:5000/). If port 5000 is taken, try incrementing the port until you find the one where it is running (or look at the terminal console to see what port it is running on)

