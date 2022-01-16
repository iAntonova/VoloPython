# Load these two json files, validate each of them against Marshmallow
# schema (name, age and weight are mandatory fields, all other fields,
# if any – must be excluded during loading. Compare two json objects.
# Filed order must be ignored. If they do not match, then create a
# third object, which will be a list of the first & the second objects
# and write it to the output json file.

# Terminal: pycodestyle --first app.py
#           py 'app.py' -f1 hdata1.json -f2 hdata2.json


import argparse
import json
import sys

from marshmallow import Schema, fields, EXCLUDE
from deepdiff import DeepDiff


class MySchema(Schema):
    class Meta:
        unknown = EXCLUDE

    age = fields.Integer(required=True)
    name = fields.String(required=True)
    weight = fields.Integer(required=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog=sys.argv[0],
                                     description="JSON validator")
    # A new trick: using FileType as argument
    parser.add_argument("-f1", "--file1", type=argparse.FileType(),
                        help="1-st JSON file to compare")
    parser.add_argument("-f2", "--file2", type=argparse.FileType(),
                        help="2-nd JSON file to compare")

    exit_code = 0

    try:
        args = parser.parse_args()

        # FileType() opens a file and returns a handle
        data1 = json.load(args.file1)
        data2 = json.load(args.file2)

        # Validating content against schema
        for data in (data1, data2):
            MySchema().load(data)

        # Comparing results with updated field excluded
        diff = DeepDiff(data1, data2, ignore_order=True)
        if diff:
            with open('output.json', "w") as of:
                json.dump([data1, data2], of)
                of.close()
        exit_code = 1

    except Exception as x:
        sys.stderr.write(str(x) + "\n")
        sys.exit(-1)

    sys.exit(exit_code)
