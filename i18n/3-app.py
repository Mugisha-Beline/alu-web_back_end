#!/usr/bin/env python3
"""
Module for trying out Babel i18n with Flask.

This module demonstrates the implementation of internationalization (i18n) 
and localization in a Flask web application using the Flask-Babel extension.

Dependencies:
- Flask: Web framework for building the application.
- Flask-Babel: Extension for adding i18n and l10n support to Flask.

Usage:
1. Install the required dependencies: Flask, Flask-Babel.
2. Run the script to start the Flask web server.

Note: This script assumes the presence of a 'templates' folder containing
      HTML templates for rendering.
"""

from flask_babel import Babel, _
from flask import Flask, render_template, request, flash


# Initialize Flask app and Flask-Babel extension
app = Flask(__name__, template_folder='templates')
babel = Babel(app)


# Configuration class for Flask-Babel
class Config(object):
    """ Configuration Class for Babel """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Apply the configuration to the app
app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """Render a Basic Template for Babel Implementation.

    This route renders a simple HTML template using Flask's render_template
    function. The HTML template may include translated strings marked with
    the underscore (_) function provided by Flask-Babel.

    Returns:
        str: Rendered HTML template.
    """
    return render_template("3-index.html")


@babel.localeselector
def get_locale() -> str:
    """Select a language translation to use for that request.

    This function is a locale selector for Flask-Babel. It determines the
    language to be used for translation based on the client's preferences.

    Returns:
        str: Selected language code.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()

