#!/usr/bin/env python

from flask_wtf import Form
from wtforms import SelectField
from wtforms.validators import DataRequired

sample_cities = [
    ("nyc", "NYC"),
    ("philly", "Philadelphia"),
    ("rot", "Rotchester"),
    ("boston", "Boston"),
    ("la", "Los Angeles"),
    ("sf", "San Francisco")
]

sample_categories = [
    ("cs", "Computer Science"),
    ("math", "Mathematics"),
    ("bio", "Biology"),
    ("astro", "Astrology"),
    ("phys", "Physics"),
    ("chem", "Chemistry"),
    ("art", "Art"),
    ('linguistics', "Linguistics"),
    ('dance', "Dance")
]

class SearchForm(Form):
    '''SelectField options for searching for searching for a public event'''
    city     = SelectField('Choose a city', choices=sample_cities)
    category = SelectField('Choose a category', choices=sample_categories)
