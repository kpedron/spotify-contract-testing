import json
from os.path import join, dirname
import time


def load_json_file(filename):
    absolute_path = join(dirname(__file__), filename)

    with open(absolute_path) as read_file:
        return json.loads(read_file.read())


def load_schema_file(schemaname):
    relative_path = join("..\\Schemas", schemaname)
    absolute_path = join(dirname(__file__), relative_path)

    with open(absolute_path) as read_file:
        return json.loads(read_file.read())


def update_json_file(filename, newinfo):
    absolute_path = join(dirname(__file__), filename)

    with open(absolute_path, 'w') as write_file:
        json.dump(newinfo, write_file, indent=2)


def check_timestamp_is_old(timestamp_refreshtoken):
    timestamp_now = time.time()
    if timestamp_refreshtoken < timestamp_now:
        return True
    elif timestamp_refreshtoken > timestamp_now:
        return False

    return True
