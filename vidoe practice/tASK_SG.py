import argparse
import configparser
import os
import pprint
import sys

CFG = {}

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", type=argparse.FileType(),
                        default="task1.ini", help="Config file")

    try:
        args = parser.parse_args()
        cfg = configparser.ConfigParser()
        cfg.read_file(args.config)

        file_conf = os.path.basename(args.config.name)
        file_env_var = file_conf.split(".")[0].upper()

        for section in cfg.sections():
            CFG[section] = {}

            for key, val in cfg.items(section):
                env_var = file_env_var + "_" + key.upper()

                if env_var in os.environ:
                    CFG[section][key] = os.environ.get(env_var)
                else:
                    CFG[section][key] = val

    except (argparse.ArgumentError, argparse.ArgumentTypeError) as x:
        sys.stderr.write(str(x))
        sys.exit(-1)

    pprint.pprint(CFG)
