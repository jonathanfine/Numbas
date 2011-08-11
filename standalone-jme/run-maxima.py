"""
Generate maxima output using new file run-maxima.py.
"""

import subprocess

def doit():
    
    tgt_filename = 'local/examples.maxima'

    lines = open('standalone-jme/examples.txt', 'rb')
    tmp = open(tgt_filename, 'wb')

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line[0] == '#':
            continue

        tmp.write('tex(%s);\n' % line)
    tmp.close()

    args = ['maxima', '-b', tgt_filename]
    args = ['maxima', 'batch-b', tgt_filename]
    args = ['maxima']

    p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    stdout, stderr = p.communicate(open(tgt_filename).read() + 'quit();\n')
    p.wait()

    print stdout


if __name__ == '__main__':

    doit()
