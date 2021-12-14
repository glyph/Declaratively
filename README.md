# Declaratively

This is a Python module for encouraging certain things be executed
declaratively, at module-import time, so that those declarations are fixed
throughout the lifetime of a program and are not (for example) subject to
injection of untrusted data from a network or the user into a place that should
only contain fixed information specified by a programmer.

(At present the state of the code could charitably be described as
"experimental".)
