#!/usr/bin/env python

from flask_wtf import Form
from wtforms import SelectField
from wtforms.validators import DataRequired


class SearchForm(Form):
    '''SelectField options for searching for searching for a public event'''
