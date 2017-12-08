nr_val=(64 128 256 512 1024)
ni_val=(4 8 16 32 64 128)
npf_val=(4 8 16 32 64 128)

if [[ -f "report.dat" ]]; then
	rm "report.dat"
fi
touch "report.dat"

for nr in ${nr_val[*]}; do
	for ni in ${ni_val[*]}; do
		for npf in ${npf_val[*]}; do
			$GEM5/build/X86/gem5.opt hw3config.py -c daxpy/daxpy --cpu-type="DerivO3CPU" --caches --l2cache --npf_regs=$npf --nr_entries=$nr --ni_entries=$ni
		done
	done
done > "report.dat"

