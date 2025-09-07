from flask import Flask, request, jsonify, render_template
import pandas as pd
import os

# Detect if running locally or on server
RUN_LOCAL = os.environ.get("RUN_LOCAL", "true").lower() == "true"

if RUN_LOCAL:
    import pywhatkit as kit  # Only import PyWhatKit locally

app = Flask(__name__)

# Load Excel file
try:
    people_df = pd.read_excel("people.xlsx", engine="openpyxl")
    print("✅ Excel file loaded successfully.")
except Exception as e:
    print(f"❌ Error loading Excel file: {e}")
    people_df = pd.DataFrame(columns=["Name", "Age", "Phone"])

@app.route('/')
def index():
    return render_template("index.html", people=people_df.to_dict(orient="records"))

@app.route('/send_alert', methods=['POST'])
def send_alert():
    message = request.json.get("message", "")
    if not message:
        return jsonify({"status": "error", "message": "No message provided"}), 400

    for _, person in people_df.iterrows():
        phone = str(person["Phone"]).strip()

        # Add country code if missing
        if not phone.startswith("+"):
            phone = "+91" + phone  # Change +91 to your country code

        if RUN_LOCAL:
            try:
                kit.sendwhatmsg_instantly(phone, message)
                print(f"✅ Message sent to {phone}")
            except Exception as e:
                print(f"❌ Error sending message to {phone}: {e}")
        else:
            print(f"[SERVER] Would send to {phone}: {message}")

    return jsonify({"status": "success", "message": "Alert processed"})

if __name__ == "__main__":
    print("🚀 Starting Disaster Alert System...")
    app.run(debug=True, host="0.0.0.0")
