# TDA-Graph-Mapping-Framework
Topological Data Analysis (TDA) graphs represent a formidable mathematical tool for elucidating the intricate structure and relationships inherent in intricate datasets. Derived from principles in algebraic topology, TDA graphs possess a unique capacity to unveil nuanced patterns and features that may elude conventional data analysis methodologies, particularly in handling high-dimensional and noisy datasets.  

An interesting application involves the **mapping of new data samples within a pre-constructed TDA graph**. This mapping framework within TDA represents a noteworthy innovation, enabling the seamless integration of new data samples into pre-existing TDA graphs for the sophisticated analysis of complex datasets. This approach yields profound insights into the relationships, similarities, and disparities between newly introduced data and established topological structures. Particularly advantageous in scenarios necessitating a nuanced understanding of evolving data landscapes, the mapping framework enhances the adaptability of TDA graphs, rendering it a potent tool for applications such as pattern recognition, classification, and anomaly detection.  
In the context of **personalized medicine**, this innovative TDA application holds substantial promise, facilitating the integration of patient-specific data into TDA graphs for tailored health profiles. By discerning intricate patterns within high-dimensional patient data, this approach facilitates precise diagnostics and the formulation of personalized treatment strategies, contributing to more accurate disease profiling and revolutionizing personalized therapeutic interventions for optimized healthcare delivery.

---

## How the Mapping Framework works?
The Mapping Framework concentrates on the initial two steps of the Mapper algorithm: **Filtering** and **Covering**. The Filtering operation plays a pivotal role in the transformation of original data for topological analysis. It employs a filter (lens) function to project high-dimensional data points into a more compact representation, aligning with specific analysis objectives and data attributes. On the other hand, the Covering operation simplifies high-dimensional data by segmenting it into overlapping intervals (or hypercubes), each linked to a node in the TDA graph. This meticulous process, regulated by _n_cubes_ and _perc_overlap_ parameters, captures local structures, thereby augmenting the Mapper algorithm capability to comprehend intricate data topology.

### Pipeline
**a. TDA graph creation**  
Construct a TDA graph from an initial dataset of samples using the Mapper algorithm. Utilize various dimensionality reduction techniques to project the initial data into a lower-dimensional space, usually 2D. Keep each transformation for subsequent reuse, facilitating the projection of new samples into established spatial representation obtained through these techniques.

**b. Cover step analysis**  
After constructing the bidimensional space representation of the initial dataset, the Cover is established using the projected data. Consequently, hypercubes are generated based on the _n_cubes_ and _perc_overlap_ parameters, which are defined at the outset and remain constant throughout the entirety of the mapping procedure.

**c. New sample projection**  
Upon having the Cover and Filter transformations prepared, the final step involves projecting a new sample into the pre-constructed TDA graph. In this projection, the new sample undergoes transformation using the saved transformation from step (a) and is subsequently projected into the 2D space where the TDA graph is defined. Subsequently, three distinct outcomes emerge:

1. The new sample is accurately mapped inside at least one node of the TDA graph, signifying that the transformed new sample lies within a hypercube of the Cover that was transformed into a node following the Clustering (the final step of the Mapper algorithm).
  
2. The new sample is not mapped into any node of the pre-constructed TDA graph, indicating that the new sample does not fall within any hypercube of the Cover.

3. The new sample is mapped inside a "noisy" node, denoting nodes that were discarded during the creation of the TDA graph. These nodes correspond to bins containing a number of samples less than the _min_samples_ parameters of DBSCAN, and in the Clustering step, they are deemed as noise and then discarded.

![Mapping Framework scheme](/images/framework_scheme.pdf)

---

## New sample mapping function (Python)
The following Python function has been purposefully crafted to map new samples within the pre-constructed TDA graph.
```python
def mapping_tda(data, sample, cover):
    # Add index column to data
    idx = np.arange(data.shape[0])[:, np.newaxis]
    data = np.hstack((idx, data))

    # Fit cover and get cube centers
    bins = cover.fit(data)
    bins = [(sublist[0], sublist[1]) for sublist in bins]

    # Transform data into hypercubes
    hypercubes = cover.transform(data, bins)

    # Find indices of cubes containing the sample
    index_cubes = cover.find(sample)

    # Get indices of matching hypercubes
    hypercubes_index = []
    for index in index_cubes:
        cube = cover.transform_single(data, bins[index])

        for j in range(len(hypercubes)):
            if np.array_equal(cube, hypercubes[j]):
                hypercubes_index.append(j)

    # Print hypercubes with only one sample
    for k in hypercubes_index:
        if len(hypercubes[k]) == 1:
            print(f'Hyper cube {k} with only one sample')
        else:
            continue

    # Return indices, hypercubes, and centers
    return hypercubes_index, hypercubes, bins
```
The initial operation of the function involves fitting the Cover to determine the `bins`, denoting the bins within the bidimensional space generated following the Filtering step. Subsequently, leveraging these `bins`, the function generates the `hypercubes` that contain the input data, which are the initial data transformed during the Filtering step, considering one of the available dimensionality reduction techniques. These `hypercubes` subsequently serve as the nodes within the TDA graph.  
Following the identification of `hypercubes`, the subsequent step focuses on mapping a new sample within the bidimensional space defined by the variable `data`. This entails retrieving the index or indices corresponding to the `hypercubes` wherein the new sample has been mapped. Importantly, these indices align with the nodes of the preconstructed TDA graph, providing insights into the spatial location of the new sample post-mapping.  
Conclusively, the function also outputs information regarding wheter the new sample has been mapped within a `hypercubes` containing only a single sample. This specific categorization is significant, as `hypercubes` with a singular sample are considered indicative of noise within the dataset.

---

## Methods and Materials
The Mapping Framework has been developed leveraging [Kepler Mapper](https://kepler-mapper.scikit-tda.org/en/latest/), a software library that integrates the [Mapper](https://www.quantmetry.com/blog/topological-data-analysis-with-mapper/) algorithm within the Python programming language. Kepler Mapper is tailored for visualizing high-dimensional data and 3D point cloud data. It is equipped with capabilities to utilize cluster and scaling algorithms that seamlessly align with the Scikit-Learn API.
