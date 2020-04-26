from pathlib import Path
import os

#Askes User for folder name
name = input("Enter the Project Name: ")

# Check to see if the already directory exsists
# Set directory to user input
path = f"./{name}"

# Check whether the specified path exists
isExist = os.path.exists(path)

# If it exists return this error
if (isExist) == True:
    print("The directory already exists")
    
# If the directory does not exist run this script
else:
# Creates directory from user input
    os.mkdir(f"{name}")

    os.path.dirname(f"{name}")

# Creates app.py in new user directory
    Path(f"{name}/app.py").touch()

# Creates templates directory inside new user directory
    os.mkdir(f"{name}/templates")

# Creates index.html in templates directory
    Path(f"{name}/templates/index.html").touch()

# Creates layout.html in templates directory
    Path(f"{name}/templates/layout.html").touch()
