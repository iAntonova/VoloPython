# Given a config file task1.ini
# Get the config file path from argparse and load configuration into dictionary
# If any of environment variables (TASK1_HOST, TASK1_PORT, TASK1_LOGIN)
# are defined, then they must override values of host, port,
# and login respectively
# Print resulting dictionary to the screen
# pycodestyle --first .\task2-4.py
# TASK1_HOST=127.0.0.1;TASK1_PORT=9090;TASK1_LOGIN=superadmin

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
