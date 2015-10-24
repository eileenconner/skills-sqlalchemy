"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.

brandeight = Brand.query.filter(Brand.id == 8).all()

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

modellist = Model.query.filter(Model.name == "Corvette", Model.brand_name == "Chevrolet").all()

# Get all models that are older than 1960.

over1960 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

after1920 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

cor = Model.query.filter(Model.name.like("Cor%")).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.

post1903 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()
# Python appears to want "is None" or similar, but if I run that in interactive mode the result is an empty list. ??

# Get all brands with that are either discontinued or founded before 1950.

discorfounded = Brand.query.filter((Brand.founded < 1950) | (Brand.discontinued == None)).all()
# This works for the first two items and then errors out.
# "UnicodeEncodeError: 'ascii' codec can't encode character u'\xeb' in position 22: ordinal not in range(128)"
# Is the umlaut in Citroen the issue?

# Get any model whose brand_name is not Chevrolet.

notchev = Model.query.filter(Model.brand_name != "Chevrolet").all()
# I did this with both "!=" and "<>" and got the same output
# Again there's a unicode error: ??
# "UnicodeEncodeError: 'ascii' codec can't encode character u'\xeb' in position 28: ordinal not in range(128)"

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    pass


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    pass

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
