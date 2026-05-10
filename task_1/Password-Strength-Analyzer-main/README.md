# 🔐 Password Strength Analyzer

A full-stack web application that evaluates the strength of user-entered passwords based on security rules such as length, complexity, and uniqueness.

---

## 🚀 Features

- ✅ Check password **length**
- ✅ Validate **complexity** (uppercase, lowercase, numbers, symbols)
- ✅ Detect **password reuse** using database
- ✅ Suggest **strong alternative passwords**
- ✅ Confirm password validation
- ✅ Show password strength (Weak / Medium / Strong)
- ✅ Secure storage using **hashed passwords**
- ✅ Clean UI with real-time feedback
- ✅ Navigation to welcome page after successful validation

---

## 🧠 Technologies Used

### Frontend
- React.js
- Axios
- React Router

### Backend
- Flask (Python)
- Flask-CORS
- Flask-SQLAlchemy

### Database
- SQLite

---

## 🔐 Security Concepts Used

- Password strength analysis
- Regular expressions (regex)
- SHA-256 hashing
- Password reuse prevention
- Basic authentication flow

---

## 📁 Project Structure
password-analyzer-pro/
│
├── backend/
│ └── app.py
│
├── frontend/
│ └── src/
│ ├── App.js
│ ├── App.css
│ ├── PasswordChecker.js
│ └── Welcome.js

---

## ⚙️ Installation & Setup

### 🔹 Backend

```bash
cd backend
pip install flask flask-cors flask-sqlalchemy
python app.py
cd frontend
npm install
npm install axios react-router-dom
npm start

🌐 Usage
Enter username
Enter password and confirm password
Click Enter
System will:
Analyze password strength
Suggest improvements
Check if password was reused
If valid → redirect to welcome page 🎉
📸 Screenshots

(Add screenshots here if needed)

🎯 Learning Outcome

This project helps understand:

Password security principles
Basic cryptography (hashing)
Full-stack development
API integration
Database usage in web apps
🔮 Future Improvements
🔐 Use bcrypt instead of SHA-256
👤 Add login/register system
🌐 Deploy to cloud (Render / Vercel)
📊 Add password strength meter visualization
🧠 AI-based password suggestions
👨‍💻 Author

Ananda Eswarar A
