# Mapping Framework Validation
The Mapping Framework has been developed and vallidated with consideration for fMRI data from specific subjects. However, it is adaptable and extendable to accomodate diverse types of datasets, contingent upon the rewuirements and scope of the study project.

### Dataset
The dataset included in this repository comprises information about 587 subjects. Each subject is characterized by fMRI feature data, specifically the connectivity matrix associated with Dosenbach's atlas (160x160 matrix). Furthermore, each subject is assigned a class label indicating the diagnosis. The distribution of diagnoses is as follows: 251 Healthy Control (HC) subjects, 119 Recent Onset Psychosis (ROP) subjects, 111 Recent Onset Depression (ROD) subjects, and 106 Clinical High-Risk (CHR) subjects.

---

## New sample mapping function (Python)
```python
def mapping_tda(data, sample, cover):
    # Add index column to data
    indices = np.arange(data.shape[0])[:, np.newaxis]
    data = np.hstack((indices, data))

    # Fit cover and get cube centers
    cube_centers = cover.fit(data)
    cube_centers = [(sublist[0], sublist[1]) for sublist in cube_centers]

    # Transform data into hypercubes
    hyper_cubes = cover.transform(data, cube_centers)

    # Find indices of cubes containing the sample
    index_cubes = cover.find(sample)

    # Get indices of matching hypercubes
    hyper_cubes_index = []
    for index in index_cubes:
        cube = cover.transform_single(data, cube_centers[index])

        for j in range(len(hyper_cubes)):
            if np.array_equal(cube, hyper_cubes[j]):
                hyper_cubes_index.append(j)

    # Print hypercubes with only one sample
    for k in hyper_cubes_index:
        if len(hyper_cubes[k]) == 1:
            print(f'Hyper cube {k} with only one sample')
        else:
            continue

    # Return indices, hypercubes, and centers
    return hyper_cubes_index, hyper_cubes, cube_centers
```




