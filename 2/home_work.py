import json
import os

def monitor(read_dir, result_dir, error_dir):
    for file in read_dir:
        f = open(file, 'r')
        try:
            res = process(f.read())
            new = open(result_dir + f.name, 'w')
            new.write(res)
            new.close(0)
        except:
            pass   # move to error_dir
        finally:
            f.close()
            f



def process(list_string):
    """
    Reading string and return sum of list's elements
    :param list in string format:
    :return: number (sum of list's elements)
    """
    return sum(json.loads(list_string))


def find_txt(read_dir):
    return read_dir + 'list of pathes to txt files'

