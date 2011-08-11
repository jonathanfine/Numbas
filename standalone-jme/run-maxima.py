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


def doit():
    
    # Create the input stream.
    tgt_filename = 'local/examples.maxima'
    lines = open('standalone-jme/examples.txt', 'rb')
    
    examples = list(filter_input(lines))
    pending = [
        'tex(%s);\n' % example
        for example in examples
        ]
    number_of_examples = len(pending)    
    pending.append('quit();\n')
    stdin = ''.join(pending)

    args = ['maxima']
    p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    stdout, stderr = p.communicate(stdin)
    p.wait()


    output_lines = stdout.split('\n')
    example_output = list(filter_output(output_lines))

    a, b = len(pending), len(example_output)
    assert a == b, ('length', a, b)

    return zip(examples, example_output)

if __name__ == '__main__':

    x = doit()
