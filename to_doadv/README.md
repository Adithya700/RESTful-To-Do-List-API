# ToDo REST API

A simple RESTful API built using Flask for managing tasks. The application supports creating, retrieving, updating, deleting, filtering, and searching tasks.

## Features

* Create a new task
* View all tasks
* Retrieve a task by ID
* Filter tasks by completion status
* Filter tasks by priority
* Search tasks by title
* Update task details
* Delete tasks
* JSON-based API responses
* Input validation and error handling

---

## Technologies Used

* Python 3
* Flask
* JSON
* REST API Principles

---

## Data Structure

Each task contains:

* `id`
* `title`
* `priority`
* `completed`

Example:

```json
{
  "id": 1,
  "title": "Complete Flask Assignment",
  "priority": "High",
  "completed": false
}
```

---

## API Endpoints

### Home

**GET /**

Returns:

```json
{
  "message": "Welcome to ToDo API"
}
```

---

### Create Task

**POST /tasks**

Request:

```json
{
  "title": "Complete Flask Assignment",
  "priority": "High"
}
```

---

### Get All Tasks

**GET /tasks**

Returns all tasks.

---

### Filter Tasks by Completion Status

**GET /tasks?completed=true**

Returns completed tasks.

**GET /tasks?completed=false**

Returns incomplete tasks.

---

### Get Task by ID

**GET /tasks/id/<task_id>**

Example:

```text
GET /tasks/id/1
```

---

### Get Tasks by Priority

**GET /tasks/priority/<priority>**

Example:

```text
GET /tasks/priority/High
```

---

### Search Tasks by Title

**GET /tasks/search?title=Flask**

Returns tasks whose titles contain the specified keyword.

---

### Update Task

**PUT /tasks/<task_id>**

Request:

```json
{
  "completed": true
}
```

---

### Delete Task

**DELETE /tasks/<task_id>**

Deletes the specified task.

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
http://127.0.0.1:5000/
```

---

## Learning Objectives

This project was developed to practice:

* Flask application development
* REST API design
* CRUD operations
* Route and query parameters
* JSON request and response handling
* Filtering and searching data
* Validation and error handling

---

## Author

**Adithya K.S.**
