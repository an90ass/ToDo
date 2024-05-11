from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////Users/anass/Desktop/TodoApp/ToDo.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
@app.route("/")
def index():
    all_to_does =ToDo.query.all()
    """
    [
    {
    "id":1,"title":"test","content":"test", "complete" =0
    }
    .
    .
    }
    ]
    """
    return render_template("index.html",all_to_does=all_to_does)

@app.route("/add", methods=["POST"]) # just to do post request
def addTodo():
    title = request.form.get("title")
    content = request.form.get("content")
    new_to_do = ToDo(title=title,content=content,complete=False)# object
    db.session.add(new_to_do)
    db.session.commit()#update db
    return redirect(url_for("index"))

@app.route("/complete/<string:id>",methods=["Get"])
def complete(id):
    to_do = ToDo.query.filter_by(id=id).first()
    if to_do.complete == False:
        to_do.complete =True
    else:
        to_do.complete =False
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/delete/<string:id>",methods=["Get"])
def delete(id):
    to_do = ToDo.query.filter_by(id=id).first()
    db.session.delete(to_do)
    db.session.commit()#update db
    return redirect(url_for("index"))

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    complete = db.Column(db.Boolean)

if __name__ == '__main__':
    app.run(debug=True)
