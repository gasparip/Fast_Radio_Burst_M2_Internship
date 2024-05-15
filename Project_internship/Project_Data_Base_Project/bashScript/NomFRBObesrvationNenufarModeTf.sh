#!/bin/bash

ls /databf/nenufar-tf/ES05/*/*/*/L1 | grep .fits | grep -v '_rm' | cut -d'_' -f1 | sort | uniq -c > ./FichierTestModeTF.txt
echo 'ls /databf/nenufar-tf/ES05/*/*/*/L1 | grep .fits | grep -v '_rm' | cut -d'_' -f1 | sort | uniq -c > ./FichierTestModeTF.txt'

exit 1

