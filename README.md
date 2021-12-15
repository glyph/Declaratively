# Declaratively

This is a Python module for encouraging certain things be executed
declaratively, at module-import time, so that those declarations are fixed
throughout the lifetime of a program and are not (for example) subject to
injection of untrusted data from a network or the user into a place that should
only contain fixed information specified by a programmer.

(At present the state of the code could charitably be described as
"experimental".)

You can read a little more about this here: https://glyph.twistedmatrix.com/2021/12/declaratively.html

I've set up this repository just as a sketch, to see if there is interest.  If you'd like to see a more productionized (i.e.: tested) version of this, please feel free to contribute!
