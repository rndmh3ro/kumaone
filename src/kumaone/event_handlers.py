#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Event Handler module for kumaone"""

# Import builtin python libraries
from copy import deepcopy
import json
from pathlib import Path
import time
from types import SimpleNamespace

# Import external python libraries
from rich.console import Console
import socketio
from socketio.exceptions import TimeoutError


# Import custom (local) python packages
from .config import ConfigActions, check_config, create_config, delete_config, edit_config
from .settings import event_data, monitor_events
from .utils import app_info, log_manager

# Source code meta data
__author__ = "Dalwar Hossain"
__email__ = "dalwar23@pm.me"


def get_event_data(event):
    """
    Get event data

    :param event: (event) socketIO event
    :return: (dict) socketIO event data
    """

    timestamp = time.time()
    while event_data[event] is None:
        if time.time() - timestamp > 10:
            raise TimeoutError("Event response timed out.")
        if event_data[event] == {} and event in monitor_events:
            return []
        time.sleep(0.01)
    time.sleep(0.2)
    return deepcopy(event_data[event].copy())


def list_monitors_event(data):
    """
    Get all the monitors

    :return: (dict) socketIO event data
    """
    event_data["monitorList"] = data