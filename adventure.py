"""Command-line engine for the Hacktoberfest Forest adventure."""

from story import SCENES


def play(input_fn=input, output_fn=print):
    """Play once, returning when the player quits or reaches an ending."""
    scene_id = "start"

    while True:
        scene = SCENES[scene_id]
        output_fn(f"\n{scene['text']}")

        if scene.get("ending"):
            output_fn(f"\n{scene['ending'].upper()} ENDING")
            return scene["ending"]

        for number, (description, _) in scene["choices"].items():
            output_fn(f"{number}. {description}")

        while True:
            answer = input_fn("\nChoose an option (or q to quit): ").strip().lower()
            if answer == "q":
                output_fn("Thanks for playing!")
                return None
            if answer in scene["choices"]:
                scene_id = scene["choices"][answer][1]
                break
            output_fn("Please enter one of the numbered choices, or q to quit.")


def main(input_fn=input, output_fn=print):
    """Run the game, offering a replay after each completed adventure."""
    output_fn("=== Hacktoberfest Forest Adventure ===")

    while True:
        result = play(input_fn=input_fn, output_fn=output_fn)
        if result is None:
            return

        while True:
            answer = input_fn("\nPlay again? (y/n): ").strip().lower()
            if answer == "q" or answer == "n":
                output_fn("Thanks for playing!")
                return
            if answer == "y":
                break
            output_fn("Please enter y to replay, n to quit, or q to quit.")


if __name__ == "__main__":
    main()
