import sys, os
f_path = os.path.dirname(__file__)
parent_path = os.path.join(f_path, '..')
sys.path.append(os.path.abspath(parent_path))

from src.example_package.flask_example import *

if __name__ == '__main__':
    print('Modulo "flask_example" importato correttamente.')
    print('Avvio test del modulo "flask_example.py"\n')
    print('Permetti l\'attivazione del server in locale dal terminale per accedere ai contenuti:\n' +
          'Terminale - Linux > export FLASK_APP=test_flask_example.py\n' +
          '    CMD - Windows > set FLASK_APP=test_flask_example.py\n' +
          '     PS - Windows > env:FLASK_APP = "test_flask_example.py"\n')
    print('Esegui il comando "flask run" dal terminale per attivare il server.\n')
    print('Visita quindi il sito: "http://127.0.0.1:5000" dal browser ' +
          '(o quello che viene mostrato nel terminale) per raggiungere l\'homepage.')
