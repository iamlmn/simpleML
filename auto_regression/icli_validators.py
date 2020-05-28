
from PyInquirer import Validator, ValidationError
import os

class PhoneNumberValidator(Validator):
    def validate(self, document):
        ok = regex.match('^([01]{1})?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})\s?((?:#|ext\.?\s?|x\.?\s?){1}(?:\d+)?)?$', document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid phone number',
                cursor_position=len(document.text))  # Move cursor to end



class KfoldsValidator(Validator):
    def validate(self, document):
        try:
            if int(document.text)< 2:
                raise ValidationError(
                message='Requires minimum 2 folds, Enter number above 2',
                cursor_position=len(document.text))

        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))

            

class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end

class InputFilePathValidator(Validator):
    def validate(self, document):
        try:
            if not os.path.isfile(document.text):
            	raise ValidationError(
                message='File not present, enter a valid path',
                cursor_position=len(document.text))
            elif os.path.splitext(document.text)[-1] != '.csv':
                 raise ValidationError(
                    message='Invalid file type, provide CSV files only.',
                    cursor_position=len(document.text))
        except ValueError:
            raise ValidationError(
                message='Please enter a valid path as string',
                cursor_position=len(document.text))  # Move cursor to end


def get_column_names(setup_answers):
	import pandas as pd
	if setup_answers['demo_run'] == True:
		return []
	filepath = setup_answers['input_file']
	df = pd.read_csv(filepath)
	return list(df.columns)