from flask import Flask

from requests import get

app = Flask(__name__)

@app.route("/videos")
def show_video():
	videos = get("http://127.0.0.1:4005/api").json()
	
	return videos[0]["title"]
    
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
