from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.dp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)





class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)

@app.route("/")
def hello_world():
    #return "Hello World!"
    return render_template('index.html')


@app.route("/products")
def products():
    return "This is product Page"



if __name__ == '__main__':
    app.run(debug=True)