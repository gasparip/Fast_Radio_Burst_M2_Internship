#!/bin/bash
DataNameToLoad=$1
if [[ $DataNameToLoad == "" ]]; then
echo "Vous n'avez pas entrée de base de donnée ! "
exit
fi
dirPath='/data/pgaspari/BaseDonneeProject/NewVersion'
ListDataBase=$dirPath'/.processScript/ListDataBase.txt'
dataBaseDirectory="dataBase"
printf ''>$ListDataBase

oldIFS=$IFS     # sauvegarde du séparateur de champ
IFS=$'\n'  
for NameDataBase in $(find $dirPath/$dataBaseDirectory/ -type d)
do 
echo `basename $NameDataBase` >> $ListDataBase
done
tail -n +2 $ListDataBase > $ListDataBase"2"
mv $ListDataBase"2" $ListDataBase

if grep -qx $DataNameToLoad $ListDataBase; then
    echo "La valeur $DataNameToLoad est présente dans le fichier $ListDataBase."
else
    echo "La valeur $DataNameToLoad n'est pas présente dans le fichier ! Les bases de données disponibles sont : "
    cat $ListDataBase
    exit
$IFS = $oldIFS	
fi

#### Actuellement en mode path day date, But this can change.
# Nenufar
if [[ $DataNameToLoad == "NenufarPULSAR" ]]; then 
PathDataBaseNenufarPulsarMode=$dirPath/.processScript/PathDataBaseNenufarPulsarMode.txt
DataBase_NenufarPULSAR=$dirPath/$dataBaseDirectory/"NenufarPULSAR/DataBase_NenufarPULSAR.txt"
ls /databf/nenufar-pulsar/??05/*/*/*.fits > $PathDataBaseNenufarPulsarMode
echo 'header_NenufarPULSAR: Name Date Path'> $DataBase_NenufarPULSAR
for lignePULSAR in $(cat $PathDataBaseNenufarPulsarMode)
do
echo $lignePULSAR | cut -d/ -f7 | cut -d_ -f1 >> $DataBase_NenufarPULSAR
echo $lignePULSAR | cut -d/ -f7 | cut -d_ -f2 | cut -dT -f1 | cut -dD -f2 >> $DataBase_NenufarPULSAR
echo $lignePULSAR >> $DataBase_NenufarPULSAR
done 

elif [[ $DataNameToLoad == "NenufarTF" ]]; then 
PathDataBaseNenufarTFMode=$dirPath/.processScript/PathDataBaseNenufarTFMode.txt
DataBase_NenufarTF=$dirPath/$dataBaseDirectory/"NenufarTF/DataBase_NenufarTF.txt"
ls -d /databf/nenufar-tf/??05/*/*/* > $PathDataBaseNenufarTFMode
echo 'header_NenufarTF: Name Date Path Duration'> $DataBase_NenufarTF
for ligneTF in $(cat $PathDataBaseNenufarTFMode)
do
echo $ligneTF | cut -d/ -f7 | cut -d_ -f5 >> $DataBase_NenufarTF
echo $ligneTF | cut -d/ -f7 | cut -d_ -f1 >> $DataBase_NenufarTF
echo $ligneTF >> $DataBase_NenufarTF
#cat `$ligneTF'/*.parset' | grep -E 'Beam\[0\].duration' | tail -1 | cut -d= -f2`
#!/bin/bash
output=$(cat "$ligneTF"/*.parset 2>&1 | grep -E 'Beam\[0\].duration' | tail -1 | cut -d= -f2)
if [[ $output == '' ]]; then
output=$(cat "$ligneTF"/L0/*.parset 2>&1 | grep -E 'Beam\[0\].duration' | tail -1 | cut -d= -f2)
fi
#echo $output >> $DataBase_NenufarTF

done 

#elif [[ $DataNameToLoad == "Chime" ]]; then
fi
