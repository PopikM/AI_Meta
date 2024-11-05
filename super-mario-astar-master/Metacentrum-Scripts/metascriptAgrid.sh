#!/bin/bash

for dfpap  in $(seq 0 1 10)
do
  for dfpmp  in $(seq -f "%0.2f" 0 0.25 3)
  do
    echo $dfpap $dfpmp
    qsub -v DFPAP=$dfpap,DFPMP=$dfpmp scriptAgrid.sh
  done
done