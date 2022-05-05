from flask import Flask

app = Flask(__name__)

# view function: "homepage" area
@app.route("/") # URL
def homepage():
    hello = ("<h1 style='color:red'>" +
             "Hello World!" +
             "</h1>" +
             
             "<h2 style='color:green'>" +
             "Flask works correctly." +
             "</h2>" +
             
             "<h3 style='color:blue'>" +
             "Please visit the site: \"./contacts\"." +
             "</h3>")

    return hello

# view function: "contacts" area
@app.route("/contacts") # URL
def contacts():
    contacts = "Contact us:\n+39 0123456789"
    return contacts

if __name__ == '__main__':
    print('Running "browser_page.py"!\n')
    print('Let the local server be activated from the terminal to have access to the contents:\n' +
          'Terminal - Linux > export FLASK_APP=browser_page.py\n' +
          '   CMD - Windows > set FLASK_APP=browser_page.py\n' +
          '    PS - Windows > env:FLASK_APP = "browser_page.py"\n')
    print('Run the "flask run" command from the terminal to activate the server.\n')
    print('Thus, visit the site: "http://127.0.0.1:5000" through the browser ' +
          '(or the site printed on your terminal) in order to reach the homepage.')

    
