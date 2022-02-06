#Machine Learning Analysis on Target Protiens for Drug Discovery

## 💭Background
Using code from *data professor Chanin Nantasenamt* that uses machine learning models for the target protien *acetylcholinesterase*, looking at pIC50 values. I will use this code to provide visual graphs for the data bioactivty analysis on a causal bioinformatics streamlit app so anyone can do bioinformatics on any target protien on their choice (involes cheminformatics). Includes further RNA and DNA analysis on the target protien (bioinformatics). 

## 🧬Information

**Remember, when choosing your target protien from the ChemBL database, it should ideally be a large dataset. The larger the dataset is, the better**
#### PART 1:
IC5O information:
- IC50 is the potency of the drug, in part 1, the standard_value part, the lower the number the more potency the drug becomes. Higher number, the worse the potency becomes. 
- (Standerd value should be as lower as possible)
- The inhibitory concentration at 50%, would have a low concentration 
--> (In order to licit 50% of the inibitors of a target protein you would need a lower concentration of the drug)
--> The higher the concentration is required, you require more of the drug in order to perform the same
- The bioactivity data is in the IC50 unit, compounds with 1000 nM (standerd_value) are active, etc, etc. Three classes: Inactive, active, intermediate
-->Active ingredient is the ingredient in a pharmaceutical drug that is bioloically active. 

#### PART 2:
Lipinski Descriptors:
- Christopher Lipinski, a scientist atPifzer, came up with a set of rule-of-thumb for evaluating the druglikeness of compounds.
- Druglikenessis based on Absorption, Ditribution, Metabolism, Excretion (Also known as the pharmacokinetic profile)
--> Lipinsky analyzed all orally active FDA-approved drugs in the formulation of what is to be known as the Rule of Five or Lipinski's Rule
Rules of LD:
- Molecular weight < 500 Dalton 
- Octanol-water partition coefficient (LogP) < 5
- Hydrogen bond donors < 5
- Hydrogen bond acceptors < 10

### 🛠️Work to be done
- Change the target proten to be different and test them out, cornavirus, etc (other target protiens, look at the chembl website search for target protien)
- For data anaylsis paper, you need images (both cor and hep) of the model predictions. Prediction vs Experimental pIC50 values. 
- RNA and DNA analysis
- Get genome from GenBank, convert and translate to identify and annotate functions for all the protiens encoded from the genome. (Needs more biology research)
- OpenMM molecular simulation of protien folding??

### 🏗️Resources:
- https://github.com/dataprofessor/bioinformatics_freecodecamp (dataprofessor acetylcholinesterase data)
- https://stackoverflow.com/questions/63427607/python-upload-files-directly-to-github-using-pygithub *uploading to github from google colab*
- https://github.com/geohot/corona *RNA sequence anaylsis? (unknown)*
