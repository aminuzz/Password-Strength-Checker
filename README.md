# Password Strength Checker 🔐

A Python application that helps you **assess the strength of your passwords**.  
It combines entropy calculation, character variety checks, and the HaveIBeenPwned API to see if your password has been leaked.  
All of this comes together in a simple **Tkinter GUI** for interactive use 💻✨.

---

## 🚀 Features

- ✅ Password length validation (minimum 12 characters)  
- ✅ Character variety check (lowercase, uppercase, numbers, special symbols)  
- ✅ Entropy calculation to measure password strength  
- ✅ Check if the password has been exposed in data breaches via the HaveIBeenPwned API  
- ✅ Simple Tkinter GUI for easy interaction  

---

## 🛠 How It Works

1. **User Input**: Type your password into the GUI.  
2. **Password Object**: Your input is wrapped in the `Password` class.  
3. **Validation**: The program checks:
   - Minimum length requirement  
   - Character variety (lowercase, uppercase, digits, symbols)  
4. **Entropy Calculation**: Determines password strength using Shannon entropy.  
5. **Pwned Check**: Verifies if the password exists in known breaches.  
6. **Result Display**: Shows results in a popup window with all findings.  

---

## 💻 Usage

1. Clone the repository:
```bash
git clone https://github.com/aminuzz/Password-Strength-Checker.git
```
2. Navigate into the project folder:
```bash
cd Password-Strength-Checker
```
3. Run the application:
```bash
python gui.py
```
Type your password in the GUI, click Submit, and view your results in the popup!



## 📂 Project Structure
```
password-checker/
├── gui.py           # Tkinter GUI and main entry point
├── password_logic.py # Password class with validation and API checks
├── README.md         # Project documentation
```

## 📝 Notes
- This project is for educational purposes and demonstrates Python, OOP, and GUI skills.
- Passwords are not stored; the HaveIBeenPwned API only receives a hashed prefix for safety.
- Internet connection is required for the password breach check.
- Password requirements are displayed in the GUI while typing.



## ⚠️ Disclaimer
This content is for educational purposes only. The HaveIBeenPwned API is used to illustrate password security.
All credit for the HaveIBeenPwned service goes to Troy Hunt and his team.

## 🧾 License
This project is licensed under the MIT License.

