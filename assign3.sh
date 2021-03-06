nr_val=(4 8 16 32 64 128)
ni_val=(4 8 16 32 64 128)
npf_val=(64 128 256 512 1024)

# if [[ ! -f "report.dat" ]]; then
# 	touch "report.dat"
# fi

patterns='seconds.*simulated|ROBFullEvents'

for nr in ${nr_val[*]}; do
	for ni in ${ni_val[*]}; do
		for npf in ${npf_val[*]}; do
			$GEM5/build/X86/gem5.opt hw3config.py -c daxpy/daxpy --cpu-type="DerivO3CPU" --caches --l2cache --npf_regs=$npf --nr_entries=$nr --ni_entries=$ni > /dev/null
			cat m5out/stats.txt | grep -Ei "$patterns" | grep -Eo '\s+[0-9]+|\s+[0-9]\.[0-9]+' | sed 's/\s*//g' > temp.txt
			if [[ $(cat 'temp.txt' | wc -l) -eq '1' ]]; then
				echo 0 >> 'temp.txt'
			fi
			cat 'temp.txt'
			rm core* > /dev/null
		done
	done
done > "report.dat"

