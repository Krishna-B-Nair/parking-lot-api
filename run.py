from app import create_app

app = create_app()

print("starting server...")

if __name__ == '__main__':
    app.run(debug=True)