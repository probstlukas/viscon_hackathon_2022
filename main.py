from website import create_app

app = create_app()

# Only run the webserver, if we run this file directly
if __name__ == '__main__':
    app.run(debug=True)