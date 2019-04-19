#!/usr/bin/env python3
# Author: ChengYi
# Mail: chengyi818@foxmail.cn
# created time: Fri 19 Apr 2019 10:36:03 AM CST

from pathlib import Path
from .repor import Repo
from .const import TEMPLATE_TOML, CONFIG_FILE_NAME
import datetime
import toml
import os
import json


class Configer(object):
    def __init__(self):
        self.home = str(Path.home())
        self.config_file = os.path.join(self.home, CONFIG_FILE_NAME)
        self.repos = []
        self.return_if_dirty = True

    def generate_config(self):
        if os.path.exists(self.config_file):
            print("config file: ", self.config_file, "already exists!")
            return

        file = open(self.config_file, 'w')
        file.write(TEMPLATE_TOML)
        file.close()
        print("generate_config in: ", self.config_file)

    def parse_config(self):
        parsed_toml = self.get_toml()
        if not parsed_toml:
            return False

        config_json = self.toml_to_json(parsed_toml)
        # print(config_json)

        config_dict = json.loads(config_json)
        # print(config_dict)
        self.return_if_dirty = config_dict['global']['return_if_dirty']

        for name in config_dict['repo']:
            local_path = config_dict['repo'][name]['local_path']
            repo = Repo(name, local_path)
            self.repos.append(repo)

        return True

    def toml_to_json(self, parsed_toml):
        # convert toml to json
        indent_json = 2
        separators = (',', ': ')
        json_data = json.dumps(parsed_toml,
                               default=json_serialize,
                               ensure_ascii=False,
                               indent=indent_json,
                               separators=separators,
                               sort_keys=True)
        return json_data

    def get_toml(self):
        if not os.path.exists(self.config_file):
            print("config file not exist, please run git996 init first!")
            return None

        with open(self.config_file, "r") as f:
            data = f.read()
            parsed_toml = toml.loads(data)
            # toml_string = toml.dumps(parsed_toml)
            # print(toml_string)

        return parsed_toml


def json_serialize(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("{0} is not JSON-serializable".format(repr(obj)))
