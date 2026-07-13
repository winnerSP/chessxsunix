from flask import Flask, jsonify, request

app = Flask(__name__)

from database import connect


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


# REGISTER

@app.route("/register", methods=["POST"])
def register():

    data = request.json

    username = data["username"]
    password = data["password"]


    db = connect()
    cursor = db.cursor()


    cursor.execute(
        """
        INSERT INTO users(username,password,rating,xp,games)
        VALUES(?,?,?,?,?)
        """,
        (username,password,800,0,0)
    )


    db.commit()
    db.close()


    return {
        "message":"Account created 🚀"
    }



# LOGIN

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



# PROFILE

@app.route("/profile/<username>")
def get_profile(username):

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        SELECT username,rating,xp,games
        FROM users
        WHERE username=?
        """,
        (username,)
    )


    user = cursor.fetchone()


    db.close()


    if user:

        return {

            "username":user[0],
            "rating":user[1],
            "xp":user[2],
            "games":user[3]

        }


    return {

        "message":"Player not found"

    }



# LEADERBOARD

@app.route("/leaderboard")
def leaderboard():

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        SELECT username,rating
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



# DELETE USER (testing)

@app.route("/delete_user/<username>")
def delete_user(username):

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        "DELETE FROM users WHERE username=?",
        (username,)
    )


    db.commit()
    db.close()


    return {

        "message":username + " deleted 🗑️"

    }



# ADD XP

@app.route("/add_xp/<username>/<amount>")
def add_xp(username, amount):

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        UPDATE users
        SET xp=xp+?
        WHERE username=?
        """,
        (int(amount),username)
    )


    db.commit()

    db.close()


    return {

        "message":"XP added 🚀"

    }



# CREATE TOURNAMENT

@app.route("/create_tournament/<name>/<date>")
def create_tournament(name,date):

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        INSERT INTO tournaments(name,date,status)
        VALUES(?,?,?)
        """,
        (name,date,"Open")
    )


    db.commit()

    db.close()


    return {

        "message":"Tournament created 🏆"

    }



# VIEW TOURNAMENTS

@app.route("/tournaments")
def tournaments():

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        "SELECT * FROM tournaments"
    )


    data = cursor.fetchall()


    db.close()


    tournaments=[]


    for t in data:

        tournaments.append({

            "id":t[0],
            "name":t[1],
            "date":t[2],
            "status":t[3]

        })


    return {

        "tournaments":tournaments

    }



if __name__ == "__main__":

    app.run(debug=True)
