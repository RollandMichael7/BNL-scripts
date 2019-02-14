import os
from socket import *
from caproto.server import pvproperty, PVGroup, ioc_arg_parser, run
from caproto.threading.client import Context


class XBeeIOC(PVGroup):
	# time in between scans
	dt = pvproperty(value=3.0)

	Light1 = pvproperty(value=-1.0)
	Temp1 = pvproperty(value=-1.0)
	RelH1 = pvproperty(value=-1.0)

	Light2 = pvproperty(value=-1.0)
	Temp2 = pvproperty(value=-1.0)
	RelH2 = pvproperty(value=-1.0)

	Light3 = pvproperty(value=-1.0)
	Temp3 = pvproperty(value=-1.0)
	RelH3 = pvproperty(value=-1.0)

	pvs = [Light1, Temp1, RelH1, Light2, Temp2, RelH2, Light3, Temp3, RelH3]

	# TODO: figure out how to create PVs procedurally
	nSensors = 3

	# pvsL = [pvproperty(value=-1.0, name="Light"+str(i+1)) for i in range(nSensors)]
	# pvsT = [pvproperty(value=-1.0, name="Temp"+str(i+1)) for i in range(nSensors)]
	# pvsH = [pvproperty(value=-1.0, name="RelH"+str(i+1)) for i in range(nSensors)]
	# for pv in pvsL:
	# 	setattr(pv.name, pv)
	# for pv in pvsT:
	# 	setattr(pv.name, pv)
	# for pv in pvsH:
	# 	setattr(pv.name, pv)

	@dt.startup
	async def dt(self, instance, async_lib):
		'Periodically update sensor values'

		#print(type(self.Light1))
		#print(type(self.pvs[0]))
		
		UDPSock = socket(AF_INET, SOCK_DGRAM)
		addr = ("", 13000)
		buf = 1024
		UDPSock.bind(addr)

		while True:
			(data, addr) = UDPSock.recvfrom(buf)
			readings = data.decode('utf-8').split('\n')

			# TODO: do this in a not stupid way
			await self.Light1.write(float(readings[0][3:]))
			await self.Temp1.write(float(readings[1][3:]))
			await self.RelH1.write(float(readings[2][3:]))
			await self.Light2.write(float(readings[3][3:]))
			await self.Temp2.write(float(readings[4][3:]))
			await self.RelH2.write(float(readings[5][3:]))
			await self.Light3.write(float(readings[6][3:]))
			await self.Temp3.write(float(readings[7][3:]))
			await self.RelH3.write(float(readings[8][3:]))
    		
    		# Let the async library wait for the next iteration
			await async_lib.library.sleep(self.dt.value)


if __name__ == '__main__':
	ioc_options, run_options = ioc_arg_parser(
		default_prefix='XBee:',
		desc='Read XBee wi-fi sensors.')
	ioc = XBeeIOC(**ioc_options)
	run(ioc.pvdb, **run_options)
