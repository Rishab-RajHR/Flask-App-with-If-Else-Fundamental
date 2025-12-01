from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def student_profile():
  return render_template(
      "profile.html",
      name="Alex",
      is_topper = True,
      subjects = ["Maths", "Science", "History"]
  )