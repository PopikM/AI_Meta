#!/bin/bash
#PBS -q default@cerit-pbs.cerit-sc.cz
#PBS -l walltime=20:00:00
#PBS -l select=1:ncpus=1:mem=4gb:scratch_local=1gb:spec=5.1:cluster=adan
#PBS -e /auto/vestec1-elixir/home/sosi123/job_logs
#PBS -o /auto/vestec1-elixir/home/sosi123/job_logs

DATADIR=/auto/vestec1-elixir/home/sosi123/repo/super-mario-astar
RESULTDIR=/auto/vestec1-elixir/home/sosi123/results/astarGrid
ROOT=/auto/vestec1-elixir/home/sosi123

NDW=0.00
TTFW=0.50
DFPT=2.00
DFPAP=3.00

echo "$PBS_JOBID is running on node `hostname -f` in a scratch directory $SCRATCHDIR" >> $DATADIR/jobs_info.txt

module add openjdk-17

# test if scratch directory is set
# if scratch directory is not set, issue error message and exit
test -n "$SCRATCHDIR" || { echo >&2 "Variable SCRATCHDIR is not set!"; exit 1; }

cp -R $DATADIR/Mario-AI-Framework $SCRATCHDIR || { echo >&2 "Error while copying input file(s)!"; exit 2; }

cd $SCRATCHDIR/Mario-AI-Framework

# compile and run Java
javac -cp src src/mff/agents/benchmark/AgentBenchmarkMetacentrum.java
java -cp src mff.agents.benchmark.AgentBenchmarkMetacentrum $NDW $TTFW $DFPT $DFPAP

# move output to data dir
mkdir -p $RESULTDIR
cp -a agent-benchmark/. $RESULTDIR/ || { echo >&2 "Error while copying output file(s) to result dir!"; exit 2; }

clean_scratch
