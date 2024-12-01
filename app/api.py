import http.client

from flask import Flask

import sys
sys.path.append('./')



from app.util import convert_to_number
from app.calc import add_internal, substract_internal, multiply_internal, divide_internal, power_internal, check_types_internal, sqrt_internal, log_internal


# CALCULATOR = Calculator()
api_application = Flask(__name__)
api_application.config["DEBUG"] = True
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}


@api_application.route("/")
def hello():
    return "Hello from The Calculator!\n"


@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    try:
        num_1, num_2 = convert_to_number(op_1), convert_to_number(op_2)
        result = add_internal(num_1, num_2)  # Ejecuta la operación
        return f"{result}", http.client.OK
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/substract/<op_1>/<op_2>", methods=["GET"])
def substract(op_1, op_2):
    try:
        num_1, num_2 = convert_to_number(op_1), convert_to_number(op_2)
        return ("{}".format(substract_internal(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/multiply/<op_1>/<op_2>", methods=["GET"])
def multiply(op_1, op_2):
    try:
        num_1, num_2 = convert_to_number(op_1), convert_to_number(op_2)
        return ("{}".format(multiply_internal(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)
    except InvalidPermissions as e:
        return (str(e), http.client.FORBIDDEN, HEADERS)


@api_application.route("/calc/divide/<op_1>/<op_2>", methods=["GET"])
def divide(op_1, op_2):
    try:
        num_1, num_2 = convert_to_number(op_1), convert_to_number(op_2)
        return ("{}".format(divide_internal(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/power/<op_1>/<op_2>", methods=["GET"])
def power(op_1, op_2):
    try:
        num_1, num_2 = convert_to_number(op_1), convert_to_number(op_2)
        return ("{}".format(power_internal(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/sqrt/<op_1>", methods=["GET"])
def sqrt(op_1):
    try:
        num_1 = convert_to_number(op_1)
        return ("{}".format(sqrt_internal(num_1)), http.client.OK, HEADERS)
    except (TypeError, ValueError) as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/log/<op_1>", methods=["GET"])
def log(op_1):
    try:
        num_1 = convert_to_number(op_1)
        return ("{}".format(log_internal(num_1)), http.client.OK, HEADERS)
    except (TypeError, ValueError) as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


class InvalidPermissions(Exception):
    """Exception raised for invalid permissions."""
    pass


api_application.run()