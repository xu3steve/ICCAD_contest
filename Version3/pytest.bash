#!/bin/bash

for((i = 0;i<9;i++))
do
	echo "============== Round $i ================"
	#echo "  =================================="
	#echo "  | Step 1: Generate test.py       |"
	#echo "  =================================="
	python3 map.py ../cases8/case$i.json test.py
	#echo "  =================================="
	#echo "  | Step 2: Generate name_in.json  |"
	#echo "  =================================="
	python3 random_gen.py ../cases8/case$i.json name_in.json
	#echo "  =================================="
	#echo "  | Step 3: Start mapping          |"
	#echo "  =================================="
	python3 test.py name_in.json out.json
	#echo "  =================================="
	#echo "  | Step 4: Checking the Answer    |"
	#echo "  =================================="
	python3 evaluate.py ../cases8/case$i.json out.json
	#echo "  ==> Done"
done
