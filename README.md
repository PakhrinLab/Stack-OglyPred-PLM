# Stack-OglyPred-PLM

## Abstract

O-linked glycosylation, an essential post-translational modification process in Homo sapiens, involves attaching sugar moieties to the oxygen atoms of serine and/or threonine residues. It significantly influences various biological and cellular functions. While threonine or serine residues within protein sequences are potential sites for O-linked glycosylation, not all serine and/or threonine residues undergo this modification, underscoring the importance of characterizing its occurrence. This study presents a novel approach for predicting intracellular and extracellular O-linked glycosylation events on proteins, crucial for comprehending cellular processes. Two base multi-layer perceptron models were trained by leveraging a stacked generalization framework. These base models respectively employ ProtT5 and Ankh O-linked glycosylation site-specific embeddings whose combined predictions trained the meta-model. Trained on extensive O-linked glycosylation datasets, the stacked-generalization model demonstrated high predictive performance on independent test datasets. Furthermore, the study emphasizes the distinction between nucleocytoplasmic and extracellular O-linked glycosylation, offering insights into their functional implications that were overlooked in previous studies. By integrating the protein language model’s embedding with stacked generalization techniques, this approach enhances predictive accuracy of O-linked glycosylation events and illuminates the intricate roles of O-linked glycosylation in proteomics, potentially accelerating the discovery of novel glycosylation sites.

<br>
<img max-width = 100% alt="image" src="https://github.com/PakhrinLab/Stack-OglyPred-PLM/blob/main/Stack-OglyPred-PLM.jpg">
The comprehensive framework for Stack-OglyPred-PLM
<br>
<br>

## Process To Reproduce NetOGlyc-4.0 Extracellular O-linked Glycosylation Results
Please download the below listed files and model from the publicly shared google drive (link provided) 
<br>
<br>
Again_Ankh_Feature_Extraction_667_Positive_OGalNAc.txt
<br>
Again_Ankh_Feature_Extraction_17817_Negative_OGalNAc.txt
<br>
One_hundred_Thirty_Seven_Training_Proteins_OGalNAc.txt
<br>
Positive_OGalNAc_ProtT5_Positive_Features_vectors_1837_Net_O_Glyc_4.txt
<br>
Negative_OGalNAc_ProtT5_Negative_Features_vectors_59414_Net_O_Glyc_4.txt
<br>
Seventenn_INdependent_Proteins_OGalNAc.txt
<br>
Extracellular_OGalNAc_Stacked_226294Model.h5
<br>

Place all the above files in a directory and execute it with the help of a python IDE to receive the reported results for NetOGlyc-4.0 extracellular datasets.


## Process To Reproduce dbPTM Nucleocytoplasmic Extracellular O-linked Glycosylation Results
Please download the below listed files and model from the publicly shared google drive (link provided) 
<br>
<br>
Ankh_Feature_5724_Positive_Taining_Site_Intracellular_from_1638_Proteins.txt
<br>
Ankh_Feature_232286_Negative_Taining_Site_Intracellular_from_1638_Proteins.txt
<br>
Nucleocytoplasmic_5724_with_1638_Proteins.csv
<br>
Nucleocytoplasmic_232286_with_1638_Proteins.csv
<br>
Ankh_Feature_1062_Positive_Independent_Testing_Site_Intracellular_from_183_Proteins.txt
<br>
Ankh_Feature_27031_Negative_Independent_Testing_Site_Intracellular_from_183_Proteins.txt
<br>
Nucleocytoplasmic_Independent_testing_Positive_1062_with_183_Proteins.csv
<br>
Nucleocytoplasmic_Independent_testing_Negative_27031_with_183_Proteins.csv
<br>
Model_Nucleus_and_Cytoplasm_Stacked_2687032Model.h5
<br>

Place all the above files in a directory and execute it with the help of a python IDE to receive the reported results for  dbPTM nucleocytoplasmic datasets.

## Process To Reproduce GalNAc-T Extracellular O-linked Glycosylation Results
Please download the below listed files and model from the publicly shared google drive (link provided) 
<br>
<br>
Ieva_OGalNAc_TProtT5_Positive_676_less_Features.txt
<br>
Ieva_OGalNAc_TProtT5_Negative_18392_less_Features.txt
<br>
One_Thirty_five_training_protein74828.txt
<br>
Fifteen_Testing_protein74828.txt
<br>
Ankh_Feature_Negative_OGalNAc_T_fasta_sites_18392.txt
<br>
Ankh_Feature_Positive_OGalNAc_T_sites_676_or_less.txt
<br>
Subash_taken_advice_from_IevaExtracellular_OGalNAc_T_Ieva_Stacked_2393728Model.h5
<br>

Place all the above files in a directory and execute it with the help of a python IDE to receive the reported results for GalNAc-T extracellular datasets.
<br>
<br>

## Environments Used
Python 3.10.4-TensorFlow-2.11.0
<br>
sklearn: 1.4.1.post1
<br>
Jupyter Notebook: 6.4.0
<br>
Numpy: 1.22.3
<br>
Pandas: 1.4.2

## Creating a ProtT5 File For A Protein
Use the following two files to generate ProtT5 embeddings for your desired protein sequence:
<br>
analyze_Prot_GalNAc_T_833_Proteins.py
<br>
analyze_Prot_GalNAc_T_833_Proteins.sh


## Creating a Ankh File For A Protein
Use the following two files to generate Ankh embeddings for your desired protein sequence:
<br>
analyze_ankh_OGalNAc_154.py
<br>
analyze_ankh_OGalNAc_154.sh

## Process To Extract "S/T" Embeddings From ProtT5 Protein File
Please use the following file to extract "S/T" embeddings from a ProtT5 file:
<br>
ProtT5_Feature_Vector_Creation_of_OGalNAc_Negative.ipynb
<br>

## Process To Extract "S/T" Embeddings From Ankh Protein File
Please use the following file to extract "S/T" embeddings from a Ankh file:
<br>
Ankh Feature Extraction Nucleocytoplasmic Negative Independent Testing.ipynb
<br>

## Datasets Availablity
All the training and independent test data are uploaded at the following Google Drive links:
https://drive.google.com/drive/folders/1x7oplkL7webstaSPZ-49ie7bl6FC-zkh?usp=sharing
<br>
https://drive.google.com/drive/folders/1US_ET64jcjb2HaBOPyry27d79QmDEGVN
<br>
https://drive.google.com/drive/folders/1sm4UpxB85iOJx5M7g-J3qvicmRCoccxh?usp=drive_link
<br>
https://drive.google.com/drive/folders/10w4IvzN5xz7YfyiqAumlgq9mEodYKYx4
<br>
https://drive.google.com/drive/folders/1MoEsfnoxpDQ6zxIbId2G6yMMsZq-hnSB
<br>
https://drive.google.com/drive/folders/1KlQTmliwIHaBZnY9MZj7aTGXe49Kv4oM
<br>
**If you need any help don't hesitate to get in touch with Dr. Subash Chandra Pakhrin (pakhrins@uhd.edu)**
