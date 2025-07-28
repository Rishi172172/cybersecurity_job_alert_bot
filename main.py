from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    jobs = [
        {
            "title": "Cybersecurity Analyst – Toronto",
            "link": "https://www.example.com/job1",
            "description": "Looking for a SOC analyst with SIEM experience."
        },
        {
            "title": "SOC Level 1 – Remote",
            "link": "https://www.example.com/job2",
            "description": "Entry-level SOC position available immediately."
        }
    ]
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
