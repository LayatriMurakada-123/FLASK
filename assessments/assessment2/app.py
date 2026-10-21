from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)


# 1. Home page
@app.route("/")
def home():
    return render_template("home.html")


# 2. About page
@app.route("/about")
def about():
    return render_template("about.html")


# 3. GET request - Get name and batchno using Postman
@app.route("/getdata", methods=["GET"])
def getdata():
    name = request.args.get("name")
    batchno = request.args.get("batchno")

    return f'name is {name}, batchno is {batchno}'

# 4. POST request - Get name and skills using JSON in Postman
@app.route("/postdata", methods=["POST"])
def postdata():
    data = request.get_json()
    name = data.get("name")
    skills = data.get("skills")
    return f'name is {name}, skills are {skills}'


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5200,debug=True)