import os

# # Block avoided in order to test the "export PYTHONPATH=src"
# # command in the "applications-test.yml" file
# import sys
#
# # Reach the parent's path
# f_path = os.path.dirname(__file__)
# root_path = os.path.join(f_path, os.pardir)
# sys.path.append(os.path.abspath(root_path))

# Import of the desired module
import src.compute_flask_cv.browser_page as bp


# pytest
def test_homepage():
    text_homepage = (
        "<h1 style='color:red'>" +
        "Hello World!" +
        "</h1>" +

        "<h2 style='color:green'>" +
        "Flask works correctly." +
        "</h2>" +

        "<h3 style='color:blue'>" +
        "Please visit the site: \"./contacts\"." +
        "</h3>")
    assert bp.homepage() == text_homepage


def test_contacts():
    text_contacts = {"data": [+342111, +325555]}
    assert bp.contacts() == text_contacts


# Test as main
if __name__ == '__main__':

    # Module correctly imported
    print('"browser_page" imported correctly.')
    print('Start testing "browser_page.py"\n')
    
    # Instructions
    f_path = os.path.dirname(__file__)
    root_path = os.path.join(f_path, os.pardir)
    print('\nHELP')
    print(f'1) Let the local server be activated from the terminal to have access to the contents:\n' +
          f'   Terminal -  Linux  > export FLASK_APP={root_path}\\src\\compute_flask_cv\\browser_page.py\n' +
          f'        CMD - Windows > set FLASK_APP={root_path}\\src\\compute_flask_cv\\browser_page.py\n' +
          f'         PS - Windows > env:FLASK_APP = "{root_path}\\src\\compute_flask_cv\\browser_page.py"')
    print('2) Let the FLASK environment be set on "development" status:\n' +
          '   Terminal - Linux > export FLASK_ENV=development\n' +
          '        CMD - Windows > set FLASK_ENV=development\n' +
          '         PS - Windows > env:FLASK_ENV = "development"')
    print('3) Thus, visit the site: "http://127.0.0.1:5000" through the browser\n' +
          '   (or the site printed on your terminal) in order to reach the homepage.\n\n')
    bp.app.run()

    
