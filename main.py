from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('web/index.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    code = request.form['code']
    response = requests.post('https://replit.com/data/repls/<YOUR_REPL_ID>/result', data={'code': code})
    result = response.json().get('result', '')
    return result

if __name__ == '__main__':
    app.run(debug=True)
