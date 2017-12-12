from m5 import fatal
import m5.objects
from textwrap import TextWrapper

#add options for number of ROB entries, IQ entries, and number of physical
#floating point registers
def addHW4Opts(parser):
	parser.add_option('--nr_entries', type="int", default=192)
	parser.add_option('--ni_entries', type="int", default=64)
	parser.add_option('--npf_regs', type="int", default=1024)
	# available policies: SingleThread RoundRobin Branch IQCount LSQCount
	# parser.add_option('--fetch_policy', type="str", default="SingleThread")
	parser.add_option('--fetch_policy', type="str")
	# available policies: Dynamic Partitioned Threshold
	# parser.add_option('--ROB_policy', type="str", default="Dynamic")
	parser.add_option('--ROB_policy', type="str")

#set parameters taken in from options on command line
def set_config(cpu_list, options):
  for cpu in cpu_list:
    # set parameters for each thing
    cpu.numROBEntries = options.nr_entries
    cpu.numIQEntries = options.ni_entries
    cpu.numPhysFloatRegs = options.npf_regs
    if options.fetch_policy:
	    cpu.smtFetchPolicy = options.fetch_policy
    if options.ROB_policy:
	    cpu.smtROBPolicy = options.ROB_policy
