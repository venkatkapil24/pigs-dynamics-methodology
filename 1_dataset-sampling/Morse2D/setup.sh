for T in {0100..1000..100} 150
do
 
	mkdir ${T}
	cd ${T}

	for file in init.xyz  input.xml  input_replay.xml  submit_replay.sh  submit.sh run-ase.py
	do

		sed "s/xxxTxxx/${T}/g" ../${file} > ${file}

	done

	cd ..
done
