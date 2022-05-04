from flask import Flask

app = Flask(__name__)

# view function: area "homepage"
@app.route("/") # URL
def homepage():
    hello = ("<h1 style='color:red'>" +
             "Hello World!" +
             "</h1>" +
             
             "<h2 style='color:green'>" +
             "Flask funziona correttamente." +
             "</h2>" +
             
             "<h3 style='color:blue'>" +
             "Visita il sito: \"./contatti\"." +
             "</h3>")

    return hello

# view function: area "contatti"
@app.route("/contatti") # URL
def contatti():
    contatti = "Contattaci al numero:\n+39 0123456789"
    return contatti

if __name__ == '__main__':
    print('Stai eseguendo il file "flask_example.py"!\n')
    print('Permetti l\'attivazione del server in locale dal terminale per accedere ai contenuti:\n' +
          'Terminale - Linux > export FLASK_APP=flask_example.py\n' +
          '    CMD - Windows > set FLASK_APP=flask_example.py\n' +
          '     PS - Windows > env:FLASK_APP = "flask_example.py"\n')
    print('Esegui il comando "flask run" dal terminale per attivare il server.\n')
    print('Visita quindi il sito: "http://127.0.0.1:5000" dal browser ' +
          '(o quello che viene mostrato nel terminale) per raggiungere l\'homepage.')

    
