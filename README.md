# Hacktoberfest Forest Adventure

A small command-line choose-your-own-adventure game written in Python 3 using
only the standard library. You are a lost hiker trying to escape a forest
during Hacktoberfest week.

## Play

From the project directory, run:

```bash
python3 adventure.py
```

Choose a numbered option when prompted. Enter `q` at any choice or replay
prompt to quit. After an ending, enter `y` to play again or `n` to quit.

## Tests

Install pytest if needed, then run:

```bash
python3 -m pytest
```

The story is kept separately in `story.py`; the command-line engine is in
`adventure.py`.

## How it was built

Built with GitHub Copilot CLI for MLH Global Hack Week: Hacktoberfest 2026. Copilot wrote the story data, the game loop and the tests from a single prompt. I then ran the test suite and played through every ending by hand to check it.
