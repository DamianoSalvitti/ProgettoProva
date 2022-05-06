import sys
import os

# Reach the parent's path
f_path = os.path.dirname(__file__)
root_path = os.path.join(f_path, os.pardir)
sys.path.append(os.path.abspath(root_path))

# Import of the desired module
import src.compute_flask_cv.browser_page as bp

# Test
if __name__ == '__main__':

    # Module correctly imported
    print('"browser_page" imported correctly.')
    print('Start testing "browser_page.py"\n')

    # Instructions
    print('\nHELP')
    print(f'1) Let the local server be activated from the terminal to have access to the contents:\n' +
          f'   Terminal -  Linux  > export FLASK_APP={root_path}\src\compute_flask_cv\\browser_page.py\n' +
          f'        CMD - Windows > set FLASK_APP={root_path}\src\compute_flask_cv\\browser_page.py\n' +
          f'         PS - Windows > env:FLASK_APP = "{root_path}\src\compute_flask_cv\\browser_page.py"')
    print('2) Let the FLASK environment be set on "development" status:\n' +
          '   Terminal - Linux > export FLASK_ENV=development\n' +
          '        CMD - Windows > set FLASK_ENV=development\n' +
          '         PS - Windows > env:FLASK_ENV = "development"')
    print('3) Thus, visit the site: "http://127.0.0.1:5000" through the browser\n' +
          '   (or the site printed on your terminal) in order to reach the homepage.\n\n')
    bp.app.run()
    
    # Test
    from app import index

    def test_homepage():
        assert index() == "Hello world"

    
