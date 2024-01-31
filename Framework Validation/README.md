# Mapping Framework Validation
The Mapping Framework has been developed and validated with consideration for fsMRI data from specific subjects. However, it is adaptable and extendable to accomodate diverse types of datasets, contingent upon the requirements and scope of the study project.

### Dataset
The dataset included in this repository comprises information about 587 subjects. Each subject is characterized by _sMRI feature data_ associated with regional grey matter volume (GMV) from the anatomical ROIs of the Hammers atlas, which is defined as the quantity of grey matter located between the grey-white interface and the pia mater; _environmental characteristics_ including immigration status, scores on the everyday discrimination scale, and scores on the bullying scale; _fMRI features data_ associated to the functional connectivity matrix associated with the Dosenbach's atlas. Furthermore, each subject is assigned a class label indicating the diagnosis. The distribution of diagnoses is as follows: 251 Healthy Control (HC) subjects, 119 Recent Onset Psychosis (ROP) subjects, 111 Recent Onset Depression (ROD) subjects, and 106 Clinical High-Risk (CHR) subjects.

---
Four techniques for dimensionality reduction have been explored:
- **Principal Componenet Analysis (PCA)** [🔗](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
- **Kernel PCA** [🔗](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html)
- **Isomap** [🔗](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html)
- **Fast ICA** [🔗](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA)

To validate the framework, a TDA graph is constructed exclusively based on HC subjects. Subsequently, the framework is applied to remap each sample, and the accuracy of their mapping within the corresponding nodes of the pre-constructed TDA graph is assessed. The anticipated outcome is the correct mapping of each sample to its respective nodes, signifying the framework consistency and robustness.  

As evident from the notebook, it is observed that, for all four employed dimensionality reduction techniques, each sample has been accurately remapped to its corresponding nodes.





