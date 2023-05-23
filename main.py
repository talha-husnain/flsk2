from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)

def real_job():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    columns = result.keys()
    jobs = [dict(zip(columns, row)) for row in result]
    return jobs


@app.route("/")
def hello_world():
  jobs = real_job()
  return render_template('home.html', jobs=jobs, nav="LEARN FLASK")


@app.route("/raw")
def raw():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0", debug=True)
