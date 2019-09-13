import sys
from time import sleep, localtime, strftime
from epics import caget

if len(sys.argv) != 3:
	print("Arguments required: [PV name] [file name]")
	exit(1)
print("Monitoring " + sys.argv[1])

out = open(sys.argv[2] + ".txt", "w+")
out.write(sys.argv[1] + "\r\n\r\n")
while True:
	val = caget(sys.argv[1])
	time = strftime("%m-%d %H:%M", localtime())
	line = str(time) + "\t" + str(val)
	print(line)
	out.write(line + "\r\n")
	sleep(300)
