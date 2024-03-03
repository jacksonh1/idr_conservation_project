mamba activate odb_groups_x86
cd ./p1_odb_clustered_ldos/
nice -n19 nohup bash create_database.sh > create_database.out &
cd ..
cd ./p2_alignments/
nice -n19 nohup python info_json_2_clusteredldofa_nonsnakemake.py > info_json_2_clusteredldofa_nonsnakemake.out &
nohup snakemake --cores 60 --jobs 8 > snakemakeoutput.out &
rm -r ../database/clustered_ldo_fastas/

cd ..
mamba activate slim_conservation
cd ./p3_alignment_scores/
nice -n19 nohup python property_entropy_scores.py > property_entropy_scores.out &

cd ..
cd ./p4_file_key/
python ./generate_database_key.py 
