from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to return student number
@app.route('/')
def home():
    return jsonify({"student_number": "200593016"})

# Webhook route for Dialogflow fulfillment
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return jsonify({"message": "Webhook is live!"})

    req = request.get_json(silent=True, force=True)
    if not req:
        return jsonify({"fulfillmentText": "Invalid request: No JSON received"}), 400

    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName")

    if intent_name == "ScheduleDevice":
        parameters = req.get("queryResult", {}).get("parameters", {})
        device = parameters.get("device", "your device")
        time = parameters.get("time", "a specified time")

        fulfillment_text = f"Got it! I have scheduled your {device} to turn on/off at {time}."
        return jsonify({"fulfillmentText": fulfillment_text})

    return jsonify({"fulfillmentText": "Sorry, I didn't understand that."})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
