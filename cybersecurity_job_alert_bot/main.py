from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_jobs():
    url = "https://ca.indeed.com/jobs?q=cybersecurity&l=Canada&sort=date"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all("a", class_="tapItem")

    job_data = []
    for job in jobs[:10]:
        title_tag = job.find("h2")
        if not title_tag:
            continue
        title = title_tag.text.strip()
        link = "https://ca.indeed.com" + job.get("href")
        snippet = job.find("div", class_="job-snippet")
        snippet_text = snippet.text.strip().replace("\n", " ") if snippet else "No description"
        job_data.append({
            "title": title,
            "link": link,
            "snippet": snippet_text
        })
    return job_data

@app.route("/", methods=["GET"])
def index():
    return jsonify(scrape_jobs())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
