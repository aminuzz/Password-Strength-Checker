# This is a very simple Python script that checks the strength of a password. 
# This script has an Entropy calculation built into it further boosting it's capability
# It also checks if the password has been leaked before via the HaveIBeenPwned API
# Interactable via Tkinter GUI
import string
import math
from typing import Tuple
import hashlib
import requests


class Password:
    # Class attribute
    special_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', "'", '-', '_', '=', '+', '[', ']', '{', '}']


    def __init__(self, password: str):
        self.password = password
        self.conditions = {}




    def password_length(self) -> Tuple[bool, str]:
        length_of_pass = len(self.password)
        if length_of_pass < 12:
            return False, "The password is too short, the minimum length is 12 characters."
        elif 12 <= length_of_pass <= 16:
            return True, "Length requirement has been met."
        else:
            return True, "Length requirement has been met."
        
            


    def check_variety(self) -> Tuple[bool, str]:
        


        lowercase_letters = False
        uppercase_letters = False
        numbers = False
        special_characters = False



        for char in self.password:
            if char in string.ascii_lowercase:
                lowercase_letters = True
            elif char in string.ascii_uppercase:
                uppercase_letters = True
            elif char in string.digits:
                numbers = True
            elif char in Password.special_symbols:
                special_characters = True

        
        self.conditions = {'lowercase letters': lowercase_letters, 'uppercase letters': uppercase_letters, 'numbers': numbers, 'special characters': special_characters}
        



        if all(self.conditions.values()):
            return True, "Requirements met"
        # Don't need an else statement due to the return above if the condition is true

        unsatisfied_conditions = [key for key, value in self.conditions.items() if not value]
        unsatisfied_conditions = ', '.join(unsatisfied_conditions)
        return False, f"Your password is missing: {unsatisfied_conditions}"


    def entropy(self) -> float:

        
        char_set = 0
        length_of_pass = len(self.password)
        
        # Just in case if someone runs the entropy method before the check_variety method
        # Makes sure that entropy doesn't deal with an empty conditions dictionary
        if not self.conditions:
            self.check_variety()
        
        for key, value in self.conditions.items():
            if key == 'lowercase letters' and value:
                char_set += 26
            elif key == 'uppercase letters' and value:
                char_set += 26
            elif key == 'numbers' and value:
                char_set += 10
            elif key == 'special characters' and value:
                char_set += len(Password.special_symbols)
        
        
        
        entropy = round(length_of_pass * math.log2(char_set), 1)
        if entropy == 0:
            return '0 bits', 'Password contains no valid characters.'
        elif entropy < 28:
            return f'{entropy} bits', 'This is a very weak password (can be brute-forced instantaneously)'
        elif 28 <= entropy <= 35:
            return f'{entropy} bits', 'This is weak password'
        elif 36 <= entropy <= 59:
            return f'{entropy} bits', 'This is a reasonable / moderate password'
        elif 60 <= entropy <= 127:
            return f'{entropy} bits', 'This is a strong password'
        elif entropy >= 128:
            return f'{entropy} bits', 'This is a very strong password'
        
        

    def haveibeenpwned(self) -> Tuple[int, str]:
        count = 0
        password_hash = hashlib.sha1(self.password.encode()).hexdigest().upper()
        # encode() --> converts the password string into bytes so SHA-1 can process it
        # hashlib.sha1() --> hashes those bytes produced by the encode function using the SHA-1 algorithm, producing a raw byte hash
        # hexdigest() --> converts the raw byte hash into a readable hexadecimal string.
        # upper() --> makes the hex string uppercase to match the API format.

        first_5_characters, tail = password_hash[:5], password_hash[5:]

        response = requests.get(f'https://api.pwnedpasswords.com/range/{first_5_characters}')
        # Pass the first 5 characters into the API, API responds with list of SHA-1 hashes that share those same first 5 characters 
        # but it gives us the remaining 35 characters (hence 'tail') and the number of times each password was seen in breaches.
        # tail: count



        '''
        hash_dict = {}


        response.text() refers to a string that contains all of the information from the API response. 
        splitlines() refers to splitting each individual string into a list of lines and from there we can split each individual string 
        to have a key, value pair.
        
        for line in response.text.splitlines():
            tail_hash_from_API, count_str = line.split(":")
            hash_dict[tail_hash_from_API] = int(count_str)
        
        if tail in hash_dict:
            count += hash_dict[tail]
            return count, f'Your password has been pwned. Your password has appeared {count} times in data breaches.'
        else:
            return count, f"Your password hasn't appeared in known data breaches."
        
        
        '''


        # Instead of creating a dictionary, we can loop through the values of the API response itself and stop when we find a match.

        for line in response.text.splitlines():
            tail_hash_from_API, count_str = line.split(":")
            if tail_hash_from_API == tail:
                count = int(count_str)
                return count, f'Your password has been pwned. Your password has appeared {count} times in data breaches.'
        return count, f"Your password hasn't appeared in known data breaches."







        

