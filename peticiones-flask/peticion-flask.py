from flask import Flask, jsonify

app = Flask(__name__)

videos = [
          {
          "id" : 1,
          "title" : "Avatar"
          },
          {
          "id": 2,
          "title": "Titanic"
          }
          ]

@app.route("/api")
def get_all_videos():

  return jsonify(videos)
  
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

