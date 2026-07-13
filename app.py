from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():

    return jsonify({
        "message": "♞ CHESS × SUNIX Backend Online",
        "status": "Running 🚀"
    })


@app.route("/stats")
def stats():

    return jsonify({

        "members": "Growing",
        "tournaments": 3,
        "puzzles": "Weekly",
        "status": "Active"

    })


@app.route("/players")
def players():

    return jsonify({

        "players":[
            {
                "name":"Player One",
                "rating":800
            },
            {
                "name":"Player Two",
                "rating":900
            }
        ]

    })


if __name__ == "__main__":

    app.run(debug=True)
