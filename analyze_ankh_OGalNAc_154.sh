#!/bin/bash
#SBATCH --array=1-154
#SBATCH --mem=200G
#SBATCH --cpus-per-task=18
module load TensorFlow/2.3.1-foss-2019b-Python-3.7.4
source ~/virtualenv/ANKH/bin/activate

BASEDIR=/homes/t326h379/OGalNAc/Ankh_154_Proteins

export FILENAME=$(ls ${BASEDIR}/*.fasta | sed -n ${SLURM_ARRAY_TASK_ID}p)
python ~/analyze_ankh_OGalNAc_154.py