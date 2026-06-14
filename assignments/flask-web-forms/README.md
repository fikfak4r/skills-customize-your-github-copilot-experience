# 📘 Assignment: Interactive Web Forms with Python Flask

## 🎯 Objective

Build a small Flask web app that accepts user input through HTML forms, validates the submission, and displays a personalized response.

## 📝 Tasks

### 🛠️ Create the Flask App

#### Description
Create a Flask application that renders a homepage with a form for the user to enter their name and favorite programming topic.

#### Requirements
Completed app should:

- Use Flask to serve web pages.
- Render an HTML form on the homepage (`/`) with fields for `name` and `favorite topic`.
- Use `GET` and `POST` methods correctly for form submission.

### 🛠️ Process Form Data

#### Description
Handle the form submission and validate the input values on the server.

#### Requirements
Completed app should:

- Accept form submissions at the same route or a separate route.
- Ensure both fields are not empty before rendering the response.
- Show an error message when a field is missing.

### 🛠️ Display a Personalized Response

#### Description
After successful form submission, display a custom response page with the user’s input.

#### Requirements
Completed app should:

- Show the user's name and favorite programming topic.
- Use a template to render the response page.
- Provide a friendly confirmation message, such as `Hello, [name]! Your favorite topic is [topic].`.
