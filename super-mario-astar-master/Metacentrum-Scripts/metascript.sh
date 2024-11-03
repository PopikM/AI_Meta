#!/bin/bash

for ss in $(seq 1 1 10)
do
  for ttfw in $(seq -f "%0.2f" 0.2 0.2 2)
  do
    echo $ss $ttfw
    qsub -v searchSteps=$ss,timeToFinnishWeight=$ttfw script.sh
  done
done

for ttfw in $(seq -f "%0.2f" 0.2 0.2 2)
do
  echo 20 $ttfw
  qsub -v searchSteps=20,timeToFinnishWeight=$ttfw script.sh
done