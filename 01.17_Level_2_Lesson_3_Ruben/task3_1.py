#  py 'task3_1.py' -x hdata1.xml -j out.json -d -l logfile.log
import sys
import json
import argparse
import xmltodict
import logging

from marshmallow import Schema, fields, validate


class PersonSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True,
                         validate=validate.Range(min=1, max=110))


def x2d_postprocess(path, key, value):
    if key == 'age':
        value = int(value)
    return key, value


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--xml", type=argparse.FileType(), required=True)
    parser.add_argument("-j", "--json",
                        type=argparse.FileType(mode="w"), required=True)
    parser.add_argument("-d", "--debug", action="store_true", default=False)
    parser.add_argument("-l", "--logfile", type=str)

    has_logging = False

    try:
        args = parser.parse_args()
        log_level = logging.DEBUG if args.debug else logging.WARNING
        logging.basicConfig(filename=args.logfile,
                            format='%(asctime)s: %(levelname)s:%(message)s',
                            level=log_level)

        has_logging = True

        logging.info(f"Loading XML file {args.xml.name}")
        with args.xml:
            xml_content = xmltodict.parse(args.xml.read(),
                                          postprocessor=x2d_postprocess)
        logging.info("Reformatting XML content")

        xml_data = [dict(x) for x in xml_content["content"]["person"]]

        logging.info("Validating XML content")
        PersonSchema().load(xml_data, many=True)

        logging.info(f"Writing output to {args.json.name}")
        json.dump(xml_data, args.json, indent=4)

    except Exception as x:
        if has_logging:
            logging.error(str(x))
        else:
            sys.stderr.write(str(x))
        sys.exit(-1)
