Pumphandle
==========
A (very) work in progress collection of tools for computational and mathematical
Epidemiology.

Contents
--------
Utilities:

- "NetDrop": A simple function for downloading data files from web sources


Dependencies
------------
requests


Versions
--------
0.0.1 - Initial PyPi release version.
0.0.2 - Minor changes to NetDrop code.

Version Notes
-------------
0.0.1 - This release is intended primarily to make the developers life slightly
easier by packaging a commonly used function for repeated use. It's not a
general-purpose release, and unless you really hate writing very short bits of
requests code, it's likely not worth your trouble.

0.0.2 - As with version 0.0.1, but with some slightly more sophisticated
handling of what to do if a data file already exists, avoid accidental
overwrites or wasted bandwidth from pulling down redundantly huge files. Also
cleaned up code with Flake8.

Why 'Pumphandle'?
-----------------
The repository name is a reference to John Snow(1) and the Broad Street Pump

1: <http://en.wikipedia.org/wiki/John_Snow_(physician)>