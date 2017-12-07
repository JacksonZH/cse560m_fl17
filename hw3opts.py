from m5 import fatal
import m5.objects
from textwrap import TextWrapper

#add options for number of ROB entries, IQ entries, and number of physical
#floating point registers
def addHW3Opts(parser):

#set parameters taken in from options on command line
def set_config(cpu_list, options):
  for cpu in cpu_list:
    # set parameters for each thing
