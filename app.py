from flask import Flask, jsonify

app = Flask(__name__)

from database import connect


@app.route("/add_player/<name>/<rating>")
def add_player(name, rating):

    db = connect()

    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO players(username, rating, games) VALUES (?, ?, ?)",
        (name, int(rating), 0)
    )

    db.commit()
    db.close()

    return {
        "message": "Player Added 🚀"
    }


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
