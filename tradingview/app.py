import json, os, config
from flask import Flask, request

app = Flask(__name__)

@app.route("/tradingview-to-discord-study", methods=['POST'])
def discord_study_tv():

    logbot.logs("========== STUDY ==========")
    
    data = json.loads(request.data)

    webhook_passphrase = os.environ.get('WEBHOOK_PASSPHRASE', config.WEBHOOK_PASSPHRASE)

    if 'passphrase' not in data.keys():
        return {
            "success": False,
            "message": "no passphrase entered"
        }

    if data['passphrase'] != webhook_passphrase:
        return {
            "success": False,
            "message": "invalid passphrase"
        }
    del data["passphrase"]

    try:
        chart_url = data["chart_url"]
        del data["chart_url"]
    except KeyError:

    return {
        "success": True
    }