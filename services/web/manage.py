from flask.cli import FlaskGroup
from project import app, db 
import os

cli = FlaskGroup(app)

@cli.command("create_db")
def create_deb():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == "__main__":
    cli()