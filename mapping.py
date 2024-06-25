import numpy as np

class MappingTDA():
    def __init__(self, data, projector, cover):
        self.data = projector.transform(data)
        self.cover = cover

    def mapping(self, sample):
        ''''
        Perform mapping of a new sample inside a pre-constructed TDA graph.

        Parameters:
        - sample: numpy array, the sample to be mapped inside the TDA graph.
        - verbose: bool, optional, flag to enable verbose mode for printing hypercube details. Default is False.

        Returns:
        - hypercubes_index: list, indices of hypercubes containing the sample.
        - hypercubes: list, hypercubes containing samples from the original dataset.
        - bins: list, centers of the hypercubes.

        This function applies the TDA mapping framework to a given new sample.
        It fits the Cover with the dataset and generates hypercubes based on the specified cover range.
        It then identifies the hypercubes containing the given sample and returns their indices along with the
        generated hypercubes and their centers.
        '''

        # Add index column to data
        idx = np.arange(self.data.shape[0])[:, np.newaxis]
        data = np.hstack((idx, self.data))

        # Fit cover and get cube centers
        bins = self.cover.fit(data)
        bins = [(sublist[0], sublist[1]) for sublist in bins]

        # Transform data into hypercubes
        hypercubes = self.cover.transform(data, bins)

        # Find indices of cubes containing the sample
        index_cubes = self.cover.find(sample)

        # Get indices of matching hypercubes
        hypercubes_index = []
        for index in index_cubes:
            cube = self.cover.transform_single(data, bins[index])

            for j in range(len(hypercubes)):
                if np.array_equal(cube, hypercubes[j]):
                    hypercubes_index.append(j)

        # Return indices, hypercubes, and centers
        return hypercubes_index, hypercubes, bins