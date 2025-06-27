REST API with Flask
--------------------
Description: A simple REST API built using Flask to manage user data. The API supports creating, retrieving, updating, and deleting user records. It uses an in-memory Python dictionary for storing user data during runtime.

Features:
- Provides GET, POST, PUT, and DELETE HTTP methods.
- Stores user data (name and email) in memory.
- Error handling for invalid or missing user records.
- Easy to test using Postman or curl.
  
Functions:
- Accepts and processes JSON data using Flask's request handling.
- Stores user data in a dictionary with auto-incremented integer IDs.
- Performs:
   GET /users → Returns all users
   GET /users/<id> → Returns specific user
   POST /users → Adds a new user
   PUT /users/<id> → Updates an existing user
   DELETE /users/<id> → Deletes a user

Tools used:
- Python 3 – Core programming language.
- Flask – Lightweight web framework to build the API.
- Postman / curl – Used to test HTTP routes and responses. (screenshot of test using curl is in screenshots folder)
- VS Code – To write and manage the Python script.
- Terminal / Command Prompt – To run and test the Flask app
