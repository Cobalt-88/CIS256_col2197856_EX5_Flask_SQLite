from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import DataRequired
from booksdb import BooksDB

# REMOVED all BooksDB() and .getauthors() calls  was causing crash
class SearchWTF(FlaskForm):
    myoptions = [(None, "Choose your Search Type"), ('byAuthor','By Author'),('byTitle','By Title'),('byPublisher','By Publisher')]
    search_choice = SelectField("SearchChoice", choices=myoptions, validators=[DataRequired()])

class ByAuthorIdWTF(FlaskForm):
    author_choice = SelectField("Select Author", coerce=int, validators=[DataRequired()])

class ByPublisherIdWTF(FlaskForm):
    publisher_choice = SelectField("Select Publisher", coerce=int, validators=[DataRequired()])

class ByTitleWTF(FlaskForm):
    title_search = StringField("Title Contains", validators=[DataRequired()])

