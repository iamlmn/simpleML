#!/usr/bin/env python
# coding: utf-8

import sys,os
IPYNB_FILENAME = 'testNb.ipynb'
CONFIG_FILENAME = '.config_ipynb'

def main(argv):
    with open(CONFIG_FILENAME,'w') as f:
        f.write(' '.join(argv))
    os.system('jupyter nbconvert --execute {:s} --to script --TemplateExporter.exclude_input=True'.format(IPYNB_FILENAME))
    return None

if __name__ == '__main__':
    main(sys.argv)

