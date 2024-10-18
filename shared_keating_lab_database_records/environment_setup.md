# slim conservation environment
This environment is composed of 2 custom pipelines. Both pipelines have their own repositories, however they are can be installed in the same environment. The [./Makefile](./Makefile) and [./environment.yml](./environment.yml) files in this directory make it easier to create the environment.

All that you have to do to use the tools is make sure that conda/mamba is installed and then navigate to the directory containing the makefile (should be `/mnt/shared/shared_data/orthoDB/CODE/`) and run the command `make environment`. This will create a conda environment called `odb_conservation_pipeline` with the necessary dependencies installed and the correct environment variables set. The environment variables are used by the tools to find the necessary files and executables.

## troubleshooting

By default, the makefile assumes that you are using mamba. If you are using conda, you can change the value of `CONDA` in the makefile to `conda` and then run the command `make environment`. 


Using a GPU for the ESM2 embeddings (in PairK) requires certain tools to access and use cuda (cuda must be installed on your system). The makefile automatically does this for dave (the computer) which has cuda 12.1 installed at the time of writing. If this doesn't work or a different version of cuda is installed that you want to use, modify the `CUDA_INSTALL_COMMAND` value in the makefile to whatever cuda installation command you need. Follow the instructions from pytorch on what conda command to use. 


## recreating the environment
If something happens to dave (the computer) and you have to recreate the directory `/mnt/shared/shared_data/orthoDB/CODE/`, you can recreate the environment by following these steps:
- navigate to the directory that you want to be the new `CODE` directory.
- clone the slim_conservation_orthogroup_generation and slim_conservation_scoring repositories:
    ```bash
    git clone https://github.com/jacksonh1/slim_conservation_orthogroup_generation.git
    git clone https://github.com/jacksonh1/slim_conservation_scoring.git
    ```
- change the environment variables in the `.env` files in the `env_variables` directories of the two repositories to point to the correct iupred and orthoDB files. For example, I used the following commands to change those variables:
    ```bash
    sed -i "s|ORTHODB_DATA_DIR = '/Users/jackson/Dropbox (MIT)/work/07-SLiM_bioinformatics/04-orthoDB_local_orthogroup_creation/data/orthoDB_sample_data/'|ORTHODB_DATA_DIR = '/mnt/shared/shared_data/orthoDB/orthodb_data/'|g" ./slim_conservation_orthogroup_generation/orthodb_tools/env_variables/.env
    sed -i "s|IUPRED2A_LIB_DIR = '/Users/jackson/tools/iupred2a/'|IUPRED2A_LIB_DIR = '/mnt/shared/shared_data/iupred2a'|g" ./slim_conservation_scoring/slim_conservation_scoring/env_variables/.env
    ```
    - you don't have to use `sed` like I did, you can just change the files manually.
    - more details are in the README.md files of the two repositories.

