from flask import Flask, jsonify

app=Flask(__name__)
@app.route("/besmart")
def api():
    data= {
        "message": "Welcoome to the Flask API, today we will be learning how to be smart",
        "status": "get smarter"
    }
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)