import sqlite3

DATABASE = "users.db"

def init_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    """)

    cursor.execute(
        "INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'admin123')"
    )

    connection.commit()
    connection.close()


def login(username, password):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

    cursor.execute(query)
    user = cursor.fetchone()

    connection.close()

    if user:
        print("Login successful!")
        print("Welcome,", user[1])
    else:
        print("Invalid username or password.")


def main():
    init_database()

    print("=== User Login System ===")
    username = input("Username: ")
    password = input("Password: ")

    login(username, password)


if __name__ == "__main__":
    main()
