# Student Management REST API

A simple RESTful API built using Flask for managing student records. The application allows adding students, retrieving a student by ID, and viewing all students.

## Features

* Add a new student
* Retrieve a student by ID
* View all students
* Prevent duplicate student IDs
* Validate required fields
* JSON-based API responses

---

## Technologies Used

* Python 3
* Flask
* JSON
* REST API Principles

---

## Data Structure

Each student contains:

* `id`
* `name`
* `course`

Example:

```json
{
  "id": 1,
  "name": "Adithya",
  "course": "Computer Science"
}
```

---

## API Endpoints

### Add Student

**POST /student**

Request:

```json
{
  "id": 1,
  "name": "Adithya",
  "course": "Computer Science"
}
```

Response:

```json
{
  "message": "Student added successfully",
  "Student": {
    "id": 1,
    "name": "Adithya",
    "course": "Computer Science"
  }
}
```

---

### Get Student by ID

**GET /student?id=1**

Returns the details of the specified student.

If the student does not exist:

```json
{
  "message": "Student not found"
}
```

---

### Get All Students

**GET /students**

Returns all students.

---

## Running the Application

Install Flask:

```bash
pip install flask
```

Run the application:

```bash
python app.py
```

The server runs on:

```text
http://127.0.0.1:5001/
```

---

## Learning Objectives

This project was developed to practice:

* Flask routing
* Building REST APIs
* CRUD concepts
* JSON request and response handling
* Route and query parameters
* Input validation
* Error handling
* Managing in-memory data structures

---

## Author

**Adithya K.S.**
