from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
Scss(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False
db=SQLAlchemy(app)

#colums of data
class MyTask(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(100),nullable=False)
    complete=db.Column(db.Integer)
    created=db.Column(db.DateTime, default=datetime.utcnow)
 
    #dunder method of string representation
    def __repr__(self):
        return f"Task {self.id}"

#db created
with app.app_context():
        db.create_all()

@app.route("/",methods=["POST","GET"])
def index():
    #add task
    if request.method=="POST":
        current_task=request.form['content']
        new_task=MyTask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"Error:{e}")   
            return f"Error:{e}"
    #see all current tasks    
    else:
        tasks=MyTask.query.order_by(MyTask.created).all()
        return render_template('index.html', tasks=tasks)    

#delete    
@app.route("/delete/<int:id>")
def delete(id:int):
    delete_task=MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"Error {e}"

#edit
@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id:int):
    task=MyTask.query.get_or_404(id)
    if request.method=="POST":
        task.content=request.form['content']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Error:{e}"
    else:
        return render_template('edit.html', task=task)  

#  


#runner and debugger
if __name__=="__main__":

    app.run(debug=True)








