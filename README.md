# Password Strength Checker

A Python application that checks the strength of a password.  
It calculates password entropy, checks for required character types, and verifies if the password has been leaked before via the HaveIBeenPwned API.  
This application uses a Tkinter GUI for easy interaction.

---

## Features

- Password length validation
- Character variety check (lowercase, uppercase, numbers, special characters)
- Entropy calculation to measure password strength
- Check if the password has been leaked in data breaches
- Interactive Tkinter GUI

---

## How It Works

1. **User Input**: The user types a password into the GUI.
2. **Password Object**: The input is passed into the `Password` class object.
3. **Validation**: The program checks:
   - Minimum length (12+ characters)
   - Character variety (lowercase, uppercase, digits, special symbols)
4. **Entropy Calculation**: Measures how strong the password is using Shannon entropy.
5. **Pwned Check**: Uses the HaveIBeenPwned API to see if the password has appeared in breaches.
6. **Result Display**: All results are displayed in a popup window.

---

## Usage

1. Clone the repository:
```bash
git clone https://github.com/yourusername/your-repo.git
```

2. Navigate into the project folder:
```bash
cd your-repo
```

3. Run the application:
```bash
python gui.py
```

4. Enter your password in the GUI, click Submit, and view the results in a popup window.


## Project Structure
password-checker/
├── gui.py           # Tkinter GUI and main entry point
├── password_logic.py # Password class with validation and API checks
├── README.md         # Project documentation

## Notes
- This project is for educational purposes and demonstrates Python, OOP, and GUI skills.
- Passwords are not stored anywhere; the HaveIBeenPwned API only receives a hashed prefix for safety.
- Internet connection is required for the password breach check.
- Password requirements are displayed in the GUI while typing.


## License
License
This project is licensed under the MIT License.

