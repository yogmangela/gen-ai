
from flask import Flask, render_template, request, redirect, url_for, flash
from secure_storage import cipher
import database
import sqlite3

app = Flask(__name__)
app.secret_key = "super_secret_key"

@app.route("/")
def home():
    conn = sqlite3.connect("data_security.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, classification, encrypted_data FROM records")
    records = cursor.fetchall()
    conn.close()
    return render_template("index.html", records=records)

@app.route("/add", methods=["POST"])
def add_data():
    data = request.form["data"]
    classification = classify_data(data)
    encrypted_data = cipher.encrypt(data.encode()).decode()
    
    conn = sqlite3.connect("data_security.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO records (data, classification, encrypted_data) VALUES (?, ?, ?)", 
                   (data, classification, encrypted_data))
    conn.commit()
    conn.close()
    
    database.log_action("Data Added", f"Classified as {classification}")
    flash("Data stored securely!", "success")
    
    return redirect(url_for("home"))

@app.route("/delete/<int:id>")
def delete_record(id):
    conn = sqlite3.connect("data_security.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM records WHERE id=?", (id,))
    conn.commit()
    conn.close()
    
    database.log_action("Data Deleted", f"Record ID: {id}")
    flash("Record deleted successfully!", "danger")
    
    return redirect(url_for("home"))

def classify_data(data):
    PII_KEYWORDS = ["name", "email", "phone", "address", "ssn"]
    PHI_KEYWORDS = ["medical", "diagnosis", "prescription", "treatment"]
    
    for keyword in PII_KEYWORDS:
        if keyword in data.lower():
            return "Confidential (PII detected)"
    
    for keyword in PHI_KEYWORDS:
        if keyword in data.lower():
            return "Restricted (PHI detected)"
    
    return "Public (No sensitive data detected)"

if __name__ == "__main__":
    app.run(debug=True)