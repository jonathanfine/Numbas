'''
Assuming you've cloned the repository into clone-of-Numbas the
following should run the tests.

    clone-of-Numbas$ python standalone-jme/doit.py
    ok

You'll have to install PyYaml.
    http://pypi.python.org/pypi/PyYAML/
    
You'll need the Rhino command line JavaScript interpreter to be installed
(which is implemented in Java).  Ubuntu's prompt suggests Rhino when you 
type 'js' at the command line.

On Windows you'll need Java (of course).  Install Rhino by placing js.jar
in the clone-of-Numbas folder.

I've found that JSDB fails.  The most recent version with
     error while loading shared libraries: libstdc++-6.dll: cannot open shared object file:
     
With version 1.7.3.6  of JSDB I get a runtime error (which might be due 
to Rhino and JSDB interpreting JavaScript differently).
    $ ./jsdb.exe local/expr-to-latex.js
    local\expr-to-latex.js:1837     TypeError: functions[x].concat is not a function
    Execution error in local\expr-to-latex.js.
'''


import sys
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


def yaml_to_json(names):

    for name in names:
        src = os.path.join('standalone-jme', 'tests',name+'.yaml')
        tgt = os.path.join('local', 'tests',name+'.json')

    data = yaml.load(open(src))
    json.dump(data, open(tgt, 'w'), indent=4)


if __name__ == '__main__':

    if not os.path.isdir('local'):
        os.mkdir('local')
        if not os.path.isdir(os.path.join('local','tests')):
            os.mkdir(os.path.join('local','tests'))

    yaml_to_json(['expr-to-latex'])

    # Create the composite file.
    tgt = open('local/expr-to-latex.js', 'wb')

    for filename in source_filenames:

        src = open(filename, 'rb')
        tgt.write(src.read())
        src.close()
    
    tgt.close()


    # Run the test script.
    args = 'js -modules local -modules standalone-jme -main standalone-jme/testit.js'.split()
    # Special case Windows batch file.
    if sys.platform == 'win32':
        args[0] = 'js.bat'
    p = subprocess.Popen(args)
    p.wait()

