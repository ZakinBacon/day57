from flask import Flask
from flask import render_template
import random
import datetime
import requests

app = Flask(__name__)


def current_year():
    today = datetime.date.today()
    year = today.year
    return year


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    return render_template('index.html', num=random_number, year=current_year())


@app.route("/guess/<string:name>")
def gender_guess(name):
    genderize = requests.get(f"https://api.genderize.io?name={name}")
    genderize = genderize.json()
    agify = requests.get(f"https://api.agify.io?name={name}")
    agify = agify.json()
    gender = genderize['gender']
    age = agify['age']
    name = name.title()
    return render_template('guess.html', name=name, gender=gender, age=age)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
