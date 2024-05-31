from fastapi import FastAPI, Path
from typing import Optional
app = FastAPI()

students = {
    1: { 
        "name": "John",
		"Text": "What is Lorem Ipsum? Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Why do we use it It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."
	}
}

@app.get("/")
def index():
    return {"name": "First Data"}

## Path Parameters
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view")):
	if student_id not in students:
		return {"Error": "Student not found"}
	return students[student_id]

## Query Parameters
@app.get("/get-by-name")
def get_student(name: Optional[str] = None):
	for student_id in students:
		if students[student_id]["name"] == name:
			return students[student_id]
	return {"Data": "Not found"}

## Path Parameters with Query Parameters
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None):
	for student_id in students:
		if students[student_id]["name"] == name:
			return students[student_id]
	return {"Data": "Not found"}

## Re
    