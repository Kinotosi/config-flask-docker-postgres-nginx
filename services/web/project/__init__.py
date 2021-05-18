from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

my_host = "localhost:1337"

class Siswa(db.Model):
    nis = db.Column(db.Integer, primary_key=True, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    tempat_lahir = db.Column(db.String(100), nullable=False)
    tanggal_lahir = db.Column(db.String(20), nullable=False)
    alamat = db.Column(db.String(255), nullable=False)

    def __init__(self, nis, nama, tempat_lahir, tanggal_lahir, alamat):
        self.nis = nis
        self.nama = nama
        self.tempat_lahir = tempat_lahir
        self.tanggal_lahir = tanggal_lahir
        self.alamat = alamat

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nis = request.form["nis"]
        nama = request.form["nama"]
        tempat_lahir = request.form["tempat_lahir"]
        tanggal_lahir = request.form["tanggal_lahir"]
        alamat = request.form["alamat"]

        add_data = Siswa(nis, nama, tempat_lahir, tanggal_lahir, alamat)
        db.session.add(add_data)
        db.session.commit()

        return redirect("http://localhost:1337/list")

    return render_template("index.html")

@app.route("/list")
def listSiswa():
    data_siswa = db.session.query(Siswa)
    return render_template("list.html", data_siswa=data_siswa)
