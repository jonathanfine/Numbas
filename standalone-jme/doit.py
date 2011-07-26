'''
Assuming you've cloned the repository into clone-of-Numbas the
following should run the tests.

    clone-of-Numbas$ python standalone-jme/doit.py
    ok

It requires a command line JavaScript interpreter to be installed - I
use Mozilla's Rhino (which is implemented in Java).

You could also use JSDB:
    http://www.jsdb.org/

You'll also have to install PyYaml.
    http://pypi.python.org/pypi/PyYAML/

'''


import os
import subprocess
import yaml
import json

source_filenames = [
    'standalone-jme/stub-numbas.js',
    'runtime/scripts/math.js',
    'runtime/scripts/util.js',
    'runtime/scripts/jme.js',
    'runtime/scripts/jme-display.js',
]


def yaml_to_json():

    src = os.path.join('standalone-jme', 'test-data.yaml')
    tgt = os.path.join('local', 'test-data.json')

    data = yaml.load(open(src))
    json.dump(data, open(tgt, 'wb'), indent=4)


if __name__ == '__main__':

    if not os.path.isdir('local'):
        os.mkdir('local')

    yaml_to_json()

    # Create the composite file.
    tgt = open('local/expr-to-latex.js', 'wb')

    for filename in source_filenames:

        src = open(filename, 'rb')
        tgt.write(src.read())
        src.close()
    
    tgt.close()


    # Run the test script.
    args = 'js -f local/expr-to-latex.js -f standalone-jme/testit.js'.split()
    p = subprocess.Popen(args)
    p.wait()

