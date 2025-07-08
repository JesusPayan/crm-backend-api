from flask import Blueprint, render_template, jsonify,request

from bd_config import db
from utils import validate_json
import utils
from logging import Logger

# Definir el Blueprint correctamente
bp = Blueprint('group', __name__, url_prefix='/group')

bp.route('/', methods=['POST'])
def add_group():
    print(request.get_json())
    data,code = utils.validate_json(request.get_json(),"group")       
