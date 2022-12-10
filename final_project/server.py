from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    text = request.args.get('textToTranslate')    
    text = translator.english_to_french(text)

    return text #,200, {'Content-Type': 'text/plain; charset=utf-8'}

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    text = translator.french_to_english(text)
    return text


@app.route("/")
def renderIndexPage():
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
