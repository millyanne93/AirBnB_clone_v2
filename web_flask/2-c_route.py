#!/usr/bin/python3
""" A script that starts a Flask web application.
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """
    Route handler function for the root URL.
    Return a given string.
    """
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Route handler function for '/hbnb' URL.
    Returns a given string.
    """
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """
    Route handler function for '/c/<text>' URL.
    Display C followed by the value of the text variable
    """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
