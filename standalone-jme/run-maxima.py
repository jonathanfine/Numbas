"""
Generate maxima output using new file run-maxima.py.
"""

import subprocess

def filter_input(lines):

    for line in lines:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        yield line


def filter_output(lines):

    for line in lines:
        if line.startswith('(%i'):

            # This is a bit yucky and obscure.
            bits = line.split(None, 1)
            if len(bits) == 1:
                yield ''
            else:
                yield bits[1]
        else:
            continue


def doit(lines):

    # Create the input stream.
    pending = [
        'tex(%s);\n' % line
        for line in lines
        ]
    pending.append('quit();\n')
    stdin = ''.join(pending)

    args = ['maxima']
    p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    stdout, stderr = p.communicate(stdin)
    p.wait()

    output_lines = stdout.split('\n')
    return list(filter_output(output_lines))[:-1] # Discard the quit() line.


if __name__ == '__main__':

    lines = open('standalone-jme/examples.txt', 'rb')
    lines = list(filter_input(lines))

    x = doit(lines)

    assert len(x) == len(lines), (len(x), len(lines))
