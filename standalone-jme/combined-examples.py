'''Combine the inputs and outputs into a single file.'''

import json


def iter_file(filename):

    f = open(filename)
    for line in f:
        
        if line.endswith('\n'):
            line = line[:-1]
        yield line
    f.close()


def iter_numbas(filename):

    f = open(filename)
    data = json.loads(f.read())
    for d in data:

        value = d.get('value')
        if value is None:
            value = d.get('error')
        if value is None:
            value = 'None (look into this).'
        yield value


def doit():

    max_out = iter_file('local/max-out.txt')
    max_in = iter_file('local/max-in.txt')
    numbas_out = iter_numbas('local/numbas-out.json')

    return zip(max_in, numbas_out, max_out)


if __name__ == '__main__':

    triples = doit()
    f = open('standalone-jme/combined.txt', 'wb')

    for item in triples:
        f.write('%s\n%s\n%s\n\n' % item)

    f.close()
