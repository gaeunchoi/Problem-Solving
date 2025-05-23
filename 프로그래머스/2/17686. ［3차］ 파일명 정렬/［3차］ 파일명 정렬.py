import re

def solution(files):
    def parse_file(file):
        match = re.match(r"([^\d]+)(\d{1,5})", file)
        head, number = match.groups()
        return (head.lower(), int(number))
    return sorted(files, key = parse_file)