from flask import Blueprint, render_template, send_file
from app.shuffle import make_shuffled_datapack

views = Blueprint('views', __name__)

@views.route('/')
def index():
  return render_template('pages/index.jinja')

@views.route('/download')
def download():
  file = make_shuffled_datapack()
  return send_file(file, attachment_filename='ShuffleCraft.zip', as_attachment=True, cache_timeout=-1)
