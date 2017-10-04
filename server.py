"""Simple REST based Flask server to handle the following requests:

'/hello?firstname={first name}&lastname={last name}&gender={m/f}' will respond
with 'Hello Mr/Ms {First Name}{Last Name} depending on gender.

'/compute?num1={num1}&num2={num2}&operator={add/subtract/multiply/divide}' will
respond with the result of the computation of 2 nums based on specified
operator type

'/date' will respond with the current date in form 'yyyy-mm-dd'"""

import datetime
import operator

from flask import Flask, request

app = Flask(__name__)


@app.route("/hello")
def say_hello():
    """Responds to GET request from hello route with Hello Mr/Ms fname lname."""

    # retrieve first name, last name, gender from url parameters
    fname = request.args.get("firstname")
    lname = request.args.get("lastname")
    gender = request.args.get("gender")

    if gender == "m":
        return "Hello Mr {} {}".format(fname.capitalize(), lname.capitalize())

    elif gender == "f":
        return "Hello Ms {} {}".format(fname.capitalize(), lname.capitalize())

    # in case gender non-binary or not specified
    else:
        return "Hello {} {}".format(fname.capitalize(), lname.capitalize())


@app.route("/compute")
def compute():
    """Responds to GET request from compute route with result comp of 2 nums."""

    # retrieve num1, num2, and operation from url params
    # convert string nums to float - ensures correct result when dividing nums
    # if integer division desired use int() instead of float()
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    requested_operation = request.args.get("operation")

    # dictionary maps operator string to operator function
    ops = {"add": operator.add, "subtract": operator.sub,
           "multiply": operator.mul, "divide": operator.div}

    # try/except used for error handling in case of invalid parameter input
    try:
        return str(ops[requested_operation](num1, num2))

    except:
        return "Invalid operation, please check url parameters."


@app.route("/date")
def get_date():
    """Responds to GET request from date route with date in yyyy-mm-dd form."""

    # use datetime module to retrieve today's date
    return str(datetime.date.today())


if __name__ == "__main__":

    app.run(port=5000, host="0.0.0.0")
