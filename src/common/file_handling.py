from typing import List

def file_to_list(path) -> List[str]:
    with open(path, 'r') as f:
        return f.read().splitlines()
