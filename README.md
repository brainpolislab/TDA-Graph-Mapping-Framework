# TDA-Graph-Mapping-Framework
Topological Data Analysis (TDA) graphs represent a formidable mathematical framework for elucidating the intricate structure and relationships inherent in intricate datasets. Derived from principles in algebraic topology, TDA graphs possess a unique capacity to unveil nuanced patterns and features that may elude conventional data analysis methodologies, particularly in handling high-dimensional and noisy datasets.  

An interesting application involves the **mapping of new data samples within a pre-constructed TDA graph**. This mapping framework within TDA represents a noteworthy innovation, enabling the seamless integration of new data samples into pre-existing TDA graphs for the sophisticated analysis of complex datasets. This approach yields profound insights into the relationships, similarities, and disparities between newly introduced data and established topological structures. Particularly advantageous in scenarios necessitating a nuanced understanding of evolving data landscapes, the mapping framework enhances the adaptability of TDA graphs, rendering it a potent tool for applications such as pattern recognition, classification, and anomaly detection.  
In the context of **personalized medicine**, this innovative TDA application holds substantial promise, facilitating the integration of patient-specific data into TDA graphs for tailored health profiles. By discerning intricate patterns within high-dimensional patient data, this approach facilitates precise diagnostics and the formulation of personalized treatment strategies, contributing to more accurate disease profiling and revolutionizing personalized therapeutic interventions for optimized healthcare delivery.

---

## How the Mapping Framework works?
The Mapping Framework concentrates on the initial two steps of the Mapper algorithm: **Filtering** and **Covering**. The Filtering operation plays a pivotal role in the transformation of original data for topological analysis. It employs a filter (lens) function to project high-dimensional data points into a more compact representation, aligning with specific analysis objectives and data attributes. On the other hand, the Covering operation simplifies high-dimensional data by segmenting it into overlapping bins, each linked to a node in the TDA graph. This meticulous process, regulated by _resolution_ and _gain_ parameters, captures local structures, thereby augmenting the Mapper algorithm capability to comprehend intricate data topology.

### Pipeline
**a. TDA graph creation**  
Construct a TDA graph from an initial dataset of samples using the Mapper algorithm. Utilize various dimensionality reduction techniques to project the initial data into a lower-dimensional space, usually 2D. Keep each transformation for subsequent reuse, facilitating the projection of new samples into established spatial representation obtained through these techniques.

**b. Cover step analysis**  
After constructing the bidimensional space representation of the initial dataset, the Cover is established using the projected data. Consequently, bins are generated based on the _resolution_ and _gain_ parameters, which are defined at the outset and remain constant throughout the entirety of the mapping procedure.

**c. New sample projection**  
Upon having the Cover and filter transformations prepared, the final step involves projecting a new sample into the pre-constructed TDA graph. In this projection, the new sample undergoes transformation using the saved transformation from step (a) and is subsequently projected into the 2D space where the TDA graph is defined. Subsequently, three distinct outcomes emerge:

1. The new sample is accurately mapped inside at least one node of the TDA graph, signifying that the transformed new sample lies within a bin of the Cover that was transformed into a node following the Clustering (the final step of the Mapper algorithm).
  
2. The new sample is not mapped into any node of the pre-constructed TDA graph, indicating that the new sample does not fall within any bin of the Cover.

3. The new sample is mapped inside a "noisy" node, denoting nodes that were discarded during the creation of the TDA graph. These nodes correspond to bins containing only one sample, and in the Clustering step, they are deemed as noise.

![Mapping Framework scheme](/Images/mapping_framework.png)

