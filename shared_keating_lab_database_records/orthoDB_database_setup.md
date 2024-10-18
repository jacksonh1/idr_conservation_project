## orthodb database setup record
Here are details for how I set up the orthodb database

I downloaded the orthoDB data from the orthoDB website: https://data.orthodb.org/download/

I then set up the environment as explained in [./environment_setup.md](./environment_setup.md). I used the `make environment` command to create the environment.

I then created the sqlite database for the orthoDB files:
```bash
cd "/mnt/shared/shared_data/orthoDB/CODE/slim_conservation_orthogroup_generation"
bash ./prepare_data.sh
```
Note: This took a while so I used `nohup` to run it in the background.

Then I created the new "database" using these tools.<br>
I used the `odb_groups-pipeline_all_genes_in_species` command to create the database for all human proteins in orthoDB. I used the following commands:
```bash
mamba activate odb_conservation_pipeline
cd "/mnt/shared/shared_data/orthoDB/orthodb_preprocessed_databases/human_orthogroups_v4"
"odb_groups-pipeline_all_genes_in_species" -c "./params.yml" --species_id "9606_0" -o -n 30 -f
```
The `params.yml` file is in the same `human_orthogroups_v4` directory (`/mnt/shared/shared_data/orthoDB/orthodb_preprocessed_databases/human_orthogroups_v4/params.yml`).
The contents of the `params.yml` file are:
```yaml
filter_params:
  min_fraction_shorter_than_query: 0.5

og_select_params:
  OG_selection_method: level_name

ldo_select_params:
  LDO_selection_method: alfpy_google_distance

align_params:
  align: true
  n_align_threads: 2

main_output_folder: ./database
```
Note: This took a while so I used `nohup` to run it in the background.

I then changed the permissions of the directories `./CODE`, `./orthodb_data`, and `./orthodb_preprocessed_databases` such that anyone in the "slims" group can access them. I used commands like: 
`sudo chgrp -R slims ./CODE/`
`sudo chmod -R g+w ./CODE/`

