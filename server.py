from flask import Flask, send_file
app = Flask(__name__)


@app.route("/map", methods=['GET'])
def getMap():
    return send_file("static/map.svg")

@app.route("/image/<imageId>")
def getImage(imageId):
    return send_file("static/" + imageId + ".svg")


if __name__ == "__main__":
    app.run()
