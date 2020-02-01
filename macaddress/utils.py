import re


def clamp(value, max_limit):
    return value % (max_limit+1)


def parse_hex(value):
    return int(''.join([x.group(0) for x in re.finditer(r'[\da-fA-F]', value.lower())]), base=16)
