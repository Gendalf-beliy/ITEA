import json
import os
import time


def monitor(read_dir, res_dir, err_dir):
    file = '11'
    if os._exists(read_dir):
        s = process(file)


def process(file):
    lst = []
    try:
        with open(file, 'r') as f:
            lst = json.loads(f.read())
    except:
        # move file to err_dir
        pass
    return sum(lst)


if __name__ == '__main__':
    while True:
        monitor('1', '2', '3')
        time.sleep(5)
