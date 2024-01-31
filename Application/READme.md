# Mapping Framework Application
Following validation, the mapping framework has been implemented in a real-world scenario. The objective was to integrate the mapping framework into the realm of personalised medicine, thereby augmenting the diagnosis and treatment of psychiatric disorders.  
The dataset comprises a total of 587 subjects categorized into the following diagnostic classes: Healthy Control (HC), Recent Onset Psychosis (ROP), Recent Onset Depression (ROD), and Clinical High Risk (CHR). Each subject is linked with environmental characteristics, structural magnetic resonance imaging features (sMRI), and functional magnetic resonance imaging features (fMRI).  

For each feature set, a normative TDA graph has been systematically constructed, utilizing data exclusively from HC subjects. Subsequently, the barycenter of the graph has been determined as follows: the centroid for each node within the TDA graph has been computed, and then the barycenter has been calculated employing a weighted mean. Specifically, each centroid in the calculation has been weighted by the numerosity of the corresponding node, representing the total count of subjects contained within that node.  
Following the construction of the normative graph, the subsequent phase entailed the computation of distances between the centroid of each node within the graph and the previously calculated barycenter. This distribution of distances will serve as a reference for subsequent analyses.

![Mapping Framework application](/Images/framework_application.png)
