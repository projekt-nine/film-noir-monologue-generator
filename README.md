# Film Noir Monologue Generator

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

## Examples

> So there I was. I had just checked in with a friend who was over at Danny-O's and ordered a cup of cold coffee. So
> in slides Specialist MacSporran - looking for me as usual. Turns out Analyst MacNidder got snubbed. It looked like
> a set-up; they were attacked from several angles. The business happened within the past 24 hours. I briefly glanced
> out the window, then loaded my pistol. The rounds found their way home with a satisfying click.

----

> It was a bad week in a bad month; maybe even a bad year.  The Times were calling it the worst crime spike the city
> had ever seen. I had just strolled into Lenny's and ordered the saddest French onion soup I've ever seen. So in
> rushes Elda Red Eye - looking for me as usual. Turns out Enea the Worm got disappeared. A Columbian neck-tie. The
> incident went down last Thursday.  I jotted down the details and got ready for a grisly new case.

----

> It was a dark day in the big city.  Normal for this time of year, but something felt darker today... something more
> sinister. I had just cruised into Hank's and ordered a vodka lime. So in stumbles Goro the Claw - looking for me as
> usual. Turns out Father McNaas got axed. They managed to fight back - a bloody trail led all the way down the
> hall. Got a call about something similar just yesterday. "Sounds like the Hood murders," I thought out loud, grabbing my
> .22.


