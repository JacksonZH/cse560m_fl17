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
	parser.add_option('--fetch_policy', type="str", default="SingleThread")
	# available policies: Dynamic Partitioned Threshold
	parser.add_option('--LSQ_policy', type="str", default="Dynamic")
	# available policies: Dynamic Partitioned Threshold
	parser.add_option('--IQ_policy', type="str", default="Dynamic")
	# available policies: Dynamic Partitioned Threshold
	parser.add_option('--ROB_policy', type="str", default="Dynamic")
	# available policies: Aggressive RoundRobin OldestReady
	parser.add_option('--commit_policy', type="str", default="Aggressive")

#set parameters taken in from options on command line
def set_config(cpu_list, options):
  for cpu in cpu_list:
    # set parameters for each thing
    cpu.numROBEntries = options.nr_entries
    cpu.numIQEntries = options.ni_entries
    cpu.numPhysFloatRegs = options.npf_regs
    cpu.smtFetchPolicy = options.fetch_policy
    cpu.smtLSQPolicy = options.LSQ_policy
    cpu.smtIQPolicy = options.IQ_policy
    cpu.smtROBPolicy = options.ROB_policy
    cpu.smtCommitPolicy = options.commit_policy
