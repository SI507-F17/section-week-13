from flask import Flask, request, render_template
import requests

app = Flask(__name__)


def duck_answer_this(question):
    # based on https://duckduckgo.com/api
    response = requests.get('http://api.duckduckgo.com/', params={
        'q': question,
        'format': 'json'
    })
    # print(response.text)
    result = response.json()
    return result


@app.route('/')
def index():
    question = None
    answer = None
    result = {}
    if request.args:
        question = request.args.get('q')
        if question:
            # TODO get result and answer values
            #print(question)
            result = duck_answer_this(question)
            #print(result)
            answer = result['Answer'] or result['AbstractText'] # For example

    # always looks for template in 'templates' folder relative to the current folder
    return render_template('index.html', question=question, answer=answer, result=result)

if __name__ == '__main__':
    # auto reloads (mostly) new code and shows exception traceback in the browser
    app.run(use_reloader=True, debug=True)
