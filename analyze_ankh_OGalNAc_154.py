import os

basedir = "/homes/t326h379/OGalNAc/Ankh_154_Proteins"

os.chdir(basedir)

name=os.environ['FILENAME']

print()

print(name)

print()

from Bio import SeqIO
protein_sequences = []
for seq_record in SeqIO.parse(name,"fasta"):
    placeholder = seq_record.id
    placeholder = placeholder.split("|")[1]
    Sequence = str(seq_record.seq)
        
    protein_sequences.append(Sequence)
    
amino_acids_sequence = str(protein_sequences[0])
    
protein_sequences = [list(seq) for seq in protein_sequences]

import ankh
import torch

# To load large model:
model, tokenizer = ankh.load_large_model()
model.eval()


outputs = tokenizer.batch_encode_plus(protein_sequences, 
                                add_special_tokens=True, 
                                padding=True, 
                                is_split_into_words=True, 
                                return_tensors="pt")
with torch.no_grad():
    embeddings = model(input_ids=outputs['input_ids'], attention_mask=outputs['attention_mask'])
    
    
exact_embedding = embeddings[0][0][:-1]

filename = str(placeholder)+"_ANKH_"+".csv"
fp = open(filename,"a+")
for i in range(exact_embedding.shape[0]):
    features = str(exact_embedding[i].numpy().tolist())
    features = features.strip("[")
    features = features.strip("]")
    fp.write(amino_acids_sequence[i])
    fp.write(",")
    fp.write(features)
    fp.write("\n")
fp.close()    