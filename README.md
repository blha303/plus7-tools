plus7-tools
===========

A collection of tools for retrieving data from Plus7. Possibly episodes, I couldn't say, never used this myself.

Using get-all-eps.sh
-----

Install ffmpeg, python 2.7 and pip from your package repository. If on Ubuntu 14.10 or earlier, do not install ffmpeg from the package repository, follow these instructions instead: [trac.ffmpeg.org](https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu)

* `git clone https://github.com/blha303/plus7-tools`
* `cd plus7-tools`
* `git submodule update --init`
* `pip install -r requirements.txt`
* `./get-all-eps.sh <slug>`, with slug being the bit from the show url after /plus7/. For example, the slug for Harry's Practice is harrys-practice.
