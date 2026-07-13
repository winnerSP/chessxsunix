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

@app.route("/register"...)
@app.route("/login", methods=["POST"])
def login():

    data = request.json

    username = data["username"]
    password = data["password"]


    db = connect()
    cursor = db.cursor()


    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username,password)
    )


    user = cursor.fetchone()


    db.close()


    if user:

        return {
            "message":"Login successful 🚀",
            "username":username
        }


    return {
        "message":"Invalid username or password"
    }
@app.route("/login"...)

@app.route("/profile/<username>")
def get_profile(username):

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        "SELECT username, rating, xp, games FROM users WHERE username=?",
        (username,)
    )


    user = cursor.fetchone()


    db.close()


    if user:

        return {

            "username": user[0],
            "rating": user[1],
            "xp": user[2],
            "games": user[3]

        }


    return {

        "message":"Player not found"

    }

@app.route("/leaderboard")
def leaderboard():

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        SELECT username, rating
        FROM users
        ORDER BY rating DESC
        LIMIT 10
        """
    )


    players = cursor.fetchall()


    db.close()


    result=[]


    for player in players:

        result.append({

            "username":player[0],
            "rating":player[1]

        })


    return {

        "leaderboard":result

    }



if __name__ == "__main__":

    app.run(debug=True)
