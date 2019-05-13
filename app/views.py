from flask import Blueprint, render_template, send_file, request
from app.shuffle import make_shuffled_datapack, get_versions

views = Blueprint('views', __name__)

@views.route('/')
def index():
  return render_template('pages/index.jinja', versions=get_versions())

@views.route('/download')
def download():
  v = request.args.get('v')
  file = make_shuffled_datapack(v)
  return send_file(file, attachment_filename='ShuffleCraft.zip', as_attachment=True, cache_timeout=0)
