import math
import re


def clamp(value, max_limit):
    return value % (max_limit+1)


def parse_hex(value):
    return int(''.join([x.group(0) for x in re.finditer(r'[\da-fA-F]', value.lower())]), base=16)


def per_join(iterable, delimeter, step=1):
    return delimeter.join([''.join(iterable[step*i:step*i+step]) for i in range(math.ceil(len(iterable)/step))])
