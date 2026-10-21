from flask import Flask
import uuid

app = Flask(__name__)

@app.route('/')
def home():
    return f"welcome to the home page"

@app.route('/student/<int:id>')
def student_id(id):
    return f'student id : {id}'

@app.route('/student/<float:percentage>')
def student_attendance(percentage):
    return f'student attendence : {percentage}'

@app.route('/skills/<s1>/<s2>')
def skills(s1,s2):
    return f'student has {s1} and {s2} skills'

@app.route('/student/<path:file>')
def student_filepath(file):
    return f'student file : {file}'

@app.route('/student/uuid')
def generate():
    id = uuid.uuid4().hex
    return f'student uuid : {id}'

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5100,debug=True)