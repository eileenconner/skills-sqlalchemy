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

brand_eight = Brand.query.filter(Brand.id == 8).all()

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

model_list = Model.query.filter(Model.name == "Corvette", Model.brand_name == "Chevrolet").all()

# Get all models that are older than 1960.

over_1960 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

after_1920 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

cor = Model.query.filter(Model.name.like("Cor%")).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.

post_1903 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()
# Python appears to want "is None" or similar, but if I run that in interactive mode the result is an empty list. ??

# Get all brands with that are either discontinued or founded before 1950.

disc_or_founded = Brand.query.filter((Brand.founded < 1950) | (Brand.discontinued == None)).all()
# This works for the first two items and then errors out.
# "UnicodeEncodeError: 'ascii' codec can't encode character u'\xeb' in position 22: ordinal not in range(128)"
# Is the umlaut in Citroen the issue? E w/ an umlaut is 'xeb', according to Google.

# Get any model whose brand_name is not Chevrolet.

not_chev = Model.query.filter(Model.brand_name != "Chevrolet").all()
# I did this with both "!=" and "<>" and got the same output
# Again there's a unicode error: ??
# "UnicodeEncodeError: 'ascii' codec can't encode character u'\xeb' in position 28: ordinal not in range(128)"

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_info = db.session.query(Model.name,
                                  Model.brand_name,
                                  Brand.headquarters).filter(Model.year == year).join(Brand).all()

    # How can I format this better?

    print model_info


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands_summary = db.session.query(Model.brand_name, Model.name).group_by(Model.name).all()

    print brands_summary

    # at first I did this, which gives the same output:
    # brands_summary = db.session.query(Brand.name, Model.name).group_by(Model.name).filter(Model.brand_name == Brand.name).all()
    # but it's more complicated than it needs to be because all the info is actually in the Models table
    # in sqlite I did this: SELECT brand_name, name FROM Models GROUP BY name;
    # Am I misreading the question?

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    """Returns list of objects that are brands whose name contains or == input string"""

    object_list = db.session.query(Brand.name).filter((Brand.name.like("%mystr%")) | (Brand.name == mystr)).all()

    print object_list

    # there is definitely something wrong here


def get_models_between(start_year, end_year):
    """returns a list of objects that are models with years that fall between the start year and end year"""
    models_between = db.session.query(Model.name).filter(Model.year > start_year, Model.year < end_year).all()

    print models_between

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# (is this what you mean by "returned value"?
# It's what I get when I print the assigned variable)

# returned value:

# SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded
# AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued AS brands_discontinued
# FROM brands
# WHERE brands.name = :name_1

# type: <class 'flask_sqlalchemy.BaseQuery'>


# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# I think an association table is a small table created specifically to provide a
# means by which two other tables can join.
# It would contain the standard primary key/foreign key relationship with each of
# those two other tables.
# In Python it definitely contains the relationship/backref pairs we've been writing,
# establishing keywords by means of which we can query the related tables.
# Then it would almost act as a structured join between the two. It would allow
# multiple joins and more complex queries.
