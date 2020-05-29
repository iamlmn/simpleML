
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import regex
import sys
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
from pyfiglet import Figlet
import yaml
import run_regression
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
    print(colored('Hi, configure your linear regression model!', 'green'))
    questions_modeling = [{
        'type': 'confirm',
        'name': 'StartModelling',
        'message': 'Start training job?',
        'default': True
    }, ]
    import regression_icli
    import default_values
    general_answers = prompt(regression_icli.general_questions, style=style)
    general_answers = dict(**default_values.default_general_answers, **general_answers)

    setup_answers = prompt(regression_icli.setup_questions, style=style)
    if setup_answers['custom_setup'] == False:
        setup_answers = dict(**default_values.default_setup_answers, **setup_answers)

    if general_answers['analysis_type'] == 'LinearRegression':
        regression_answers = prompt(
            regression_icli.regression_questions,
            style=style)
        modelling_answers = dict(**default_values.default_regression_answers, **regression_answers)
        _ipynb_filename = 'regression.ipynb'

    elif general_answers['analysis_type'] == 'BinaryClassification':
        classifications_answers = prompt(
            regression_icli.classifications_questions,
            style=style)
        modelling_answers = dict(**default_values.default_classification_answers, **classifications_answers)
        _ipynb_filename = 'Classification_dev.ipynb'

    
    # concaenate answers
    answers = {**general_answers, **setup_answers, **modelling_answers}
    if answers['view_config']:
        print(answers)

    with open('auto_config.yml', 'w') as outfile:
        yaml.dump(answers, outfile, default_flow_style=False)
    import os
    if os.path.isfile('auto_config.yml'):
        COCNFIG_PRESENT = 1
        print(colored('Configuration file created ...', 'blue'))
        answers_modeling = prompt(questions_modeling, style=style)
        # Start regression
        if answers_modeling['StartModelling']:
            try:
                run_regression.run_notebook(sys.argv, _ipynb_filename, default_cell_timeout = 600)
            except Exception as e:
                rasie(e)


        print(colored('Completed job...', 'green'))
        sys.exit(0)
    else:
        raise RuntimeError('Somethinng went wrong. Config file is not present')
