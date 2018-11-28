# PyIS: Intro
not that the name means anything.

This is going to be a good for nothing yet nicely designed and implemented information system, primarily based on files rather that databases.


# Intended Design
I'm planning to have a loosely-coupled bunch of packages at the end or maybe I might consider building a framework. Again I strongly admit that it's not being developed to be useful in any manner, although it might prove the contrary (who knows?).

Intended components (or whatever they are called) are as follows:
## _Package_ Easy CLI:
A flexible CLI utility for my own apps

## _Package_ MockLib: 
A flexible library for mocking my own data models, somehow!

## _Package_ TinyIS:
A flexible framework for storing and retrieving python objects as data models with built-in data mapper and multiple data interfaces.

Currently JSON is the only format supported.

It's designed upon the MVC mindset. after being included, every project should contain these files:
* models.py
* logics.py
* interface.py (no idea!)
* config.py
* app.py (entrypoint)

## _App_ pyStudent:
A simple Student Information Management System built using aforementioned packages.



# Notice
This repo is actually a combination of 3 repos (the main repo, pystudent and menu_cli).
They might/might not work properly by their own, but they are not yet integrated.