from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

url = '<your-url>'
end_point = '<your-endpoint>'

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/ask/<text>")
def ask(text):
    headers = {
        'Authorization': 'EndpointKey ' + str(end_point).strip(),
        'Content-type': 'application/json',
    }

    data = """{'question':'"""+text+"""'}"""

    response = requests.post(
                    str(url).strip(), 
                    headers=headers, 
                    data=data
                )
    information = json.loads(response.text)
    return information['answers'][0]['answer']
