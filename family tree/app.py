# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/index")
def home():

    name = "Harshit" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def home():

    name = "Bhramha" # write your name
    age = "40" # write your age

    return render_template('father.html' , name = name , age = age)
# define the route to mother webpage
@app.route("/mother")
def home():

    name = "Rama Shanthi" # write your name
    age = "39" # write your age

    return render_template('mother.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/friend")
def home():

    name = "Harsha" # write your name
    age = "14" # write your age

    return render_template('friends.html' , name = name , age = age)
# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
