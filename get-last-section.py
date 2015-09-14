#!/usr/bin/env python2.7
import sys
if len(sys.argv) > 1:
  split = sys.argv[1].split("/")
  if len(split) >= 1 and split[-1]:
    print split[-1]
  elif len(split) >= 2 and split[-2]:
    print split[-2]
  else:
    sys.stderr.write("Can't split that on slashes")
else:
    sys.stderr.write("Can't split nothing")
