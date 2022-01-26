# Load JSON content into memory.
# Use requests module to POST the json content to the endpoint
# https://jsonplaceholder.typicode.com/posts
# The response will be the data sent by you + an additional id field.
# Validate it against the proper schema created by you.
# If validation is OK, print OK, if not – print details on
# the validation failure
# Print duration of request (use request’s built-in
# features rather than time intervals)
# pycodestyle --first .\task2-5.py

import sys
import json
import requests
from pprint import pprint
from marshmallow import Schema, fields, validate, ValidationError, EXCLUDE

# The URL we are going to connect to
endpoint = "https://jsonplaceholder.typicode.com/posts"
# HTTP Header fields
header = {'Content-type': 'application/json'}
# Load data from .json
with open("task1.json", "r") as read_it:
    send_data = json.load(read_it)


# Schema created
class UserSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    body = fields.String(required=True)
    userId = fields.Integer(validate=validate.Range(min=1, max=99),
                            required=True)
    title = fields.String(required=True)


try:
    result = UserSchema().load(send_data)
    print("Validation: OK")
except ValidationError as err:
    print("Validation: FAIL")
    pprint(err.messages)


try:
    response = requests.post(endpoint, json=send_data, headers=header)
    if response.status_code not in (200, 201, 202):
        raise Exception("Non-successful HTTP request")

    # Post returns either error, or recorded data
    posted_data = json.loads(response.text)
    print(json.dumps(posted_data, indent=4, sort_keys=True))

    # Request Duration
    duration_req = response.elapsed.total_seconds()
    print(f"Duration of request is {duration_req} seconds")


except Exception as x:
    sys.stderr.write(str(x))
    sys.exit(2)
