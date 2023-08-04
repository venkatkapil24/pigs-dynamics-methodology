#!/bin/bash
#SBATCH -J opt
#SBATCH --time=48:00:00
#SBATCH -n4
#SBATCH --job-name=2DMorse_PIMD_efficient_sampling_xxxTxxxK

ipi=~/source/i-pi-dev/bin/i-pi

export OMP_NUM_THREADS=1

rm /tmp/ipi_2DMorse_PIMD_efficient_sampling_xxxTxxxK

if [ -f "RESTART" ]; then
${ipi} RESTART > log.i-pi &
else
${ipi} input.xml > log.i-pi &
fi

sleep 30

for x in {1..4};
do
python run-ase.py &
done

wait

