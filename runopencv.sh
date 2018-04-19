#!/bin/bash
source /etc/profile.d/hadoop.sh
while read line
do
	python /home/hpistor/cinf401-assignments/cinf401-project-3/opencv.py $line
done
