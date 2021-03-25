"""Randomize your standup order.
"""

import click


@click.command()
@click.argument("roster")
def standup(roster):
    print(f"{roster}")
