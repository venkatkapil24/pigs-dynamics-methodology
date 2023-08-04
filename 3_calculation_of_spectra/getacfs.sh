for x in */*/;
do
cd ${x};

echo ${x}
split -d -n 10 simulation.xc.xyz
for x in {00..09}
do
i-pi-getacf -ifile x${x} -mlag 4000 -ftpad 0 -ftwin cosine-hanning -oprefix ${x}_xx -der -dt "0.25 femtosecond" &
done

wait

awk '{c1[FNR] +=$1; c2[FNR] += $2; c2sq[FNR] += $2**2; nf[FNR]++}END{for(i=1;i<=FNR;i++)print c1[i] / nf[i], c2[i] / nf[i], (c2sq[i] / nf[i] - (c2[i] / nf[i])**2)**0.5 / nf[i]**0.5}' ??_xx_der_facf.data > xx_der_facf.data

rm x??

cd ../../;
done

wait

