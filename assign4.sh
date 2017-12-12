# policy_type=(fetch_policy ROB_policy)
fetch_policy=('SingleThread' 'RoundRobin' 'Branch' 'IQCount' 'LSQCount')
ROB_policy=('Dynamic' 'Partitioned' 'Threshold')

rm -r report
rm core*
rm *.txt
mkdir report
# fetch policy
prefix=FetchPolicy\_
for pn in ${fetch_policy[*]} ; do
	fn=$prefix$pn.txt
	$GEM5/build/ARM/gem5.opt hw4config.py --smt -c "daxpy/daxpy_arm;daxpy/daxpy_arm;daxpy/daxpy_arm;daxpy/daxpy_arm" --cpu-type="DerivO3CPU" --caches --l2cache  --fetch_policy=$pn
	cp m5out/stats.txt report/$fn
done
# ROB policy
prefix=ROBPolicy\_
for pn in ${ROB_policy[*]} ; do
	fn=$prefix$pn.txt
	$GEM5/build/ARM/gem5.opt hw4config.py --smt -c "daxpy/daxpy_arm;daxpy/daxpy_arm;daxpy/daxpy_arm;daxpy/daxpy_arm" --cpu-type="DerivO3CPU" --caches --l2cache  --ROB_policy=$pn
	cp m5out/stats.txt report/$fn
done
# patterns='seconds.*simulated|ROBFullEvents'

# for fp in ${fps[*]}; do
# 	for robp in ${robps[*]}; do
# 		$GEM5/build/ARM/gem5.opt hw4config.py --smt -c "daxpy/daxpy_arm;daxpy/daxpy_arm;daxpy/daxpy_arm;daxpy/daxpy_arm" --cpu-type="DerivO3CPU" --caches --l2cache  --fetch_policy=$fp --ROB_policy=$robp  > /dev/null
# 		cat m5out/stats.txt | grep -Ei "$patterns" | grep -Eo '\s+[0-9]+|\s+[0-9]+\.[0-9]+' | sed 's/\s*//g' > temp.txt
# 		if [[ $(cat 'temp.txt' | wc -l) -le '1' ]]; then
# 			echo 0 >> 'temp.txt'
# 		fi
# 		cat 'temp.txt'
# 		rm core* > /dev/null
# 	done
# done > "report.dat"

