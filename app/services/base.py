from typing import Union
from http import HTTPStatus
from flask import jsonify, request

SUCCESSFUL_REQUEST = HTTPStatus.OK
BAD_REQUEST = HTTPStatus.BAD_REQUEST


def handle_response(data: Union[dict, list], error: str)-> tuple: 
  if error:
    response = {'error': error}
    status_code = BAD_REQUEST
  else:
    response = data
    status_code = SUCCESSFUL_REQUEST
  return jsonify(response), status_code


def create_entity(EntityController) -> tuple:
  data, error = EntityController.create(request.json)
  return handle_response(data, error)


def get_entity_by_id(EntityController, _id: int)-> tuple:
  data, error = EntityController.get_by_id(_id)
  return handle_response(data, error)


def update_entity(EntityController) -> tuple:
  data, error = EntityController.update(request.json)
  return handle_response(data, error)


def get_entity(EntityController)-> tuple:
  data, error = EntityController.get_all()
  return handle_response(data, error)
