#!/usr/bin/env python
# coding: utf-8

import sys,os
IPYNB_FILENAME = 'Untitled.ipynb'
CONFIG_FILENAME = '.config_ipynb'

def main(argv):
    with open(CONFIG_FILENAME,'w') as f:
        f.write(' '.join(argv))
    os.system('jupyter nbconvert --execute {:s} --to html --TemplateExporter.exclude_input=True --ExecutePreprocessor.timeout=300'.format(IPYNB_FILENAME))
    return None

if __name__ == '__main__':
    main(sys.argv)

