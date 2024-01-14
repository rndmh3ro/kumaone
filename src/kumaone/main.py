#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main module for kumaone"""

# Import builtin python libraries

# Import external python libraries
from rich.console import Console
from typing_extensions import Annotated
import typer

# Import custom (local) python packages
from . import config_cli
from . import monitor_cli
from . import notification_cli
from . import status_page_cli
from .utils import app_info

# Source code meta data
__author__ = "Dalwar Hossain"
__email__ = "dalwar23@pm.me"

# Create typer app and turn off debug mode by default
app = typer.Typer()
app.add_typer(monitor_cli.app, name="monitor")
app.add_typer(config_cli.app, name="config")
app.add_typer(status_page_cli.app, name="status-page")
app.add_typer(notification_cli.app, name="notification")
state = {"log_level": "NOTSET"}
console = Console()


@app.command(name="info", help="Show information about kumaone application.")
def info(log_level: Annotated[str, typer.Option(help="Set log level.")] = "NOTSET"):
    """
    Show application information

    :return: (None) Information on screen.
    """

    if log_level:
        state["log_level"] = log_level
    app_info(log_level=log_level)


@app.callback()
def mission_control(log_level: Annotated[str, typer.Option(help="Set log level.")] = "NOTSET"):
    """
    Mission control for kumaone, an uptime kuma helper python package.
    """

    if log_level:
        state["log_level"] = log_level


if __name__ == "__main__":
    app()
