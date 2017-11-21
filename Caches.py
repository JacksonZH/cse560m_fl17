# -*- coding: utf-8 -*-
from m5.defines import buildEnv
from m5.objects import *
from common import SimpleOpts

class L1Cache(Cache):
	assoc = 2
	tag_latency = 2
	data_latency = 2
	response_latency = 2
	mshrs = 4
	tgts_per_mshr = 20
	def __init__(self, options=None):
		super(L1Cache,self).__init__()
		pass
	def connectBus(self, bus):
		self.mem_side = bus.slave
	def connectCPU(self, cpu):
		raise NotImplementedError
		
class L1_ICache(L1Cache):
	is_read_only = True
	writeback_clean = True
	size = '16kB'
	SimpleOpts.add_option('--l1i_size', help="L1 instruction cache size. Default: %s" % size)
	SimpleOpts.add_option('--l1i_assoc', help="L1 associativity value. ")
	
	def __init__(self, opts=None):
		super(L1_ICache, self).__init__(opts)
		if opts.l1i_size:
			self.size = opts.l1i_size
		if opts.l1i_assoc:
			self.assoc = opts.l1i_assoc
	
	def connectCPU(self, cpu):
		self.cpu_side = cpu.icache_port
		
class L1_DCache(L1Cache):
	size = '64kB'
	SimpleOpts.add_option('--l1d_size',
		help="L1 data cache size. Default: %s" % size)
	SimpleOpts.add_option('--l1d_assoc',
		help="L1 associativity value. ")
	
	def __init__(self, opts=None):
		super(L1_DCache, self).__init__(opts)
		if not opts or not opts.l1d_size:
			return	
		self.size = opts.l1d_size
# 		if opts.l1d_assoc:
# 			self.assoc = opts.l1d_assoc
			
	def connectCPU(self, cpu):
		self.cpu_side = cpu.dcache_port

class L2Cache(Cache):
	assoc = 8
	tag_latency = 20
	data_latency = 20
	response_latency = 80
	mshrs = 20
	tgts_per_mshr = 12
	write_buffers = 8
	size = '256kB'
	SimpleOpts.add_option('--l2_size',
		help="L2 cache size. Default: %s" % size)
# 	SimpleOpts.add_option('--l2_assoc',
# 		help="L2 associativity value. ")
	def __init__(self, options=None):
		super(L2Cache,self).__init__()
		if not options or not options.l2_size:
			return
		self.size = options.l2_size
		
	def connectBus(self, bus):
		self.mem_side = bus.slave
	def connectCPU(self, cpu):
		self.cpu_side = cpu.master