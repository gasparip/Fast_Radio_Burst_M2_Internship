#!/bin/bash
echo 'find /databf/nenufar-tf/??05/ -name '*parset' | grep -E FRB | cut -d'/' -f7 | cut -d'_' -f5 | sort | uniq -c'
find /databf/nenufar-tf/??05/ -name '*parset' | grep -E FRB | cut -d'/' -f7 | cut -d'_' -f5 | sort | uniq -c 
exit 1

