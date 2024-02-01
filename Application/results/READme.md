# TDA Mapping Framework Results
For the grid search, the following two ranges of values have been defined for Cover parameters, specifically _resolution_ and _gain_:
- _resolution_: [0.52, 0.54, 0.56, 0.58, 0.60, 0.62, 0.64, 0.66, 0.68]
- _gain_: [20, 25, 30, 35, 40, 45, 50, 55, 60]

Each of the four dimensionality reduction techniques underwent rigorous testing, with **Isomap** emerging as the most effective among them. Notably, for all four techniques, combinations of Cover parameters were identified that exhibited statistically significant differences between reference distance distributions and those of patients. However, **Isomap** displayed several combinations of Cover parameters that also yielded favorable post-hoc results, with significant distinctions observed across almost all four classes (HC, ROP, ROD, and CHR).

Here is an example of heatmaps result


