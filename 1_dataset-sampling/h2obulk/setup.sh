for T in {0100..1000..100}
do
 
	mkdir ${T}
	cd ${T}

	for file in  run-driver.sh init.xyz  input.xml  input_replay.xml  submit.sh submit_replay.sh
	do

		sed "s/xxxTxxx/${T}/g" ../${file} > ${file}

	done

	cd ..
done
