#!/bin/bash
#SBATCH -J opt
#SBATCH --time=24:00:00
#SBATCH -N 1
#SBATCH --job-name=test_h2o-molecule_PICGS_xxxTxxxK_xxxtxxx

source ~/.bashrc
conda activate py3

ipi=~/source/i-pi/bin/i-pi

export OMP_NUM_THREADS=1

rm /tmp/ipi_h2o-molecule_PICGS_xxxTxxx_xxxtxxx*

${ipi} input.xml > log.i-pi & 

sleep 30

for x in {1..1};
do
bash rundriver.sh &
~/bin/lmp_mpi < in.lmp > /dev/null &
done

wait
