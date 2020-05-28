#!/usr/bin/env python
# coding: utf-8

import sys
import os
IPYNB_FILENAME = 'regression.ipynb'
CONFIG_FILENAME = '.config_ipynb'


def run_notebook(argv, default_cell_timeout=300):
    with open(CONFIG_FILENAME, 'w') as f:
        f.write(' '.join(argv))

    os.system(
        'jupyter nbconvert --execute {:s} --to html --TemplateExporter.exclude_input=True --ExecutePreprocessor.timeout={}'.format(
            IPYNB_FILENAME,
            default_cell_timeout))

    return None


if __name__ == '__main__':
    run_notebook(sys.argv)
