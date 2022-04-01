from flask import (
    Blueprint, render_template
)

views = Blueprint('views',__name__)

@views.route('/')
@views.route('/base.html')
def home():
    return render_template("base.html", title = "Keyboard Part Picker")

