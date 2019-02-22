from caproto.server import pvproperty, PVGroup, ioc_arg_parser, run
from socket import *
import sys
import asyncio

# number of XBee sensors in network
nSensors = 3
# time inbetween sensor reads
timer = 3

# dictionary which will hold PVs later
pvDict = {}


class IOCMain(PVGroup):
    'An IOC with several PVGroups created dynamically'
    shared_value = 5

    def __init__(self, prefix, *, groups, **kwargs):
        super().__init__(prefix, **kwargs)
        self.groups = groups


class XBee(PVGroup):
    setpoint = pvproperty(value=1.0, name='')

    dt = pvproperty(value=timer)

    @dt.startup
    async def dt(self, instance, async_lib):
        'Periodically update PVs'
        while True:
            print(str(pvDict))
            await async_lib.library.sleep(self.dt.value)

    @setpoint.putter
    async def setpoint(self, instance, value):
        print('writing to setpoint the value', value)
        self.ioc.shared_value = value
        return value

    def __init__(self, prefix, *, ioc, **kwargs):
        super().__init__(prefix, **kwargs)
        self.ioc = ioc


def create_ioc(prefix, pvs_a, **ioc_options):
    'Create groups based on prefixes passed in from groups_a, groups_b'
    groups = {}

    ioc = IOCMain(prefix=prefix, groups=groups, **ioc_options)

    for group_pv in pvs_a:
        groups[group_pv] = XBee(f'{prefix}{group_pv}', ioc=ioc)

    for prefix, group in groups.items():
        ioc.pvdb.update(**group.pvdb)

    return ioc, groups


async def writePVs(pvs):
    #await run(ioc.pvdb, **run_options)

    UDPSock = socket(AF_INET, SOCK_DGRAM)
    addr = ("", 13000)
    buf = 1024
    UDPSock.bind(addr)

    while True:
        (data, addr) = UDPSock.recvfrom(buf)
        readings = data.decode('utf-8').split('\n')
        for i in range(nSensors):
            await pvs['Light'+str(i+1)].setpoint.write(float(readings[i*3][3:]))
            await pvs['Temp'+str(i+1)].setpoint.write(float(readings[i*3+1][3:]))
            await pvs['RelH'+str(i+1)].setpoint.write(float(readings[i*3+2][3:]))
        await asyncio.sleep(dt)

                        
if __name__ == '__main__':
    ioc_options, run_options = ioc_arg_parser(
        default_prefix='XBee2:',
        desc=IOCMain.__doc__,
    )

    pvList = []
    for i in range(nSensors):
        pvList.append('Light' + str(i+1))
        pvList.append('Temp' + str(i+1))
        pvList.append('RelH' + str(i+1))

    ioc, pvDict = create_ioc(pvs_a=pvList,
                     **ioc_options,
                     )

    # TODO: figure out how to make this run in background/not block
    #loop = asyncio.get_event_loop()
    #loop.create_task(writePVs(pvs))
    #loop.run_forever()


run(ioc.pvdb, **run_options)