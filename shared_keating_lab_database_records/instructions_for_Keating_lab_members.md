
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

install part 1 of the preconfigured source tools (accessing the orthodb database):
```bash
cd /mnt/shared/shared_data/orthoDB/CODE/orthogroup_generation
mamba env create -f environment_linux.yml
mamba activate odb_groups_x86
pip install -e .
```
install part 2 of the preconfigured source tools (running the conservation pipeline):
```bash
cd /mnt/shared/shared_data/orthoDB/CODE/motif_conservation_in_IDRs
mamba env create -f environment_linux.yml
mamba activate slim_conservation
pip install -e .
```

## using the pipeline

Read the readme files for the individual tools to learn how to use them. Pay particular attention to the parameters that you can adjust. Look at the `examples/` directory in each repo to see how the tools can be used.
look at `/mnt/shared/shared_data/orthoDB/CODE/example_analysis_2_Joels_table/` for an example analysis. Here are the steps that were run:<br>
map the uniprot ids in FP4Y_motif_SLIMSearch4_data.csv to orthodb gene ids:
```bash
mamba activate odb_groups_x86
python "../orthogroup_generation/src/local_scripts/map_uniprotid.py" -i "./FP4Y_motif_SLIMSearch4_data.csv" --uni_column "ProteinAcc"
```
Then run the conservation score pipeline:
```bash
mamba activate slim_conservation
python "../motif_conservation_in_IDRs/src/local_scripts/conservation_analysis.py" -c ./step2_params.yaml -n 6
```

In general, the scripts that are intended to be used the most are located in `/mnt/shared/shared_data/orthoDB/CODE/orthogroup_generation/src/local_scripts/` and `/mnt/shared/shared_data/orthoDB/CODE/motif_conservation_in_IDRs/src/local_scripts/`. You can add these to your PATH variable to make them easier to access. For example, add the following to your `~/.bashrc` file:
```bash
export PATH="/mnt/shared/shared_data/orthoDB/CODE/orthogroup_generation/src/local_scripts/:$PATH"
export PATH="/mnt/shared/shared_data/orthoDB/CODE/motif_conservation_in_IDRs/src/local_scripts/:$PATH"
```
Then you can run the scripts from anywhere on the system. For example:
```bash
map_uniprotid.py -h
conservation_analysis.py -h
```
will show the help messages for the scripts.

## record of how I set up the orthodb database
Here are details for how I set up the orthodb database (also in `/mnt/shared/shared_data/orthoDB/database_setup_information.md`):

I downloaded the orthoDB data from the orthoDB website: https://data.orthodb.org/download/

downloaded orthoDB tools that I wrote:
```bash
git clone https://github.com/jacksonh1/orthogroup_generation.git
```

edited `/mnt/shared/shared_data/orthoDB/CODE/orthogroup_generation/src/local_env_variables/.env` file to add the path to the downloaded orthoDB files:
```
ORTHODB_DATA_DIR = '/mnt/shared/shared_data/orthoDB/orthodb_data/'
```

Downloaded and installed mambaforge: 
```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh"
bash Miniforge3-Linux-x86_64.sh
```

created a virtual environment with the required tools:
```bash
cd /mnt/shared/shared_data/orthoDB/CODE/orthogroup_generation
mamba env create -f environment_linux.yml
mamba activate odb_groups_x86
pip install -e .
```

downloaded conservation tools that I wrote:
```bash
git clone https://github.com/jacksonh1/motif_conservation_in_IDRs.git
```
added iupred directory to `/mnt/shared/shared_data/orthoDB/CODE/motif_conservation_in_IDRs/src/local_env_variables/.env`:
```bash
IUPRED2A_LIB_DIR = '/mnt/shared/shared_data/iupred2a'
```

created a new virtual environment for these tools:
```bash
cd /mnt/shared/shared_data/orthoDB/CODE/motif_conservation_in_IDRs
mamba env create -f environment_linux.yml
mamba activate slim_conservation
pip install -e .
```

Then I created the new "database" using these tools.<br>
see `/mnt/shared/shared_data/orthoDB/orthodb_preprocessed_databases/human_orthogroups_v3` for all of the code to do that. 
The commands are logged in `/mnt/shared/shared_data/orthoDB/orthodb_preprocessed_databases/human_orthogroups_v3/readme_commands_that_were_executed.md`. <br>A copy of the scripts and markdown files is located here in the `./orthodb_preprocessed_databases` directory (relative to this file) - [link](./orthodb_preprocessed_databases/human_orthogroups_v3/).

I then changed the permissions of the directories `./CODE`, `./orthodb_data`, and `./orthodb_preprocessed_databases` such that anyone in the "slims" group can access them. I used commands like: 
`sudo chgrp -R slims ./CODE/`
`sudo chmod -R g+w ./CODE/`