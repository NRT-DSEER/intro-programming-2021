#!/bin/bash
#SBATCH --job-name=example_sbatch
#SBATCH --output=example_sbatch.out
#SBATCH --error=example_sbatch.err
#SBATCH --time=00:05:00
#SBATCH --partition=broadwl
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=14
#SBATCH --mem-per-cpu=2000

#we load python via anaconda first
module load python/anaconda-2020.02

#then we tell the computer to run our .py script
python3 ./lake_wanted_timeseries.py 'SU'