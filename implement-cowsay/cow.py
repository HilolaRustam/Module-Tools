import argparse
import cowsay

parser = argparse.ArgumentParser(
    description="Make animals say things")

parser.add_argument(
    "message", nargs="+", help="The message to say.")

parser.add_argument(
    "--animal",
    choices=cowsay.char_names,
    help="The animal to be saying things.")

args = parser.parse_args()

message = " ".join(args.message)

animal = args.animal or "cow"


say_func = getattr(cowsay, animal)
say_func(message)

