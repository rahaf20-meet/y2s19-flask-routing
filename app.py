from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
	students=query_all()
	return render_template('home.html', students=students)
	return "home page" 

@app.route('/student/<int:student_id>')
def display_student(student_id):
	return render_template("student.html", id_number=student_id, home=home, student=query_by_id(student_id))

if __name__ == '__main__':
    app.run(debug=True)
