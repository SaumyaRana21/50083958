from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/numbers')
def numbers():
    urls = request.args.getlist('url')
    responses = []
    for url in urls:
        try:
            response = requests.get(url)
            responses.append(response.json())
        except:
            pass
    return jsonify(responses)

if __name__ == '__main__':
    app.run()