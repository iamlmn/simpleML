"""
Usage:
    main.py -it [--configspec=<path--yaml-config-file>] [--default_cell_timeout=<time in second>]
    main.py -h|--help
    main.py -v|--version
Options:
    -h --help  Show this screen.
    -v --version  Show version.
    --yamlspec path of yaml file referring to indepth analysis report and plot control
    --default_cell_timeout: Default cell time out for executing in jupyter notebook 
"""

# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import regex
import sys
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
from pyfiglet import Figlet
from docopt import docopt
import yaml
import run_analysis
from termcolor import colored
f = Figlet(font='slant')
print(f.renderText('SimpleML'))

# f = Figlet(font='goofy', width =20)
# print(f.renderText('Linear Regression'))

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Allelysis 1.0')
    if arguments['-it']:
        if '--default_cell_timeout' in arguments:
            _default_cell_timeout = arguments['--default_cell_timeout']
        else:
            _default_cell_timeout = 600
        print(colored('Hi, configure your linear regression model!', 'green'))
        questions_modeling = [{
            'type': 'confirm',
            'name': 'StartModelling',
            'message': 'Start training job?',
            'default': True
        }, ]
        import icli_questions
        import default_values
        general_answers = prompt(icli_questions.general_questions, style=style)
        general_answers = dict(**default_values.default_general_answers, **general_answers)

        setup_answers = prompt(icli_questions.setup_questions, style=style)
        if setup_answers['custom_setup'] == False:
            setup_answers = dict(**default_values.default_setup_answers, **setup_answers)

        if general_answers['analysis_type'] == 'LinearRegression':
            regression_answers = prompt(
                icli_questions.regression_questions,
                style=style)
            modelling_answers = dict(**default_values.default_regression_answers, **regression_answers)
            _ipynb_filename = 'regression/regression.ipynb'
            _config_path = 'regression/regression_config.yml'

        elif general_answers['analysis_type'] == 'BinaryClassification':
            classifications_answers = prompt(
                icli_questions.classifications_questions,
                style=style)
            modelling_answers = dict(**default_values.default_classification_answers, **classifications_answers)
            _ipynb_filename = 'classification/Classification_dev.ipynb'
            _config_path = 'classification/classification_config.yml'
        
        # concaenate answers
        answers = {**general_answers, **setup_answers, **modelling_answers}
        if answers['view_config']:
            print(answers)

        with open(_config_path, 'w') as outfile:
            yaml.dump(answers, outfile, default_flow_style=False)
        import os
        if os.path.isfile(_config_path):
            COCNFIG_PRESENT = 1
            print(colored('Configuration file created ...', 'blue'))
            answers_modeling = prompt(questions_modeling, style=style)
            # Start regression
            if answers_modeling['StartModelling']:
                try:
                    run_analysis.run_notebook(sys.argv, _ipynb_filename, default_cell_timeout = _default_cell_timeout)
                except Exception as e:
                    rasie(e)
            print(colored('Completed job...', 'green'))
            sys.exit(0)
        else:
            raise RuntimeError('Somethinng went wrong. Config file is not present')
    else:
        raise RuntimeError('Arguments currently not supported')