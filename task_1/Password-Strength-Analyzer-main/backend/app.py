from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import re, random, string, hashlib

app = Flask(__name__)
CORS(app)

# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passwords.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# TABLE
class UserPassword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String(200))

with app.app_context():
    db.create_all()

# HASH
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# PASSWORD GENERATOR
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(12))

# ANALYZE
def analyze(username, password):
    score = 0
    feedback = []

    if len(password) >= 12: score += 2
    elif len(password) >= 8: score += 1
    else: feedback.append("Use at least 8 characters")

    if re.search(r"[a-z]", password): score += 1
    else: feedback.append("Add lowercase letters")

    if re.search(r"[A-Z]", password): score += 1
    else: feedback.append("Add uppercase letters")

    if re.search(r"[0-9]", password): score += 1
    else: feedback.append("Include numbers")

    if re.search(r"[!@#$%^&*()]", password): score += 1
    else: feedback.append("Add special characters")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    hashed = hash_password(password)

    reused = UserPassword.query.filter_by(
        username=username,
        password_hash=hashed
    ).first() is not None

    suggestion = generate_password() if strength != "Strong" else ""

    return strength, feedback, reused, suggestion, hashed

# ✅ HOME ROUTE (fixes 404)
@app.route("/")
def home():
    return "✅ Backend Running"

# CHECK
@app.route("/check", methods=["POST"])
def check():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    strength, feedback, reused, suggestion, _ = analyze(username, password)

    return jsonify({
        "strength": strength,
        "feedback": feedback,
        "reused": reused,
        "suggestion": suggestion
    })

# SAVE
@app.route("/save", methods=["POST"])
def save():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    hashed = hash_password(password)

    db.session.add(UserPassword(username=username, password_hash=hashed))
    db.session.commit()

    return jsonify({"status": "saved"})

if __name__ == "__main__":
    app.run(debug=True)