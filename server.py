from flask import Flask, send_file
app = Flask(__name__)

@app.route("/getMap.svg", methods=['GET'])
def getMap():
    return send_file("map.svg")

if __name__ == "__main__":
    app.run()
