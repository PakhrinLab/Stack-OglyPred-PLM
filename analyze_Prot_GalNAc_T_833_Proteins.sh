#!/bin/bash
#SBATCH --array=1-833
#SBATCH --mem=200G
#SBATCH --cpus-per-task=18
module load TensorFlow/2.6.2-foss-2021a
source ~/virtualenvs/Dashain/bin/activate

BASEDIR=/homes/t326h379/Ieva_GalNAc_T

export FILENAME=$(ls ${BASEDIR}/*.fasta | sed -n ${SLURM_ARRAY_TASK_ID}p)
python ~/analyze_Prot_GalNAc_T_833_Proteins.py
