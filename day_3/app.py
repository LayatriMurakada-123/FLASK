from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def home():
    return f'welcome to day 3 learning about Static vs Dynamic route'

@app.route('/profile/')
def profile():
    return f"i'm layatri"

#static routing --> /name/laya
#dynamic routing --> /name/<name>
@app.route('/name/laya')
def data():
    return f'Welcome laya...'

@app.route('/name/<name>')
def details(name):
    return f'hello {name}'

#now we want to create related to course names
@app.route('/courses/<course_name>')
def courses(course_name):
    return f'The Course is {course_name}'

@app.route('/module/<module_name>')
def modules(module_name):
    return f'The module is <b>{module_name}</b>'
#converter --> int,float,str,path,uuid
#Integer Converter
@app.route('/student/<int:student_id>')
def student(student_id):
    return f'The ID of student is {student_id}'

#Float Converter
@app.route('/student/<float:percentage>')
def student_percentage(percentage):
    return f'The percentage of student is {percentage}'

#path converters
@app.route('/path/<path:file_name>')
def path(file_name):
    return f'file is {file_name}'

#UUID --> Universal Unique Identifier
@app.route('/student_id/<uuid:stu_id>')
def student_id(stu_id):
    return f'The search of the student {stu_id}'
    

if __name__ == "__main__":
    app.run(host='0.0.0.0',  #ipv4 address , integer range of (1 - 65535) 
            port=5100,debug=True)