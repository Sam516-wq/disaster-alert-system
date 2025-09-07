from flask import Flask, request, jsonify, render_template
import pandas as pd
import pywhatkit as kit

app = Flask(__name__)

# Load Excel file
try:
    people_df = pd.read_excel("people.xlsx", engine="openpyxl")
    print("✅ Excel file loaded successfully.")
except Exception as e:
    print("❌ Error loading Excel file:", e)
    people_df = pd.DataFrame(columns=["Name", "Age", "Phone"])  # fallback

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send_alert", methods=["POST"])
def send_alert():
    data = request.get_json()
    message = data.get("message", "⚠️ Disaster Alert! Stay safe.")

    responses = []
    for _, row in people_df.iterrows():
        phone = str(row["Phone"])
        if not phone.startswith("+91"):  # Auto add country code if missing
            phone = "+91" + phone

        try:
            # Send WhatsApp message instantly (sends in browser tab)
            kit.sendwhatmsg_instantly(phone, message, wait_time=10, tab_close=True)
            responses.append({"phone": phone, "status": "sent"})
        except Exception as e:
            responses.append({"phone": phone, "status": f"failed: {e}"})

    return jsonify({"message": message, "results": responses})

# ✅ Run in debug mode (auto-reload + error logs)
if __name__ == "__main__":
    app.run(debug=True)
