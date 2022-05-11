"""This module provides the RP To-Do config functionality."""
# flight_resy/config.py

import configparser
from pathlib import Path
from os.path import exists
import typer

from flight_resy import __app_name__

SEAT_CONV = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7
}

def book(seat, number_of_seats, database) -> None:
    """Initialize the application."""
    if database is None:
        typer.secho(f"ERROR", fg=typer.colors.RED)
        return

    reserved_seats = database

    try:
        seat_row = int(seat[1:])-1
    except:
        raise ValueError("The row number should be digit")

    if seat_row>20 or seat_row<0:
        raise ValueError("Wrong input, there are 20 rows")

    if seat[0:1] not in SEAT_CONV.keys():
        raise ValueError("Wrong input, seats are A-H")

    seat_col = SEAT_CONV[seat[0:1]]
    typer.secho(f'{reserved_seats}', fg=typer.colors.RED)
    if reserved_seats[seat_row][seat_col]==1:
        typer.secho(f"ERROR", fg=typer.colors.RED)
        raise ValueError("The seat is already booked")
    else:
        count = number_of_seats
        while count > 0:
            if reserved_seats[seat_row][seat_col]==0:
                reserved_seats[seat_row][seat_col]=1
                count-=1
                seat_col+=1
            else:
                typer.secho(f"ERROR", fg=typer.colors.RED)
                return
    return reserved_seats


def cancel(seat, number_of_seats, database) -> None:
    """Initialize the application."""
    if database is None:
        typer.secho(f"ERROR", fg=typer.colors.RED)
        return

    reserved_seats = database

    try:
        seat_row = int(seat[1:])-1
    except:
        raise ValueError("The row number should be digit")

    if seat_row>20 or seat_row<0:
        raise ValueError("Wrong input, there are 20 rows")

    if seat[0:1] not in SEAT_CONV.keys():
        raise ValueError("Wrong input, seats are A-H")

    seat_col = SEAT_CONV[seat[0:1]]
    if reserved_seats[seat_row][seat_col]==0:
        typer.secho(f"ERROR", fg=typer.colors.RED)
        raise ValueError("The seat is vacent")
    else:
        count = number_of_seats
        while count > 0:
            if reserved_seats[seat_row][seat_col]==1:
                reserved_seats[seat_row][seat_col]=0
                count-=1
                seat_col+=1
            else:
                typer.secho(f"ERROR", fg=typer.colors.RED)
                return

    return reserved_seats

