#!/usr/bin/env python
# coding: utf-8

import sys,os
IPYNB_FILENAME = 'regression.ipynb'
CONFIG_FILENAME = '.config_ipynb'

def run_notebook(argv):
    with open(CONFIG_FILENAME,'w') as f:
        f.write(' '.join(argv))

    os.system('jupyter nbconvert --execute {:s} --to html --TemplateExporter.exclude_input=True --ExecutePreprocessor.timeout=300'.format(IPYNB_FILENAME))

    return None

if __name__ == '__main__':
    run_notebook(sys.argv)

