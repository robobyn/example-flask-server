# Example Flask Server

This repo contains a sample REST-based Flask server that supports 3 routes:
* /hello
* /compute
* /date

The ```/hello``` route will return the string "Hello Mr {First Name} {Last Name}"
or "Hello Ms {First Name} {Last Name}" depending on gender, or simply
"Hello {First Name} {Last Name}" if no gender specified.  The route must be
formatted as follows:

```/hello?firstname={first name}&lastname={last name}&gender={m/f}```

The ```/compute``` route will return the result of a computation as a string.
Supported operations include "add", "subtract", "multiply", and "divide".
The route must be formatted as follows:

```/compute?num1={num1}&num2={num2}&operator={add/subtract/multiply/divide}```

The ```/date``` route will return the current local date in the form yyyy-mm-dd.
This route takes no parameters or arguments.

## Getting Started

Clone the GitHub repo for this example flask server:

```$git clone https://github.com/rhartung/example-flask-server.git```

Create and activate a virtual environment:

```
$virtualenv env
$source env/bin/activate
```

Pip install requirements
```$pip install -r requirements.txt```

Run tests.py to ensure all components working properly
```$python tests.py```

Start the server
```$python server.py```

Run in browser using localhost:5000/{desired route}

## Prerequisites

Program written in Python 2.7.  Please see requirements.txt for a full list of
requirements.

## Running the tests

From the command line:
```
$python tests.py
```

## Built With

* [Flask](http://flask.pocoo.org/docs/0.12/) - The web framework used