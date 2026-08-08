from flask import Flask, render_template, request, jsonify
import mysql.connector


app = Flask(__name__)

def get_connection(): 
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="logs_test"
    )

def create_table():
    conn = get_connection()
    cursor = conn.cursor() 

    sql = """
            CREATE TABLE IF NOT EXISTS users (
                user_name VARCHAR(100),
                password VARCHAR(100)
            );
        """

    cursor.execute(sql)

    conn.commit()

    cursor.close()
    conn.close()

@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    conn = get_connection()
    cursor = conn.cursor()

    try: 
        sql = """
            INSERT INTO users
            (user_name, password)
            VALUES(%s, %s)
        """

        cursor.execute(
            sql,
            (username, password)
        )

        conn.commit()

        return jsonify({
            "success": True,
            "message": "Usuário cadastrado com sucesso!"
        })
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    create_table()
    app.run(debug=True)