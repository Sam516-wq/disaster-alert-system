from flask import Flask, request, jsonify, render_template
import pandas as pd
import pywhatkit as kit
import os

app = Flask(__name__)

# ✅ Load Excel file
EXCEL_FILE = "people.xlsx"
if os.path.exists(EXCEL_FILE):
    people_df = pd.read_excel(EXCEL_FILE, engine="openpyxl")
    print("✅ Excel file loaded successfully.")
else:
    people_df = pd.DataFrame(columns=["Name", "Age", "Phone"])
    print("⚠️ No Excel file found. Created empty DataFrame.")

# ✅ Ensure phone numbers start with +
def format_phone(phone):
    phone = str(phone).strip()
    if not phone.startswith("+91"):  # default India
        return "+91" + phone.lstrip("0")
    return phone

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send_alert", methods=["POST"])
def send_alert():
    try:
        data = request.get_json() or request.form
        message = data.get("message", "").strip()

        if not message:
            return jsonify({"error": "Message cannot be empty"}), 400

        for _, row in people_df.iterrows():
            name = row.get("Name", "User")
            phone = format_phone(row.get("Phone", ""))
            if not phone:
                continue

            print(f"📤 Sending alert to {name} ({phone})...")

            try:
                # Send WhatsApp message
                kit.sendwhatmsg_instantly(phone, f"⚠️ ALERT: {message}")
                print(f"✅ Sent to {name}")
            except Exception as e:
                print(f"❌ Failed for {name} ({phone}): {e}")

        return jsonify({"message": message, "status": "success"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("🚀 Starting Disaster Alert System...")
    app.run(debug=True)
