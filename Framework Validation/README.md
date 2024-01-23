# Mapping Framework Validation
The Mapping Framework has been developed and vallidated with consideration for fMRI data from specific subjects. However, it is adaptable and extendable to accomodate diverse types of datasets, contingent upon the requirements and scope of the study project.

### Dataset
The dataset included in this repository comprises information about 587 subjects. Each subject is characterized by fMRI feature data, specifically the connectivity matrix associated with Dosenbach's atlas (160x160 matrix). Furthermore, each subject is assigned a class label indicating the diagnosis. The distribution of diagnoses is as follows: 251 Healthy Control (HC) subjects, 119 Recent Onset Psychosis (ROP) subjects, 111 Recent Onset Depression (ROD) subjects, and 106 Clinical High-Risk (CHR) subjects.

---
Three techniques for dimensionality reduction have been explored:
- **Principal Componenet Analysis (PCA)** [🔗](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
- **Kernel PCA** [🔗](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html)
- **Isomap** [🔗](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html)

To validate the framework, a TDA graph is constructed exclusively based on HC subjects. Subsequently, the framework is applied to remap each sample, and the accuracy of their mapping within the corresponding nodes of the pre-constructed TDA graph is assessed. The anticipated outcome is the correct mapping of each sample to its respective nodes, signifying the framework consistency and robustness.






