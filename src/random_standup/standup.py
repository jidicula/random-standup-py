"""Randomize your standup order.
"""

import click
from tomlkit import parse

import random
from datetime import date
from typing import List


@click.command()
@click.argument("rosterfile")
def standup(rosterfile):
    """random-standup is a tool for randomizing the order of team member
    updates in a standup meeting.
    """
    print(date.today())
    with open(rosterfile, "r") as f:
        roster = f.read()

    parsed_roster = parse(roster)
    subteams = parsed_roster.keys()

    [
        print_shuffled_list(parsed_roster[subteam]["members"], subteam)
        for subteam in list(subteams)[:-1]
    ]
    last_team = list(subteams)[-1]
    print_shuffled_list(parsed_roster[last_team]["members"], last_team, last=True)


def print_shuffled_list(
    team_members: List[str], team_name: str, last: bool = False
) -> None:
    """Accepts a team's member list and name and prints the team's name and
    randomized list of its members to stdout.
    """
    random.shuffle(team_members)
    print(f"## {team_name}")

    [print(name) for name in team_members]
    if not last:
        print()
