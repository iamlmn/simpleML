#!/usr/bin/env python
# coding: utf-8

import sys
import os

CONFIG_FILENAME = '.config_ipynb'


def run_notebook(argv, ipynb_filename, default_cell_timeout=600, _ip = '0.0.0.0', _port = '8888'):
    os.system('pip install --upgrade prompt-toolkit') # temp fix for dockerization
    with open(CONFIG_FILENAME, 'w') as f:
        f.write(' '.join(argv))
    print("Starting {}".format(ipynb_filename))
    
    
    os.system(
        'jupyter nbconvert --execute {:s} --to html --TemplateExporter.exclude_input=True --ExecutePreprocessor.timeout={}'.format(
            ipynb_filename,
            default_cell_timeout))
    os.system('pip install prompt-toolkit==1.0.4') # temp fix for dockerization
    return None


if __name__ == '__main__':
    run_notebook(sys.argv)
