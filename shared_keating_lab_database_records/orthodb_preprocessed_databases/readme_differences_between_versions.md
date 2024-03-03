V3 is the version that should be used!


the difference between v2 and v1 is that I am performing the alignment step separately. I am a little bit worried about whether or not Mafft is thread safe when you call multiple processes of mafft simultaneously. I know it's mostly thread safe when you run a single instance of it. I'm using snakemake to handle all of the multiprocessing in v2.

v3 is v2 except I changed the default cdhit command to include `-g 1`. This ensures each protein ends up in the most similar cluster, not the first cluster that meets the threshold. It will have little to no effect on the results. It will only matter when the representative sequence for each cluster is changed which should only matter for the query protein.
