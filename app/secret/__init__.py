from flask import Blueprint

secret = Blueprint('secret', __name__)

from . import views
