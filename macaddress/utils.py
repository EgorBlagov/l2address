import re
import math


def clamp(value, max_limit):
    return value % (max_limit+1)


def parse_hex(value):
    return int(''.join([x.group(0) for x in re.finditer(r'[\da-fA-F]', value.lower())]), base=16)


def per_join(_str, delimeter, step=1):
    return delimeter.join([_str[step*i:step*i+step] for i in range(math.ceil(len(_str)/step))])
