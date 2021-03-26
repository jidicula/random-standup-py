[![Build](https://github.com/jidicula/random-standup-py/actions/workflows/build.yml/badge.svg)](https://github.com/jidicula/random-standup-py/actions/workflows/build.yml) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![PyPI](https://img.shields.io/pypi/v/random-standup)](https://pypi.org/project/random-standup/)

# 🎲random-standup-py🐍
Do you have awkward pauses in your standups because no one wants to give their
update next? Why not have a defined order? To make it fair, why not also
🎲randomize🎲 that order!

You *really* should use [the Go version](https://pkg.go.dev/github.com/jidicula/random-standup) of this tool. This Python version was developed solely as a comparison exercise for the package publishing process.

### Do you find this useful?

Star this repo!

### Do you find this *really* useful?

You can sponsor me [here](https://github.com/sponsors/jidicula)!

## Usage

1. Get the tool with `pip install random-standup`.

2. Create a team roster in a TOML file, following the format in
`example-roster.toml`:
```toml
[Subteam-1]
members = [
        "Alice",                # TOML spec allows whitespace to break arrays
        "Bob",
        "Carol",
        "David"
        ]

["Subteam 2"]                   # Keys can have whitespace in quoted strings
members = ["Erin", "Frank", "Grace", "Heidi"]
```

3. `standup example-roster.toml`

## Output
```
$ standup example-roster.toml
2021-03-25
## Subteam-1
Alice
Bob
David
Carol

## Subteam 2
Erin
Grace
Frank
Heidi
```

## Building from `main`

1. Clone and `cd` into the repo.
2. Install [Poetry](https://python-poetry.org/docs/#installation).
3. `poetry install`
4. `poetry run standup example-roster.toml`

Run tests with `poetry run pytest -v`
