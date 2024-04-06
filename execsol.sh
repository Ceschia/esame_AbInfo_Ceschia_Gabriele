#!/bin/bash

#creo la nuova cartella, copio il programma python e lo sposto nella suddetta cartella

mkdir esameCeschia
cp HertzprungRussel.py HertzprungRussel2.py
mv HertzprungRussel2.py esameCeschia

#entro nella cartella

cd esameCeschia

#download file con i dati

wget https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/Nemo_6670.dat --no-check-certificate
export DATA_FILE_PATH=$(pwd)/Nemo_6670.dat
echo $DATA_FILE_PATH

#modifico i permessi di esecuzione del file

chmod +rwx $DATA_FILE_PATH

#start programma pyhton con il nuovo path del file come parametro da riga di comando

python3 HertzprungRussel2.py $DATA_FILE_PATH
