#  py task2_1.py --file1 .\hdata1.json --file2 .\hdata2.json --output output.json
import argparse
import json
import sys

from marshmallow import Schema, fields, EXCLUDE
from deepdiff import DeepDiff


class PersonSchema(Schema):
    age = fields.Integer(required=True)
    name = fields.String(required=True)
    weight = fields.Integer(required=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog=sys.argv[0])

    parser.add_argument("--file1", type=argparse.FileType(), help="First file to load")
    parser.add_argument("--file2", type=argparse.FileType(), help="Second file to load")
    parser.add_argument("--output", type=str, help="Output file", default="output.json")
    
    try:
        args = parser.parse_args()
        
        with args.file1:
            data1 = json.load(args.file1)
        
        with args.file2:
            data2 = json.load(args.file2)

        for data in (data1, data2):
            PersonSchema().load(data, unknown=EXCLUDE)

        diff = DeepDiff(data1, data2, ignore_order=True)

        if diff:
            out_data = [data1, data2]
            with open(args.output, "w") as fp:
                json.dump(out_data, fp, indent=4)

    except Exception as x:
        sys.stderr.write(str(x) + "\n")
        sys.exit(-1)

    sys.exit(0)
