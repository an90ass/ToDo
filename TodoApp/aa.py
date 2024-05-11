from ToDo import app, db

def init_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    init_db()  # Optionally initialize the database
    app.run(debug=True)
