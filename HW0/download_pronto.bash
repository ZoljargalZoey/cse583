cd
mkdir cse583
cd cse583/
mkdir pronto 
touch README.txt
nano README.txt
mkdir data
cd data/
curl -O https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
unzip open_data_year_one.zip
head 2015_trip_data.csv

