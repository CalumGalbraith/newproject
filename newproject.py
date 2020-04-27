from pathlib import Path
import sys

invalid_input = True

def start() :
    print("Start your new project")
    name = input("Enter the Project Name: ")
    directory = Path(f"./{name}")

    # If the path does exist run the following
    if directory.is_dir():
        print ("The directory already exists")

    else:
        # Set to False because input was valid
        invalid_input = False

        # Creates directory from user input
        Path(f"./{name}").mkdir(parents=True, exist_ok=True)
        print ("Project Directory Created")
        # Creates app.py in new user directory
        Path(f"{name}/app.py").touch()
        filepath = Path(f"{name}/app.py")

        with filepath.open("a") as f:
            f.write("""from flask import Flask, render_template
            app = Flask(__name__)

            @app.route("/")
            def index():
                return render_template ("index.html")""")
            f.close()
            print ("app.py Created")

        Path(f"{name}/#.flaskenv").touch()
        filepath = Path(f"{name}/#.flaskenv")

        with filepath.open("a") as f:
            f.write("""FLASK_APP=app.py
FLASK_ENV=development""")
            f.close()
            print ("Flask Environment set")

        # Creates templates directory inside new user directory
        Path(f"{name}/templates").mkdir(parents=True, exist_ok=True)
        print ("Templates directory created")

        # Creates static directory inside new user directory
        Path(f"{name}/static").mkdir(parents=True, exist_ok=True)
        print ("Static directory created")

        # Creates index.html in templates directory
        Path(f"{name}/static/style.css").touch()
        print ("style.css created")

        # Creates index.html in templates directory
        Path(f"{name}/templates/index.html").touch()
        filepath = Path(f"{name}/templates/index.html")

        with filepath.open("a") as f:
            f.write("""{% extends "layout.html" %}

{% block heading %}

{% endblock %}

{% block body %}

{% endblock %}""")
            f.close()
            print ("index.html created")

        # Creates layout.html in templates directory
        Path(f"{name}/templates/layout.html").touch()
        filepath = Path(f"{name}/templates/layout.html")

        with filepath.open("a") as f:
            f.write(""" <!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="static/style.css">
        <title> </title>
    </head>
    <body>
        <h1>{% block heading %}{% endblock %}</h1>

        {% block body %}
        {% endblock %}

    </body>
</html>""")
            f.close()
            print ("layout.html created")
            print ("Setup Complete")

        sys.exit()

# this will loop until user enters a valid directory
while invalid_input :
    start()
