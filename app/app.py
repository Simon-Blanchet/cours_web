from flask import Flask, request, render_template
import pymysql
import pymysql.cursors

app = Flask(__name__)
 
@app.route("/")
def hello_world():
    conn = pymysql.connect(
        user = "root",
        password = "uimm",
        host = "localhost",
        port =3306,
        database= "spectacle")
    cursor= conn.cursor()
    cursor.execute ('SELECT * from Artistes')
    result = cursor.fetchone()
    
    return f"<p>Hello, World! {result}</p>"


@app.route("/artists", methods=["GET", "POST"])
def show_artists():
    artists = None
    if request.method == "POST":
        query = request.form.get("query")
        conn = pymysql.connect(
            user="root",
            password="uimm",
            host="localhost",  # ou le nom du service mysql/mariadb du docker-compose
            port=3306,
            database="spectacle",
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = conn.cursor()
        print(f"SELECT * FROM Artistes WHERE nom LIKE '{query}'")
        # cursor.execute(f"SELECT * FROM artiste WHERE nom LIKE '{query}'")
        cursor.execute("SELECT * FROM Artistes WHERE nom LIKE %s", (f"%{query}%",))
        result = cursor.fetchall()
        artists = [artist for artist in result]
    return render_template("index.html", artists=artists)
