#!/bin/sh
mkcollection -c posClaps.mf -l 1 /Users/Maxime/Documents/University/2015/Cmput466/Project/Workbench/phase2/Clap/Pos
mkcollection -c negClaps.mf -l 0 /Users/Maxime/Documents/University/2015/Cmput466/Project/Workbench/phase2/Clap/Neg
cat posClaps.mf negClaps.mf > claps.mf
bextract -sv claps.mf -w claps.arff
