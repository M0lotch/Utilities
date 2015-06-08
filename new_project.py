import os, sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("new_path", help="Create new folder within the Python folder.", type=str)
args = parser.parse_args()

test_path = args.new_path

def make_directory(new_path):
	if not os.path.exists(new_path):
		os.makedirs(new_path)
		print("New file created!")
	else:
		print("OOPS! " + test_path +" already exists.")

make_directory(test_path)