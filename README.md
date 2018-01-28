# white-noise-toolkit
**Originally developed as a coding challenge for [UnifyID](https://unify.id)**

Random.org is an API that returns random numbers. Use these random numbers to create:
* An RGB bitmap picture of 128x128 pixels

## Setup
* Install Python 3.
* Install Pillow: `pip install pillow`
* Run app.py
* Once run, `image.png` will be saved in directory and image will be shown on screen

## Potential Issues/Bugs
* Proof of concept. Does not check for malicious inputs.
* Assumes that random.org will work. Will throw HTTPError otherwise.
