"""Tests for the story graph and command-line engine."""

from adventure import main
from story import SCENES


def test_every_choice_points_to_an_existing_scene():
    for scene in SCENES.values():
        for _, destination in scene["choices"].values():
            assert destination in SCENES


def test_every_scene_is_reachable_from_start():
    reached = set()
    pending = ["start"]

    while pending:
        scene_id = pending.pop()
        if scene_id in reached:
            continue
        reached.add(scene_id)
        pending.extend(destination for _, destination in SCENES[scene_id]["choices"].values())

    assert reached == set(SCENES)


def test_there_are_at_least_three_endings():
    endings = {scene["ending"] for scene in SCENES.values() if scene.get("ending")}
    assert {"good", "bad", "funny"} <= endings
    assert len(endings) >= 3


def test_bad_input_is_reprompted_with_scripted_input(capsys):
    answers = iter(["not a choice", "9", "1", "1", "1", "n"])

    main(input_fn=lambda _: next(answers))

    output = capsys.readouterr().out
    assert output.count("Please enter one of the numbered choices") == 2
    assert "GOOD ENDING" in output


def test_game_replays_on_request():
    answers = iter(["1", "1", "1", "y", "q"])

    main(input_fn=lambda _: next(answers))

