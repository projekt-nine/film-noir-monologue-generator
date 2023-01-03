# Film Noir Generator

A quick-and-dirty project to demonstrate how to use [Tracery](https://github.com/galaxykate/tracery)
and [Pytracery](https://github.com/aparrish/pytracery) to procedurally generate Film Noir monologues.

(Most of the film noir text originally from [scadding/MyUniverse](https://github.com/scadding/MyUniverse).)

## How to use it

First, clone the repo:

```
git clone git@github.com:projekt-nine/film-noir-monologues.git
cd film-noir-monologues
```

Now make a virtual environment and install dependencies:

```
python -m virtualenv -p python3.9 .virtualenv
source .virtualenv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Now run:

```
python run.py
```

This will print a Film Noir monologues to the console.

## Why this repo

This repo demonstrates a few useful things:

* How to make a one-off procedural generator repository using Pytracery and a few JSON files
* How to keep multiple independent grammars in separate files, but combine into one grammar for generation
* How to do non-trivial procedural generation with nested templates
