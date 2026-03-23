from flask import Flask
import pymysql

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


@app.route("/voir_artiste")
def voir_artiste():
    