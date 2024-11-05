#!/bin/bash
#PBS -l walltime=2:00:00
#PBS -l select=1:ncpus=1:mem=4gb:scratch_local=1gb:spec=5.1:cluster=adan
#PBS -e /auto/brno2/home/popekmi/job_logs
#PBS -o /auto/brno2/home/popekmi/job_logs

DATADIR=/auto/brno2/home/popekmi/repo/super-mario-astar-master
RESULTDIR=/auto/brno2/home/popekmi/results/astarGrid
ROOT=/auto/brno2/home/popekmi

echo "$PBS_JOBID is running on node `hostname -f` in a scratch directory $SCRATCHDIR" >> $DATADIR/jobs_info.txt

module add openjdk-17

# test if scratch directory is set
# if scratch directory is not set, issue error message and exit
test -n "$SCRATCHDIR" || { echo >&2 "Variable SCRATCHDIR is not set!"; exit 1; }

cp -R $DATADIR/Mario-AI-Framework $SCRATCHDIR || { echo >&2 "Error while copying input file(s)!"; exit 2; }

cd $SCRATCHDIR/Mario-AI-Framework

# compile and run Java
javac -cp src src/mff/agents/benchmark/AgentBenchmarkMetacentrum.java
java -cp src mff.agents.benchmark.AgentBenchmarkMetacentrum 1 0 $DFPAP $DFPMP

# move output to data dir
mkdir -p $RESULTDIR
cp -a agent-benchmark/. $RESULTDIR/ || { echo >&2 "Error while copying output file(s) to result dir!"; exit 2; }

clean_scratch
