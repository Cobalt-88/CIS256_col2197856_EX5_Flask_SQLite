from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import DataRequired
from booksdb import BooksDB

class SearchWTF(FlaskForm):
    myoptions = [(None, "Choose your Search Type"), ('byAuthor','By Author'),('byTitle','By Title'),
                 ('byPublisher','By Publisher')]
    search_choice = SelectField("SearchChoice", choices=myoptions,validators=[DataRequired()] )

class ByAuthorIdWTF(FlaskForm):
    mydb = BooksDB()
    authors = mydb.getauthors()
    author_choice = SelectField("AuthorChoice", choices=authors)


class ByPublisherIdWTF(FlaskForm):
    # This will become the dropdown menu of publishers
    publisher_choice = SelectField(
        "Select Publisher",
        coerce=int, # converts the value to integer publisher_id
        validators=[DataRequired()]
    )

class ByTitleWTF(FlaskForm):
    # Simple text box user types part of a title
    title_search = StringField(
        "Title Contains",  # label shown on the form
        validators=[DataRequired()]
    )

