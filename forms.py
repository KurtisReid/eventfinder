#!/usr/bin/env python

from flask_wtf import Form
from wtforms import SelectField
from wtforms.validators import DataRequired

sample_cities = [
    "NYC",
    "Philadelphia",
    "Rotchester",
    "Boston",
    "Los Angeles",
    "San Francisco"
]

sample_categories = [
    "Computer Science",
    "Mathematics",
    "Biology",
    "Astrology",
    "Physics",
    "Chemistry",
    "Art",
    "Linguistics",
    "Dance"
]

class SearchForm(Form):
    '''SelectField options for searching for searching for a public event'''
    city     = SelectField('Choose a city', choices=sample_cities)
    category = SelectField('Choose a category', choices=sample_categories)
