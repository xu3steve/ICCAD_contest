#!/bin/bash

for((i = 0;i<9;i++))
do
	echo "============== Round $i ================"
	#echo "  =================================="

	./nmpgen ../cases8/case$i.json testc.py
	python3 map.py ../cases8/case$i.json testp.py

	for((j = 0;j<10;j++))
	do
		echo "  ==== Round $i Iteration $j/10 ===="
		python3 random_gen.py ../cases8/case$i.json name_in.json
		echo "      -> C++ file"
		python3 testc.py name_in.json outc.json
		python3 evaluate.py ../cases8/case$i.json outc.json
		echo "      -> Python file"
		python3 testp.py name_in.json outp.json
		python3 evaluate.py ../cases8/case$i.json outp.json
	done
done
rm testc.py
rm testp.py
rm outc.json
rm outp.json
