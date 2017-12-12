fps=('singlethread' 'roundrobin' 'branch' 'iqcount' 'lsqcount')
cps=('aggressive' 'roundrobin' 'oldestready')

# if [[ ! -f "report.dat" ]]; then
# 	touch "report.dat"
# fi

patterns='seconds.*simulated|ROBFullEvents'

for fp in ${fps[*]}; do
	for cp in ${cps[*]}; do
		$GEM5/build/ARM/gem5.opt hw4config.py -c daxpy/daxpy_arm --cpu-type="DerivO3CPU" --caches --l2cache  --fetch_policy='roundrobin' --commit_policy='aggressive'  > /dev/null
		# $GEM5/build/ARM/gem5.opt hw4config.py -c daxpy/daxpy_arm --cpu-type="DerivO3CPU" --caches --l2cache --npf_regs --nr_entries --ni_entries --fetch_policy='roundrobin' --commit_policy='aggressive'  > /dev/null
		cat m5out/stats.txt | grep -Ei "$patterns" | grep -Eo '\s+[0-9]+|\s+[0-9]\.[0-9]+' | sed 's/\s*//g' > temp.txt
		if [[ $(cat 'temp.txt' | wc -l) -eq '1' ]]; then
			echo 0 >> 'temp.txt'
		fi
		cat 'temp.txt'
		rm core* > /dev/null
	done
done > "report.dat"

