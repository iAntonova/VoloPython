# Load XML into a dict-alike structure.
# Process XML data and get a structure similar to target JSON.
#
# Before writing a JSON file, validate the content using marshmallow:
# name is mandatory, age must be in the range of 18-110.
#
# Each action must produce an info log message,
# in case of an error, we must get error messages,
#
# Command line arguments must define input xml,
# output json, log level (default is DEBUG),
# and log file (if not given, the log must go to the screen).

# Terminal: py 'app.py' -f hdata3.xml -o hdata4.json -d DEBUG -lf logfile.log


import argparse
import json
import logging
import pprint
import sys
import xmltodict

from marshmallow import Schema, fields, validate


class PersonSchema(Schema):
    name = fields.String(error_messages={"required": "Name required"},
                         required=True)
    age = fields.Integer(validate=validate.Range(min=18, max=110),
                         required=True,
                         error_messages={"required": "Age required"})


class ContentSchema(Schema):
    person = fields.Nested(PersonSchema, many=True)


class XMLSchema(Schema):
    content = fields.Nested(ContentSchema)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog=sys.argv[0])
    parser.add_argument("-f", "--file", type=argparse.FileType(),
                        help="Input XML file")
    parser.add_argument("-o", "--output", type=str, help="Output JSON file")
    parser.add_argument("-d", "--debug", type=str, help="Debug", default="DEBUG")
    parser.add_argument("-lf", "--logfile", type=str, help="Log file")
    try:
        args = parser.parse_args()
        log_format = '%(asctime)s: - %(levelname)s:%(message)s'
        logging.basicConfig(filename=f"{args.logfile}", format=log_format,
                            level=logging.getLevelName(f'{args.debug}'))
        if args.logfile is None:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(log_format)
            handler.setFormatter(formatter)
            logging.getLogger().addHandler(handler)

        with args.file:
            content = args.file.read()
            logging.info('XML file opened')
            my_dict = xmltodict.parse(content)
            logging.info('XML file parsed to dictionary')
        pprint.pprint(my_dict)
        result = XMLSchema().load(my_dict)
        logging.info('JSON validation passed')
        with open(args.output, "w") as output_file:
            json.dump(my_dict, output_file, indent=4)
            logging.info("Data saved to JSON file")
    except Exception as msg:
        logging.getLogger().addHandler(logging.StreamHandler(sys.stderr))
        logging.error(str(msg))
        sys.exit(-1)

    sys.exit(0)
