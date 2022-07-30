from flask import Flask, request
import binance

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return "Hello Flask, This is for testing."


@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = json.loads(request.data)
        print(data)
        if data.get('passphrase', None) != config.WEBHOOK_PASSPHRASE:
            return "failure: passphrase is incorrect."

        return "success"
    except Exception as error:
        print(f"error: {error}")
        return "failure"





if __name__ == '__main__':
    
    app.run(host='127.0.0.1', port=8888, debug=False)
