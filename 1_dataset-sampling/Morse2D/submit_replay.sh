#!/bin/bash
#SBATCH -J opt
#SBATCH --time=48:00:00
#SBATCH -n1
#SBATCH --job-name=2DMorse_PIMD_efficient_sampling_xxxTxxxK

ipi=~/source/i-pi-dev/bin/i-pi

export OMP_NUM_THREADS=1

rm /tmp/ipi_2DMorse_PIMD_efficient_sampling_xxxTxxxK

${ipi} input_replay.xml > log.i-pi &

sleep 30

for x in {1..1};
do
python run-ase.py &
done

wait

