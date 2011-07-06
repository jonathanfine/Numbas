'''Script to convert YAML test data files into JSON.
'''

import os
import yaml
import json

if __name__ == '__main__':

    src = os.path.join('standalone-jme', 'test-data.yaml')
    tgt = os.path.join('local', 'test-data.json')

    data = yaml.load(open(src))
    print data
    json.dump(data, open(tgt, 'wb'), indent=4)
