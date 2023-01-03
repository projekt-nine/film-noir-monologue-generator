#!/usr/bin/env python3
import argparse
import os
import glob
import json
import random
import tracery
from tracery.modifiers import base_english


parser = argparse.ArgumentParser()
parser.add_argument(
    "-s", "--start",
    default="#fnm_start#",
    help="Start token")


def combine_grammars(path):
    files = get_grammars_json_files(path)
    combined = {}
    for file in files:
        d = read_json_file(file)
        for k, v in d.items():
            if k not in combined:
                combined[k] = v
            else:
                print(f"Duplicate key found in {file}: {key}")
    return combined


def get_grammars_json_files(path):
    """
    Return a list of json files containing grammars in the grammars folder
    """
    grammars_json = glob.glob(os.path.join(path, '*.json'))
    return grammars_json


def read_json_file(path):
    """
    Read an entire file in one go.
    """
    with open(path) as f:
        return json.load(f)


def make_tracery(rules):
    """
    Instantiate and configure Tracery
    """
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    return grammar


if __name__ == "__main__":
    args = parser.parse_args()
    json = combine_grammars('grammars')
    rendered_grammar = make_tracery(json).flatten(args.start)
    print(rendered_grammar)
