from flask import Flask, request 
 
app = Flask(__name__) 
students = [] 
 
@app.route("/student", methods=["POST"]) 
def add_user(): 
    data = request.get_json() 
    for student in students:
       if student.get("id") == data.get("id"):
            return {
                "message": "ID already exists"
            }, 400

    if not data.get("name"): 
        return {"error": "Name is required"}, 400 
    if not data.get("course"): 
        return {"error": "Course is required"}, 400 
    students.append(data)
    return { 
        "message": "Student added successfully" ,
        "Student" : data
        
    } 
@app.route("/student", methods=["GET"]) 
def get_student():
    student_id = int(request.args.get("id"))

    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student not found"}, 404
  
@app.route("/students", methods=["GET"]) 
def get_users(): 
    return students
 
if __name__ == "__main__":
    app.run(debug=True, port=5001)