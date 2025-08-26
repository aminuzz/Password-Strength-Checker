import tkinter as tk
from tkinter import messagebox
from password_logic import Password

# Setup Window
root_window = tk.Tk()
root_window.geometry("800x400")
root_window.title("Password Strength Checker")

# Title Label
title_label = tk.Label(root_window, text="Password Strength Checker", font=('Arial', 18))
title_label.pack(padx=20, pady=20)

# Password Entry
password_entry = tk.Entry(root_window, font=('Arial', 14), show="*")
password_entry.pack(pady=10)

# Individual requirement labels
lowercase_label = tk.Label(root_window, text="Lowercase letter: ❌", font=('Arial', 12), fg="red")
uppercase_label = tk.Label(root_window, text="Uppercase letter: ❌", font=('Arial', 12), fg="red")
number_label = tk.Label(root_window, text="Number: ❌", font=('Arial', 12), fg="red")
special_label = tk.Label(root_window, text="Special character: ❌", font=('Arial', 12), fg="red")
length_label = tk.Label(root_window, text="Minimum length 12: ❌", font=('Arial', 12), fg="red")

lowercase_label.pack()
uppercase_label.pack()
number_label.pack()
special_label.pack()
length_label.pack()

# Functions
def update_feedback(event=None):
    """Live feedback as the user types"""
    user_input = password_entry.get()
    if not user_input:
        lowercase_label.config(text="Lowercase letter: ❌", fg="red")
        uppercase_label.config(text="Uppercase letter: ❌", fg="red")
        number_label.config(text="Number: ❌", fg="red")
        special_label.config(text="Special character: ❌", fg="red")
        length_label.config(text="Minimum length 12: ❌", fg="red")
        return

    temp_password = Password(user_input)
    length_ok, _ = temp_password.password_length()
    variety_ok, _ = temp_password.check_variety()  # updates temp_password.conditions

    # Update individual labels
    lowercase_label.config(
        text=f"Lowercase letter: {'✅' if temp_password.conditions.get('lowercase letters') else '❌'}",
        fg="green" if temp_password.conditions.get('lowercase letters') else "red"
    )
    uppercase_label.config(
        text=f"Uppercase letter: {'✅' if temp_password.conditions.get('uppercase letters') else '❌'}",
        fg="green" if temp_password.conditions.get('uppercase letters') else "red"
    )
    number_label.config(
        text=f"Number: {'✅' if temp_password.conditions.get('numbers') else '❌'}",
        fg="green" if temp_password.conditions.get('numbers') else "red"
    )
    special_label.config(
        text=f"Special character: {'✅' if temp_password.conditions.get('special characters') else '❌'}",
        fg="green" if temp_password.conditions.get('special characters') else "red"
    )
    length_label.config(
        text=f"Minimum length 12: {'✅' if length_ok else '❌'}",
        fg="green" if length_ok else "red"
    )

def submit_password():
    """Submit password to check with HIBP API and show popup"""
    user_input = password_entry.get()
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter a password")
        return

    my_password = Password(user_input)
    _, _ = my_password.password_length()
    _, variety_message = my_password.check_variety()
    _, entropy_message = my_password.entropy()
    _, pwned_message = my_password.haveibeenpwned()

    # Combine results for popup
    result_text = f"{variety_message}\n{entropy_message}\n{pwned_message}"
    messagebox.showinfo("Password Results", result_text)


password_entry.bind("<KeyRelease>", update_feedback)

# Submit Button
submit_button = tk.Button(root_window, text="Submit Password", font=('Arial', 14), command=submit_password)
submit_button.pack(pady=20)


root_window.mainloop()
