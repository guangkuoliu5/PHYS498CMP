#!/bin/bash

for bJ in $(seq 0 0.01 1.5)
do
	printf "beta=$bJ\nLx=27\nLy=27\noutFile=27data3/out_L27_$bJ" > params
	./main
done
#bJ=999999
#printf "beta=$bJ\nLx=27\nLy=27\noutFile=27data/out_L27_$bJ" > params
#./main
