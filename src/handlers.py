""" Endpoint Callback Handlers """

import logging as log
import uuid
import json

from . import model

def greeter(name):
    """Greeter route callback"""
    return f"Hello {name}!"

def reserve(json_body):
    """Save reservation callback"""
    return model.save_reservation(json_body)

def get_reservations(flight_id):
    """"Get reservations callback"""
    return model.get_reservations(flight_id)