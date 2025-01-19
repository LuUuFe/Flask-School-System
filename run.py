from app import create_app, db
from app import seed

app = create_app()

with app.app_context():
    db.create_all()
    seed.seed_data()

if __name__ == "__main__":
    app.run(debug=True)
