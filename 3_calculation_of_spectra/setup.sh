for T in 0.5 1 2 5 10 20 50 150 300 600
do

  mkdir ${T}
   
  for t in {00..00} 
  do
  mkdir ${T}/${t}
  cd ${T}/${t}
  
  sed "s/xxxTxxx/${T}/g" ../../input.xml > input.xml
  sed -i "s/xxxtxxx/${t}/g" input.xml
  sed "s/xxxTxxx/${T}/g" ../../in.lmp > in.lmp
  sed -i "s/xxxtxxx/${t}/g" in.lmp
  sed "s/xxxTxxx/${T}/g" ../../rundriver.sh > rundriver.sh
  sed -i "s/xxxtxxx/${t}/g" rundriver.sh
  sed "s/xxxTxxx/${T}/g" ../../submit.sh > submit.sh
  sed -i "s/xxxtxxx/${t}/g" submit.sh

  cp ../../init.xyz init.xyz

  cd ../../
  done

done
