from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI();
students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "Year 12"
    },
    2: {
        "name": "Yaseen",
        "age": 18,
        "class": "Uni"
    },
    3: {
        "name": "Matin",
        "age": 16,
        "class": "Year 11"
    }
}
@app.get("/")
def index():
    return{"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="Enter the ID of the student you want to view", gt = 0, lt = 3)):
    return students[student_id]

@app.get("/get-by-name")
def get_student(*, name : Optional[str] = None, test : int):
   for student_id in students:
    if students[student_id]["name"] == name:
       return students[student_id]
    return {"Data" : "Not Found"}

