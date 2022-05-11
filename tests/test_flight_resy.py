# tests/test_rptodo.py
import pytest

from typer.testing import CliRunner

from flight_resy import __app_name__, __version__, cli

runner = CliRunner()


def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout

def test_booking():
    result = runner.invoke(cli.app, ["book","--seat", "A2", "--number_of_seats", "1"],  input="\n")
    assert result.exit_code == 0

def test_cancelling():
    result = runner.invoke(cli.app, ["cancel","--seat", "A2", "--number_of_seats", "1"],  input="\n")
    assert result.exit_code == 0

def test_booking1():
    result = runner.invoke(cli.app, ["book","--seat", "A2", "--number_of_seats", "1"],  input="\n")
    assert result.exit_code == 0

def test_booking2():
    result = runner.invoke(cli.app, ["book","--seat", "A2", "--number_of_seats", "1"],  input="\n")
    assert result.exit_code == 1

def test_booking3():
    result = runner.invoke(cli.app, ["book","--seat", "U2", "--number_of_seats", "1"],  input="\n")
    assert result.exit_code == 1