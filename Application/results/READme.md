# TDA Mapping Framework Results
For the grid search, the following two ranges of values have been defined for Cover parameters, specifically _resolution_ and _gain_:
- _resolution_: [0.52, 0.54, 0.56, 0.58, 0.60, 0.62, 0.64, 0.66, 0.68]
- _gain_: [20, 25, 30, 35, 40, 45, 50, 55, 60]

Each of the four dimensionality reduction techniques underwent rigorous testing, with **Isomap** emerging as the most effective among them. Notably, for all four techniques, combinations of Cover parameters were identified that exhibited statistically significant differences between reference distance distributions and those of patients. However, **Isomap** displayed several combinations of Cover parameters that also yielded favorable post-hoc results, with significant distinctions observed across almost all four classes (HC, ROP, ROD, and CHR).

Below is an illustration of the heatmap results subsequent to the grid search, aimed at identifying the most suitable combination of Cover parameters, specifically concerning _structural magnetic resonance imaging_ (sMRI) features. This analysis has been conducted for the remaining sets of features as well, namely _environmental characteristics_ and _functional magnetic resonance imaging_ (fMRI):

<img src='/Images/isomap_smri.png' width='550'>

For each combination of Cover parameters, the heatmaps reports the resulting _p-value_ from the Kruskal-Wallis test on the four distance distributions from the normative TDA graph barycenter (HC vs ROP vs ROD vs CHR). Following this, a post-hoc analysis was conducted for each combination that yielded a significant result, aimed at evaluating the pairwise differences of distance distributions.  
The subsequent configurations of Cover parameters, along with the resulting _p-value_ matrix, are provided below, highlighting the most pertinent findings.

![Post-hoc analysis Isomap](/Images/post_hoc_isomap.png)


