#!/bin/sh

sbcl --control-stack-size 10000000 --load square.lisp
# ccl --load square.lisp
