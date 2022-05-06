import sys
import os

# Reach the parent's path
f_path = os.path.dirname(__file__)
root_path = os.path.join(f_path, os.pardir)
sys.path.append(os.path.abspath(root_path))

# Import of the desired module
import src.compute_flask_cv.browser_page import bp

# Test
if __name__ == '__main__':

    # Module correctly imported
    print('"browser_page" imported correctly.')
    print('Start testing "browser_page.py"\n')

    # Instructions
    print(f'Let the local server be activated from the terminal to have access to the contents:\n' +
          f'Terminal - Linux > export FLASK_APP={parent_path}\src\compute_flask_cv\\browser_page.py\n' +
          f'   CMD - Windows > set FLASK_APP={parent_path}\src\compute_flask_cv\\browser_page.py\n' +
          f'    PS - Windows > env:FLASK_APP = "{parent_path}\src\compute_flask_cv\\browser_page.py"\n')
    print('Run the "flask run" command from the terminal to activate the server.\n')
    print('Thus, visit the site: "http://127.0.0.1:5000" through the browser ' +
          '(or the site printed on your terminal) in order to reach the homepage.')
