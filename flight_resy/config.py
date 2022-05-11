"""This module provides the RP To-Do config functionality."""
# flight_resy/config.py


from os.path import exists
import typer


CONFIG_FILE_PATH = "reserved_seats.txt"


def get_prod_db()->str:
    mat=[[0]*8]*20
    if not exists(CONFIG_FILE_PATH):
        with open(CONFIG_FILE_PATH,'w+') as f:
            for line in mat:
                f.write(' '.join([str(a) for a in line]) + '\n')
    with open(CONFIG_FILE_PATH,'r') as f:
        ret = [[int(num) for num in line.split(' ')] for line in f.readlines()]
    return ret

def commit_to_db(data: [])->None:
    with open(CONFIG_FILE_PATH,'w') as f:
        for line in data:
            f.write(' '.join([str(a) for a in line]) + '\n')
    typer.secho(f"SUCCESS", fg=typer.colors.GREEN)


def init_app(create_db ) -> str:
    """Initialize the application."""
    return create_db()

