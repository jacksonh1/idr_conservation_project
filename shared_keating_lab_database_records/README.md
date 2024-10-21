
# important file paths on Dave
- IUPRED2A: `/mnt/shared/shared_data/iupred2a`
- orthoDB downloaded data and sqlite databases = `/mnt/shared/shared_data/orthoDB/orthodb_data/`
- orthoDB precalculated clustered least divergent ortholog groups for human: `/mnt/shared/shared_data/orthoDB/orthodb_preprocessed_databases/human_orthogroups_v3/`

# Keating lab specific instructions
I have precalculated a database of orthologs on the Keating lab workstation called Dave. Here are the steps to use the pipeline on Dave (from scratch):


if you don't have conda (or mamba) installed, install it:
```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh"
bash Miniforge3-Linux-x86_64.sh
```

install the tools that I wrote and preconfigured:
```bash
cd /mnt/shared/shared_data/orthoDB/CODE/
make environment
```

activate the environment to use the tools:
```bash
mamba activate odb_conservation_pipeline
```

see [./environment_setup.md](./environment_setup.md) for how this environment was set up.


## using the pipeline

Read the readme files for the individual tools to learn how to use them. Pay particular attention to the parameters that you can adjust. Look at the `examples/` directory in each repo to see how the tools can be used.

You can also look at `/mnt/shared/shared_data/orthoDB/example_analysis_2_Joels_table/` for an example analysis. Here are the steps that were run:<br>
map the uniprot ids in FP4Y_motif_SLIMSearch4_data.csv to orthodb gene ids:
```bash
mamba activate odb_conservation_pipeline
"odb_groups-map_uniprotid" -i "./FP4Y_motif_SLIMSearch4_data.csv" --uni_column "ProteinAcc"
```
Then run the conservation score pipeline:
```bash
"slim_conservation_scoring-pipeline" -c ./step2_params.yaml -n 6
```

The list of available command line tools are explained in the readme files of the individual repositories, but here is a list:
- `odb_groups-map_uniprotid`
- `odb_groups-orthogroup_pipeline`
- `odb_groups-pipeline_all_genes_in_species`
- `odb_groups-pipeline_input_table`
- `odb_groups-create_filemap`
- `slim_conservation_scoring-pipeline`

You can find out more about each script by running any of them with the `--help` flag. For example:
```bash
"odb_groups-map_uniprotid" --help
```

To see how I set up the orthoDB database, see [./orthoDB_database_setup.md](./orthoDB_database_setup.md).

