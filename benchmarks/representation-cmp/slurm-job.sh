#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=24:00:00
#SBATCH --job-name=llgp-rep-cmp
#SBATCH --mem=5G
#SBATCH --array=1-5

REPOROOT="$1"
OUTFOLDER="$2"
MATRIX_SIZE="$3"

cd $REPOROOT

# Warmup
benchmarks/inv-run.sh $MATRIX_SIZE
sleep 2
benchmarks/inv-run.sh $MATRIX_SIZE > $OUTFOLDER/inv-run-$SLURM_ARRAY_TASK_ID.txt
