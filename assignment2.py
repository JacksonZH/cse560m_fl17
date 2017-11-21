import m5
from m5.objects import *
import os
from Caches import *
from common import SimpleOpts
gem5_path = os.environ["GEM5"]

SimpleOpts.add_option('--clock', help="clock frequency")
(opts, args) = SimpleOpts.parse_args()

"""create system obj"""
system = System()

"""create clock domain"""
system.clk_domain = SrcClockDomain()
if opts.clock:
  print "setting clock frequency as ",opts.clock
  system.clk_domain.clock = opts.clock
else:
  system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain()

"""memory simulation mode"""
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

"""create CPU"""
system.cpu = TimingSimpleCPU()

"""create memory bus"""
system.membus = SystemXBar()
system.l2bus = L2XBar()

"""create cache"""
system.cpu.icache = L1_ICache(opts)
system.cpu.dcache = L1_DCache(opts)
system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectCPU(system.cpu)
system.cpu.icache.connectBus(system.l2bus)
system.cpu.dcache.connectBus(system.l2bus)
system.cpu.l2cache = L2Cache(opts)
system.cpu.l2cache.connectCPU(system.l2bus)
system.cpu.l2cache.connectBus(system.membus)

"""create I/O controller"""
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.master
system.cpu.interrupts[0].int_master = system.membus.slave
system.cpu.interrupts[0].int_slave = system.membus.master

system.system_port = system.membus.slave

"""create memory controller"""
system.mem_ctrl = DDR3_1600_8x8()
system.mem_ctrl.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.master

"""create process"""
#isa = str(m5.defines.buildEnv['TARGET_ISA']).lower()
#binary = gem5_path + '/tests/test-progs/hello/bin/' + isa + '/linux/hello'
if len(args) == 1:
  binary = args[0]
elif len(args) > 1:
  SimpleOpts.print_help()
  m5.fatal("Expected a binary to execute as positional argument")
process = Process()
process.cmd = [binary]
system.cpu.workload = process
system.cpu.createThreads()

"""instantiate a system"""
root = Root(full_system = False, system = system)
m5.instantiate()
print "Beginning simulation!"
exit_event = m5.simulate()
print 'Exiting @ tick %i because %s' % (m5.curTick(), exit_event.getCause())
