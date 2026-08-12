import sqlite3
import hashlib
import os
import re
import getpass

DATABASE = "users.db"


def hash_password(password):
    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )
    return salt.hex() + ":" + password_hash.hex()


def verify_password(password, stored_password):
    try:
        salt_hex, hash_hex = stored_password.split(":")
        salt = bytes.fromhex(salt_hex)

        password_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            salt,
            100000
        )

        return password_hash.hex() == hash_hex

    except (ValueError, TypeError):
        return False


def init_database():
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def validate_username(username):
    return bool(re.fullmatch(r"[A-Za-z0-9_]{3,30}", username))


def register_user(username, password):
    if not validate_username(username):
        print("Invalid username. Use 3-30 letters, numbers, or underscores.")
        return

    if len(password) < 8:
        print("Password must contain at least 8 characters.")
        return

    password_hash = hash_password(password)

    connection = sqlite3.connect(DATABASE)

    try:
        connection.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, password_hash)
        )

        connection.commit()
        print("Registration successful.")

    except sqlite3.IntegrityError:
        print("Username already exists.")

    finally:
        connection.close()


def login(username, password):
    if not validate_username(username):
        print("Invalid username format.")
        return

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        "SELECT username, password_hash FROM users WHERE username = ?",
        (username,)
    )

    user = cursor.fetchone()

    connection.close()

    if user and verify_password(password, user[1]):
        print("Login successful!")
        print("Welcome,", user[0])
    else:
        print("Invalid username or password.")


def main():
    init_database()

    print("=== Secure User Authentication System ===")
    print("1. Register")
    print("2. Login")

    choice = input("Choose an option: ").strip()

    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")

    if choice == "1":
        register_user(username, password)
    elif choice == "2":
        login(username, password)
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
