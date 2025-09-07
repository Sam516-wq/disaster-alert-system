# 🌍 Disaster Alert System  

The **Disaster Alert System** is a web-based application built using **Flask** (backend) and **HTML/CSS** (frontend).  
It allows authorities to **send disaster alerts** (like flood, earthquake, or fire warnings) to registered people via **WhatsApp messages**.  

---

## 🚀 Features  
- 📊 Stores people’s details (Name, Age, Phone Number) in an **Excel sheet**.  
- 📩 Sends **WhatsApp alerts** instantly to all registered users.  
- 🌐 Simple **frontend web interface** to trigger alerts.  
- ⚡ Powered by **Flask** backend + **PyWhatKit** for WhatsApp messaging.  
- 🛠️ Easy to extend (add more disaster types, new users, or dashboards).  

---

## 🖥️ Tech Stack  
- **Backend:** Flask (Python)  
- **Frontend:** HTML, CSS (Jinja2 templating)  
- **Database:** Excel (via Pandas & OpenPyXL)  
- **Messaging:** PyWhatKit (WhatsApp automation)  

---

## 📂 Project Structure  
disaster-alert-system/
│── app.py # Flask backend
│── people.xlsx # Excel database (Name, Age, Phone)
│── requirements.txt # Dependencies
│── templates/
│ └── index.html # Frontend page

---

## ⚙️ Setup Instructions  
1. Clone the repository:  
   ```bash
   git clone https://github.com/YOUR-USERNAME/disaster-alert-system.git
   cd disaster-alert-system
2.  Install dependencies:
pip install -r requirements.txt
3.  Run the flask app:
Run the Flask app:
4.  Open in browser:
http://127.0.0.1:5000
📊 Example Excel File (people.xlsx)
Name	Age	Phone
Satyam	18	+918146567907
👨‍💻 Author

Developed by Satyam Jha ✨