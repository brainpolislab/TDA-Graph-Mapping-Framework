# Mapping Framework Application
Following validation, the mapping framework has been implemented in a real-world scenario. The objective was to integrate the mapping framework into the realm of personalised medicine, thereby augmenting the diagnosis and treatment of psychiatric disorders.  
The dataset comprises a total of 587 subjects categorized into the following diagnostic classes: Healthy Control (HC), Recent Onset Psychosis (ROP), Recent Onset Depression (ROD), and Clinical High Risk (CHR). Each subject is linked with environmental characteristics, structural magnetic resonance imaging features (sMRI), and functional magnetic resonance imaging features (fMRI).  

For each feature set, a normative TDA graph has been systematically constructed, utilizing data exclusively from HC subjects. Subsequently, the barycenter of the graph has been determined as follows: the centroid for each node within the TDA graph has been computed, and then the barycenter has been calculated employing a weighted mean. Specifically, each centroid in the calculation has been weighted by the numerosity of the corresponding node, representing the total count of subjects contained within that node.  
Following the construction of the normative graph, the subsequent phase entailed the computation of distances between the centroid of each node within the graph and the previously calculated barycenter. This distribution of distances will serve as a reference for subsequent analyses.

```python
def get_barycenter(hypercubes):
    hypercubes_coordinates = {}
    for i, cube in enumerate(hypercubes):
        points = cube[:, 1:]
        points_center = np.mean(points, axis=0)
        hypercubes_coordinates[i] = [points_center, len(points)]

    sum_x = 0
    sum_y = 0
    total_points = 0

    # Compute weighted barycenter
    for point in hypercubes_coordinates.values():
        coordinates, weight = point
        x, y = coordinates
        sum_x += x * weight
        sum_y += y * weight
        total_points += weight

    barycenter = [sum_x / total_points, sum_y / total_points]

    return barycenter
```

With the distribution of distances at hand, the application proceeds with the subsequent mapping of patient samples into the normative TDA graph. The patient sample may (a) be accurately mapped inside a node of the graph, (b) remain unmapped within any node of the graph, or (c) be mapped within those "noisy" nodes. Notably, owing to the TDA algorithm, it is conceivable for a patient to be mapped inside more than one node of the normative graph. In such instances, the centroid of each mapped node is computed, considering also the patient, and subsequently, the distance from the barycenter is calculated for each node. Finally, these distances are averaged.  
Alternatively, in situations where a patient is not associated with any node of the graph, it is regarded independently, and subsequently, the distance between the patient and the barycenter is computed. Furthermore, in cases involving "noisy" nodes, distances are not computed, and the patient is treated as an outlier.

A schematic representation of the pipeline described above is presented below:
![Mapping Framework application](/Images/framework_application.png)


**N.B.** It is important to note that even if a new patient has been correctly mapped inside some nodes of the normative TDA graph, it may occur that among those nodes, some are indeed nodes of the graph while others are identified as "noisy" nodes. In such cases, only the "actual" nodes are considered when computing the distance with the barycenter, with the assumption that "noisy" nodes are akin to outliers.

Given the sensitivity of TDA graphs to Cover parameters, a grid search has been employed to determine suitable configurations of parameters (namely _resolution_ and _gain_). Accordingly, two distinct ranges of values for _resolution_ and _gain_ have been defined. For each combination of these parameters, the above pipeline has been executed. Subsequently, the distance distributions corresponding to each combination of Cover parameters were recorded.  
These distances were subjected to subsequent statistical analysis, aimed at identifying parameter configurations that enable the establishment of four independent distance distributions.

---

## Results analysis
After gathering all distance distributions for each feature set, categorized by diagnostic class (Reference HC, ROP, ROD, and CHR), statistical tests were conducted, specifically the Kruskal-Wallis test, to determine whether there exists any significant statistical difference between the HC reference distance distribution and those of the patients. Two distinct assessments were conducted for this purpose:

1. _HC vs others_: In this scenario, all patient distance distributions were concatenated and compared with the reference distance distribution.
2. _HC vs ROP vs ROD vs CHR_: In this scenario, each distance distribution was considered individually.
