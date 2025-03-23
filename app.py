from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to return student number
@app.route('/')
def home():
    return jsonify({"student_number": "123456789"})  # Replace with your actual student number

# Webhook route for Dialogflow fulfillment
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName")

    if intent_name == "ScheduleDevice":
        parameters = req["queryResult"]["parameters"]
        device = parameters.get("device", "your device")
        time = parameters.get("time", "a specified time")
        fulfillment_text = f"Got it! I have scheduled your {device} to turn on/off at {time}."
        return jsonify({"fulfillmentText": fulfillment_text})

    return jsonify({"fulfillmentText": "Sorry, I didn't understand that."})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
