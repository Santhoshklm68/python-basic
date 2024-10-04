touch cgi-bin/menu_file_access.cgi
chmod +x cgi-bin/menu_file_access.cgi  # Make the file executable


#!/usr/bin/env python3

import cgi
import os

# Enable debugging (useful for finding errors)
import cgitb
cgitb.enable()

# HTML template for the menu page
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Menu</title>
</head>
<body>
    <h1>Select an Option</h1>
    <form method="post" action="/cgi-bin/menu_file_access.cgi">
        <label for="filename">Enter file name:</label><br>
        <input type="text" id="filename" name="filename"><br><br>
        <input type="submit" name="action" value="Read File">
        <input type="submit" name="action" value="Create File">
        <input type="submit" name="action" value="Delete File">
    </form>
    {result}
</body>
</html>
'''

# Processing the form data
form = cgi.FieldStorage()
filename = form.getvalue("filename")
action = form.getvalue("action")
result = ""

if filename and action:
    file_path = os.path.join("/tmp", filename)  # Adjust file path as needed
    if action == "Read File":
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                result = f"<h3>File Content:</h3><pre>{file.read()}</pre>"
        else:
            result = f"<p style='color: red;'>File '{filename}' does not exist.</p>"
    
    elif action == "Create File":
        with open(file_path, "w") as file:
            file.write("This is a new file.\n")
        result = f"<p style='color: green;'>File '{filename}' created successfully.</p>"
    
    elif action == "Delete File":
        if os.path.exists(file_path):
            os.remove(file_path)
            result = f"<p style='color: green;'>File '{filename}' deleted successfully.</p>"
        else:
            result = f"<p style='color: red;'>File '{filename}' does not exist.</p>"

# Generate the HTML output
print("Content-type: text/html\n")
print(html_template.format(result=result))
