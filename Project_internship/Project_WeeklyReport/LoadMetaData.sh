#!/bin/bash

new_meta_data_file="$1"
metadata_python_path="/data/pgaspari/BaseDonnee/.processFile/metaDataPythonFile.txt"
oldIFS=$IFS     # sauvegarde du séparateur de champ
IFS=$'\n'       # nouveau séparateur de champ, le caractère fin de ligne

printf ""> $metadata_python_path
if [ -z "$new_meta_data_file" ]; then
    echo "Error: Input file path not provided."
    echo "Usage: ./LoadMetaData.sh <new_meta_data_file>"
    exit 1
fi
echo RowFile : $new_meta_data_file > $metadata_python_path
for ligne in $(cat $new_meta_data_file)
do 
   if [[ ${ligne:0:3} == "FRB" ]] || [[ ${ligne:0:3} == "SGR" ]]; then
      echo $ligne | cut -d: -f1 >> $metadata_python_path
   elif [[ ${ligne:0:3} == "DM:" ]] ; then
      echo $ligne | cut -d" " -f2 | cut -d. -f1 >> $metadata_python_path
   fi
done

echo "Processing file Successed : New MetaData Base loaded"
