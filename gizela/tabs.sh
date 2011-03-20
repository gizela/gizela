#!/bin/bash

# replace tabs with 4 spaces
# according to PEP 8

for i in *.py
do
	echo $i
	cp $i $i.
	cat $i. | sed 's/\t/    /g' > $i
done
