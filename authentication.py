import json
import hashlib
import os

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


BROKEN_DB = "database.json"
SECURE_DB = "secure_database.json"
PASSWORD_LIST = "1000-most-common-passwords.txt"


def load_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def file_exists(filename):
    return os.path.exists(filename)


def create_salt():
    return os.urandom(16).hex()


def hash_password(password, salt):
    combined = password + salt
    return hashlib.sha256(combined.encode("utf-8")).hexdigest()


def register_broken_user():
    print("\n--- Register New User into Broken Database ---")

    username = input("Create username: ")
    password = input("Create password: ")

    users = load_json(BROKEN_DB)

    for user in users:
        if user["username"] == username:
            print("\nThat username already exists.")
            return

    new_id = str(len(users) + 1)

    new_user = {
        "id": new_id,
        "username": username,
        "password": password
    }

    users.append(new_user)
    save_json(BROKEN_DB, users)

    print("\nUser added to broken database.")
  


def show_broken_database():
    print("\n--- BROKEN STATE: Plain Text Password Database ---")

    users = load_json(BROKEN_DB)

    for user in users:
        print(f"Username: {user['username']} | Password: {user['password']}")

  


def attack_broken_database():
    print("\n--- Insider Attack on Broken Database ---")

    users = load_json(BROKEN_DB)

    for user in users:
        print(f"[COMPROMISED] Username: {user['username']} | Stolen Password: {user['password']}")

def create_secure_database():
    print("\n--- Creating Secure Database with Salted SHA-256 Hashes ---")

    users = load_json(BROKEN_DB)
    secure_users = []

    for user in users:
        salt = create_salt()
        password_hash = hash_password(user["password"], salt)

        secure_users.append({
            "id": user["id"],
            "username": user["username"],
            "salt": salt,
            "password_hash": password_hash
        })

    save_json(SECURE_DB, secure_users)

    print("\nsecure_database.json has been created.")

def show_secure_database():
    print("\n--- SECURE STATE: Salted Hash Database ---")

    if not file_exists(SECURE_DB):
        print("\nSecure database does not exist yet.")
        return

    users = load_json(SECURE_DB)

    for user in users:
        print(f"Username: {user['username']}")
        print(f"Salt: {user['salt']}")
        print(f"Password Hash: {user['password_hash']}")
        print()

def attack_secure_database():
    print("\n--- Insider Dictionary Attack on Secure Database ---")

    if not file_exists(SECURE_DB):
        print("\nSecure database does not exist yet.")
        return

    users = load_json(SECURE_DB)

    with open(PASSWORD_LIST, "r", encoding="utf-8", errors="ignore") as file:
        common_passwords = file.read().splitlines()

    for user in users:
        cracked = False

        for guess in common_passwords:
            guessed_hash = hash_password(guess, user["salt"])

            if guessed_hash == user["password_hash"]:
                print(f"[CRACKED] Username: {user['username']} | Password: {guess}")
                cracked = True
                break

        if not cracked:
            print(f"[SAFE] Username: {user['username']} was not cracked using the 1,000-password list.")

def login_secure_database():
    print("\n--- Login Using Secure Database ---")

    if not file_exists(SECURE_DB):
        print("\nSecure database does not exist yet.")
        return

    username_input = input("Enter username: ")
    password_input = input("Enter password: ")

    users = load_json(SECURE_DB)

    for user in users:
        if user["username"] == username_input:
            input_hash = hash_password(password_input, user["salt"])

            if input_hash == user["password_hash"]:
                print(f"\nLogin successful. Welcome, {username_input}!")
                return
            else:
                print("\nLogin failed. Incorrect password.")
                return

    print("\nLogin failed. Username not found.")


def rsa_confidentiality_demo():
    print("\n--- RSA Confidentiality Demo ---")
    print("please input your message to encrypt:")

    confidential_message = input()
    if not confidential_message:
        print("\nNo message entered. default message will be used.")
        confidential_message = "Detecting multiple leviathan class lifeforms in the region. Are you certain whatever you're doing is worth it?"
    print("\nOriginal confidential message:")
    print(confidential_message)

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    ciphertext = public_key.encrypt(
        confidential_message.encode("utf-8"),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print("\nEncrypted message:")
    print(ciphertext.hex())

    decrypted_message = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print("\nDecrypted message:")
    print(decrypted_message.decode("utf-8"))

def main():
    while True:
        print("\n==============================")
        print(" Login Authentication Project")
        print("==============================")
        print("1. Register new user into broken database")
        print("2. Show broken database")
        print("3. Attack broken database")
        print("4. Create secure database")
        print("5. Show secure database")
        print("6. Attack secure database")
        print("7. Login using secure database")
        print("8. RSA confidentiality demo")
        print("9. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            register_broken_user()
        elif choice == "2":
            show_broken_database()
        elif choice == "3":
            attack_broken_database()
        elif choice == "4":
            create_secure_database()
        elif choice == "5":
            show_secure_database()
        elif choice == "6":
            attack_secure_database()
        elif choice == "7":
            login_secure_database()
        elif choice == "8":
            rsa_confidentiality_demo()
        elif choice == "9":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


main()
