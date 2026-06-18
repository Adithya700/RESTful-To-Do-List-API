from flask import Flask, request

app = Flask(__name__)

tasks = []


@app.route("/")
def home():
    return {"message": "Welcome to ToDo API"}

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data:
        return {"error": "Request body required"}, 400

    if not data.get("title"):
        return {"error": "Task title required"}, 400

    if not data.get("priority"):
        return {"error": "Task priority required"}, 400

    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "priority": data["priority"],
        "completed": False
    }

    tasks.append(task)

    return task, 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    completed = request.args.get("completed")

    if completed is None:
        return tasks

    completed = completed.lower() == "true"

    result = []

    for task in tasks:
        if task["completed"] == completed:
            result.append(task)

    return result

@app.route("/tasks/id/<int:task_id>", methods=["GET"])
def get_task(task_id):

    for task in tasks:
        if task["id"] == task_id:
            return task

    return {"error": "Task not found"}, 404

@app.route("/tasks/priority/<task_prio>", methods=["GET"])
def task_priority(task_prio):

    result = []
    for task in tasks:
        if task["priority"].lower() == task_prio.lower():
            result.append(task)

    if result:
        return result

    return {"error": "No tasks with this priority"}, 404

@app.route("/tasks/search", methods=["GET"])
def search_task():

    title = request.args.get("title")

    if not title:
        return {"error": "Title query parameter required"}, 400

    result = []

    for task in tasks:
        if title.lower() in task["title"].lower():
            result.append(task)

    return result

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):

    data = request.get_json()

    for task in tasks:

        if task["id"] == task_id:

            task["title"] = data.get(
                "title",
                task["title"]
            )

            task["priority"] = data.get(
                "priority",
                task["priority"]
            )

            task["completed"] = data.get(
                "completed",
                task["completed"]
            )

            return task

    return {"error": "Task not found"}, 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            return {
                "message": "Task deleted successfully"
            }

    return {"error": "Task not found"}, 404


if __name__ == "__main__":
    app.run(debug=True)