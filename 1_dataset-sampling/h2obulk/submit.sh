#!/bin/bash
#SBATCH -J opt
#SBATCH --time=336:00:00
#SBATCH -n 1 -N1
#SBATCH --mem="1024M"
#SBATCH --job-name=h2o-bulk_PIMD_efficient_sampling_xxxTxxxK

ipi=~/source/i-pi/bin/i-pi

export OMP_NUM_THREADS=1

touch /tmp/ipi_h2o-bulk_PIMD_efficient_sampling_xxxTxxxK
rm /tmp/ipi_h2o-bulk_PIMD_efficient_sampling_xxxTxxxK

# runs i-PI + driver to accumulate data

if [ -f "RESTART" ]; then
${ipi} RESTART > log.i-pi &
else
${ipi} input.xml > log.i-pi &
fi

sleep 30

for x in {1..1};
do
bash run-driver.sh &
done

wait


sleep 100

# runs i-PI in replay mode to recompute forces acting on the centroid

${ipi} input_replay.xml > log.i-pi-replay & 

sleep 30

for x in {1..1};
do
bash run-driver.sh &
done

wait
