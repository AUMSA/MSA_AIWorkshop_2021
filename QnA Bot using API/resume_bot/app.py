from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

url = 'https://resume-bot-service.azurewebsites.net/qnamaker/knowledgebases/590d86cf-b7c2-4000-84da-a81cf296c102/generateAnswer'
end_point = '2d45b479-0c40-4d84-a396-e8cbb8b8dc85'

@app.route("/")
def hello():
    return render_template('index.html')
    # return "This is my first flask app"

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


# if __name__ == '__main__':
#     app.run()