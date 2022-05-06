from flask import Flask

app = Flask(__name__)

# view function: "homepage" area
@app.route("/") # URL
def homepage():
    hello = (
        "<h1 style='color:red'>" +
        "Hello World!" +
        "</h1>" +

        "<h2 style='color:green'>" +
        "Flask works correctly." +
        "</h2>" +

        "<h3 style='color:blue'>" +
        "Please visit the site: \"./contacts\"." +
        "</h3>"
        )
    return hello

# view function: "contacts" area
@app.route("/contacts") # URL
def contacts():
    import jsonify
    contacts = {"data": [+342111, +325555]}
    return jsonify(contacts)

if __name__ == '__main__':
    print('Running "browser_page.py"!\n')
    print('\nHELP')
    print('1) Let the local server be activated from the terminal to have access to the contents:\n' +
          '   Terminal  - Linux  > export FLASK_APP=browser_page.py\n' +
          '        CMD - Windows > set FLASK_APP=browser_page.py\n' +
          '         PS - Windows > env:FLASK_APP = "browser_page.py"')
    print('2) Let the FLASK environment be set on "development" status:\n' +
          '   Terminal - Linux > export FLASK_ENV=development\n' +
          '        CMD - Windows > set FLASK_ENV=development\n' +
          '         PS - Windows > env:FLASK_ENV = "development"')
    print('3) Thus, visit the site: "http://127.0.0.1:5000" through the browser\n' +
          '   (or the site printed on your terminal) in order to reach the homepage.\n\n')
    app.run()
    
