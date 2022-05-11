from wtforms import ValidationError
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us about you.', validators=[DataRequired()])
  submit = SubmitField('Submit')


class AddPitch(FlaskForm):
  name = StringField('Pitch Name', validators=[DataRequired()])
  description = TextAreaField('Pitch Description', validators=[DataRequired()])
  category = SelectField(label="Pitch Category", choices=[(" ", "--Select an option-- "),('Pick Up Lines','Pick Up Lines'),('Applications','Applications'),('Business','Business'),('Designs','Designs'),('Interview', 'Interview'),('Product','Product')], validators=[DataRequired()])
  submit = SubmitField('Submit')

  
