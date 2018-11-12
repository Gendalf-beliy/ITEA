import json
import pickle
import csv


def importer(file):
    f = open(file, 'r')
    js = json.loads(f.read())
    print(js)

    # Write to file
    f2 = open('bytefile.txt', 'wb')
    pickle.dump(js, f2)
    f2.close()

    # Read from file
    f2 = open('bytefile.txt', 'rb')
    js = pickle.load(f2)
    f2.close()
    print(js)


importer('d://11.txt')


def greeting(name):
    pref = 'Hello, '

    def together(name):
        print(pref + name)
        return pref + name

    return together(name)

greeting('Sanyok')


def json_to_csv(file):
    f = open('new.json', 'w')
    dc = {}
    with open('1.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for i, row in enumerate(spamreader):
            dc[i] = max([int(x) for x in row])
    f.write(json.dumps(dc))
    f.close()

json_to_csv('1.csv')