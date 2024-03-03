mamba activate odb_groups_x86
cd ./p1_odb_clustered_ldos/
nice -n19 nohup bash create_database.sh > create_database.out &
cd ..

cd ./p2_conservation_scores/
mamba activate slim_conservation
nice -n19 nohup python property_entropy_scores.py > property_entropy_scores.out &
cd ..
cd ./p3_generate_database_key/
python ./generate_database_key.py 
