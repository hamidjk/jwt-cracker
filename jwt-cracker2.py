# Getting started:
# 	pip install pyjwt
# 	pip install cryptography
#   Code By Hamidjk
import jwt

print("""
   ___  _  _ _____  _____        _
  |_|| | | |_   _| /  __ \      | |
    | || |  | | |  | /  \/_ __ __ _| |_ _____ _ __
    | || |/\| | |  | |    | '__/ _` |/ __| |/ / _ \ '__|
   / \/ /\  /\  / | |    | \__/\ | | (_| | (__|   <__/ |
  \____/  \/  \/  \_/     \____/_| \__,_|\___|_|\_\___|_|

This script only supports HS256, HS384, and HS512 algorithms (not RS*).
""")

encoded_payload = input("Enter encoded payload: ")
wordlist_path = input("Path to wordlist: ").rstrip()

try:
    with open(wordlist_path, 'r') as wordlist_file:
        for secret in wordlist_file:
            secret = secret.rstrip()  # Remove trailing newline
            try:
                decoded_payload = jwt.decode(encoded_payload, secret, algorithms=['HS256', 'HS384', 'HS512'])
                print("!! F@CKING Ez !!")
                print(f"** {secret} **")
                print(decoded_payload)
                break  # Exit the loop after successful decryption
            except jwt.exceptions.DecodeError as e:
                print(f"Decoding Error - {secret}: {e}")
            except jwt.exceptions.InvalidTokenError as e:
                print(f"Invalid Token - {secret}: {e}")
            except Exception as e:  # Catch other potential exceptions
                print(f"Uncaught Exception - {secret}: {e}")
except FileNotFoundError as e:
    print(f"Error: Wordlist file not found - {wordlist_path}")
