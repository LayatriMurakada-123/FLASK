from flask import Flask,render_template,url_for,request,redirect
import uuid
app = Flask(__name__)
#we will generate UUID
@app.route('/')
def home():
    return redirect(url_for('indexPage'))
    #return 'welcome to day4 learning'

@app.route('/about')
def aboutPage():
    return render_template('about.html')

@app.route('/index')
def indexPage():
    return render_template('index.html')

@app.route('/generate')
def generate():
    id = uuid.uuid4().hex
    print(id)
    return f'The generated id is {id}'

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5100,debug=True)

#Build a Student routing app
#Student default page
#Student id
#student attendence
#file path
#student uuid


    
    