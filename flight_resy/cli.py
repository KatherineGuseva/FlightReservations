"""This module provides the RP To-Do CLI."""
# flight_resy/cli.py

from typing import Optional

import typer

from flight_resy import __app_name__, __version__
from flight_resy import config
from flight_resy import booking

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return

@app.command()
def book(
        seat: str = typer.Option(
            None,
            "--seat",
            "-s",
            prompt="what's the seat?",
        ),
        number_of_seats: int = typer.Option(
            1,
            "--number_of_seats",
            "-n",
            prompt="how many seats would you liketo book?",
        ),
) -> None:
    database = config.init_app(config.get_prod_db)
    reserved_seats = booking.book(seat=seat, number_of_seats=number_of_seats, database=database)
    if reserved_seats is not None:
        config.commit_to_db(reserved_seats)

@app.command()
def cancel(
        seat: str = typer.Option(
            None,
            "--seat",
            "-s",
            prompt="what's the seat?",
        ),
        number_of_seats: int = typer.Option(
            1,
            "--number_of_seats",
            "-n",
            prompt="how many seats would you like to cancel?",
        ),
) -> None:
    database = config.init_app(config.get_prod_db)
    reserved_seats = booking.cancel(seat=seat, number_of_seats=number_of_seats, database=database)
    if reserved_seats is not None:
        config.commit_to_db(reserved_seats)