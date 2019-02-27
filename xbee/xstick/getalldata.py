from digi.xbee.devices import XBeeDevice
from digi.xbee.io import IOLine, IOMode
import time

port = "/dev/ttyUSB0"
baud = 9600

node_ids = ["SENSE1", "SENSE2", "SENSE3"]

lightADC = IOLine.DIO1_AD1
tempADC = IOLine.DIO2_AD2
humidityADC = IOLine.DIO3_AD3


def main():
    local_device = XBeeDevice(port, baud)
    local_device.open()

    # Obtain the remote XBee device from the XBee network.
    net = local_device.get_network()
    remotes = [net.discover_device(node) for node in node_ids]

    #for remote in remotes:
    #    remote.set_io_configuration(IOLINE_IN, IOMode.ADC)
    while True:
        for remote in remotes:
            raw_light = remote.get_adc_value(lightADC)
            light = (raw_light / 1023) * 1200
            
            raw_temp = remote.get_adc_value(tempADC)
            mVanalog = (raw_temp / 1023) * 1200
            temp = (mVanalog - 500) / 10
            
            raw_humidity = remote.get_adc_value(humidityADC)
            mVanalog = (raw_humidity / 1023) * 1200
            humidity = (((mVanalog * 108.2 / 33.2) / 5000 - .16) / .0062)
            
            print(str(remote) + ": " + str(light))
            print(str(remote) + ": " + str(temp) + "C")
            print(str(remote) + ": " + str(humidity) + "%")

        time.sleep(1)

if __name__ == '__main__':
    main()