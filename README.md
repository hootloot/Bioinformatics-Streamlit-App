# Machine Learning Analysis on Target Protiens for Drug Discovery

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

#### PART 4:
The regression model will allow us to predict the pIC50 value which is the degree at which a molecule can inhibit or not inhibit the target protein of interest (if it can inhibit with potently then it can be a good drug candidate. Afterwards, they will need to be subjected to further scrutiny such as their pharmacokinetic profiles (ADMET properties encompassing the properties of molecules pertaining to Absorption, Distribution, Metabolism, Excretion and Toxicity).

The scatter plot between experimental and predicted pIC50 will allow us to visually see the correlation between the 2 variables. Ideally, a perfect prediction with 100% Accuracy would show all data points to fall on the trend line. In a practical setting, the residuals or errors (taking the predicted values and subtracting it from the experimental or actual values give us the residual or error values) would cause data points to fall either above or below the trend line (essentially the variance).

A good molecule would have a very high pIC50 value (normally higher than 6 is considered to be good). It should be noted that "good" in this context refers to strong inhibition of the target protein of interest. In a practical setting, a good molecule in addition to strong inhibition of the target protein of interest it should also possess favorable 
"pharmacokinetic profiles" (the various molecular properties pertaining to the absorption, distribution, metabolism, excretion and toxicity of a drug). Thus, ideally, a ideal drug would have strong inhibition and good pharmacokinetic profiles. In practice, this is essentially an optimization problem and it is rather challenging to find such a molecule. Thus, in the real world setting, we have drugs that are potent but also lead to side effects in patients.
--> pIC50 values are inversely proportional to the IC50 values thus high IC50 (corresponding to low pIC50) values are favorable bioactivity for inhibiting the target protein. Toxicity is another parameter that can be evaluated separately.

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
