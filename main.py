from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'name': "Talha",
  'age': 47,
}, {
  'id': 2,
  'name': "Talha",
  'age': 47,
}, {
  'id': 3,
  'name': "Talha",
  'age': 47,
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, nav="LEARN FLASK")


@app.route("/raw")
def raw():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0", debug=True)
 