from typing import List

def file_to_list(path) -> List[str]:
    with open(path, 'r') as f:
        return f.read().splitlines()

def file_to_int_list(path, separator=",") -> List[int]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
        return [int(number) for number in lines[0].split(separator)]
