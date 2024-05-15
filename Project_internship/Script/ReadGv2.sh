#!/bin/sh
filename=$1
find -type f -newer $filename | grep singlepulse.ps | while  read path ; do
  echo $path
  gv $path
  read -p "Appuez sur une touche pour continuer... "
done
