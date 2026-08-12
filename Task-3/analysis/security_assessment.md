# Secure Code Assessment

## 1. Introduction

This project performs a security assessment of a Python-based user authentication application. The source code was manually reviewed to identify common security weaknesses and coding flaws.

The assessment focuses on authentication security, password protection, database security, input handling, and secure coding practices.

## 2. Application Overview

The application is a simple Python login system that uses SQLite to store user credentials.

### Technologies Used

- Python
- SQLite
- Manual Source Code Review

## 3. Security Assessment Method

A manual source-code security review was performed.

The following areas were examined:

- Authentication
- Password storage
- Database queries
- User input handling
- Credential management
- Error handling
- Secure coding practices

## 4. Vulnerabilities Identified

### 4.1 SQL Injection

**Severity:** High

The application directly inserts user input into an SQL query using an f-string:

```python
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
