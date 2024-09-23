#!/bin/bash


age=$1

if [ $age -lt 13 ]; then
	echo "child"
elif [ $age -lt 20 ]; then
	echo "teen"
elif [ $age -lt 65 ]; then
       echo "adult"
elif [ $age -gt 65 ]; then
	echo "elderly"
fi
