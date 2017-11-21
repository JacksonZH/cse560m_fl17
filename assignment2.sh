simulate(){
	# if assignment2.py exist
	if [[ ! -f 'assignment2.py' ]]; then
		echo 'assignment2.py does not exist!'
		exit 1
	fi
	# set alias
	# type $gem5 &> /dev/null
	# if [[ $? -eq '1' ]]; then
	# 	echo 'setting command "gem5"...'
	# 	gem5=$GEM5/build/X86/gem5.opt
	# fi
	# $1 is filename
	if [[ -f "$1" ]]; then
		echo "deleting previous data file $1..."
		rm "$1"
	fi
	if [[ -f 'm5out' ]]; then
		echo 'deleting previous reports m5out...'
		rm -r m5out
	fi
	# parameters
	echo 'setting allowed cache sizes...'
	cache_size='8kB 16kB 32kB 64kB'
	echo 'initialize grep patterns...'
	patterns='instructions committed|Average Gap Between Requests|dcache.*Overall_Hits.*total|dcache.*replacements|dcache.*Overall_Miss_Rate.*total|icache.*Overall_Miss_Rate.*total|l2cache.*Overall_Miss_Rate.*total|Number of CPU Cycles'
	# create report file
	echo "creating new data file $1..."
	touch "$1"
	
	#$2 is clock speed
	#$3 is cache association
	#$4 is patterns
	echo "simulating..."
	for size in $cache_size; do
		# echo "cache size: $size"
		$GEM5/build/X86/gem5.opt assignment2.py --clock=$2 --l1d_assoc=$3 --l1d_size=$size daxpy/daxpy > /dev/null
		if [[ ! -d 'm5out' ]]; then
			echo 'creating simulation files failed!'
			exit 1
		fi
		cat m5out/stats.txt | grep -Ei "$patterns" | grep -Eo '\s+[0-9]+|\s+[0-9]\.[0-9]+' | sed 's/\s*//g'
		# cat m5out/* | grep -E "$patterns" | tr -cs '0-9.' ' '
		# rm -r m5out
	done >> "$1"
	echo "done!"
}

simulate assoc_1.dat 1.0GHz 1
simulate assoc_2.dat 0.8GHz 2
