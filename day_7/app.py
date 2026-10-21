from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    data = 25
    #create student details
    student_details = [
        {"id":1,"name":"Laya"},
        {"id":2,"name":"Sindhu"}
    ]


    return render_template('index.html',n=student_details)

@app.route('/about/')
def about():
    return render_template('about.html')

if (__name__=="__main__"):
    app.run(host = "0.0.0.0",
            port = 502,debug=True)