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
            f.write('from flask import Flask, render_template \n')
            f.write('app = Flask(__name__) \n')
            f.write(' /n')
            f.write('@app.route("/") \n')
            f.write(' /n')
            f.write('def index(): \n')
            f.write('\treturn render_template ("index.html")')
            f.close()
            print ("app.py Created")
        # Creates templates directory inside new user directory
        Path(f"{name}/templates").mkdir(parents=True, exist_ok=True)
        print ("Templates directory created")

        # Creates static directory inside new user directory
        Path(f"{name}/static").mkdir(parents=True, exist_ok=True)
        print ("Static directory created")

        # Creates index.html in templates directory
        Path(f"{name}/static/style.css").touch()

        # Creates index.html in templates directory
        Path(f"{name}/templates/index.html").touch()
        filepath = Path(f"{name}/templates/index.html")

        with filepath.open("a") as f:
            f.write('{% extends "layout.html" %} \n')
            f.write('{% block heading %} \n')
            f.write(' \n')
            f.write('{% endblock %} \n')
            f.write(' \n')
            f.write('{% body block %} \n')
            f.write(' \n')
            f.write('{% endblock %} \n')
        print ("index.html created")

        # Creates layout.html in templates directory
        Path(f"{name}/templates/layout.html").touch()
        filepath = Path(f"{name}/templates/layout.html")

        with filepath.open("a") as f:
            f.write('<!DOCTYPE html> \n')
            f.write('<html> \n')
            f.write('\t<head> \n')
            f.write('\t<link rel="stylesheet" href="static/styles.css"> \n')
            f.write('\t\t<title> </title> \n')
            f.write('\t</head> \n')
            f.write('\t<body>\n')
            f.write('\t\t<h1>{% block heading %}{% endblock %}</h1> \n')
            f.write('\t\t{% block body %} \n')
            f.write('\t\t{% endblock %} \n')
            f.write('\t</body>\n')
            f.write('</html>')
            f.close()
            print ("layout.html created")
            print ("Setup Complete")

        sys.exit()

# this will loop until user enters a valid directory
while invalid_input :
    start()
