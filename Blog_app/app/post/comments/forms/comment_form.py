from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class CommentPostForm(FlaskForm):
    body = CKEditorField(validators=[DataRequired()])
    submit = SubmitField("Submit Comment")