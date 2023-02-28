import os

import openai
from flask import Flask, redirect, render_template, request, url_for
from speech_recognition import recognize_from_microphone


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = recognize_from_microphone()
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt= question,
            temperature=0.6,
            max_tokens = 500 # Nombre de caractère à l'affichage
        )

    

        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


