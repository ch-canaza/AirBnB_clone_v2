#!/usr/bin/python3
''' initializes a Flask web application  '''


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def root_slash_hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def root_slash_c(text):
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def root_slash_python(text="is cool"):
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def root_slash_number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def root_slash_number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    """function to execute when use get"""
    if (n % 2 == 0):
        return render_template('6-number_odd_or_even.html',
                               num=n, text='even')
    return render_template('6-number_odd_or_even.html',
                           num=n, text='odd')

if __name__ == "__main__":
    app.run()
