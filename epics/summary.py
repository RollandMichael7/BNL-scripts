import sys
import re

def incrementTime(hour, minute):
	nextHour = hour
	nextMin = str(int(minute) + 1)
	if int(nextMin) < 10:
		nextMin = '0' + str(int(nextMin))
	elif nextMin == '60':
		nextMin = '00'
		nextHour = str(int(hour) + 1)
	if int(nextHour) < 10:
		nextHour = '0' + str(int(nextHour))
	elif nextHour == '24':
		nextHour = '00'
	return nextHour, nextMin

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Usage: summary [filename]")
		exit(1)

	f = open(sys.argv[1], "r")
	lines = f.readlines()

	# first time is on the third line
	m = re.search('(\d\d:\d\d)', lines[2])
	time = m.group(0)
	hour, minute = time.split(':')
	nextHour, nextMin = incrementTime(hour, minute)
	m = re.search('\d+\.\d', lines[2])
	battery = float(m.group(0))

	print(lines[2], end='')
	diffs = []

	for line in lines[3:]:
		m = re.search('(' + hour + ':' + minute + '|' + nextHour + ':' + nextMin + ')', line)
		if m is not None:
			hour, minute = m.group(0).split(':')
			nextHour, nextMin = incrementTime(hour, minute)
			m = re.search('\d+\.\d', line)
			if m is not None:
				newBattery = float(m.group(0))
				if battery != 0 and newBattery != 0:
					diff = battery - newBattery
					battery = newBattery
					if diff < 0:
						diff = 0	
					diffs.append(diff)
					print(line.rstrip() + '\t diff: ' + str(diff) + '%')
				else:
					diffs.append(0)
					battery = newBattery
					print(line.rstrip() + '\t diff: ???')

	sum = 0.0
	for diff in diffs:
		sum += diff
	avg = sum / len(diffs)
	print("\navg diff: " + str(avg) + "%")
	lifetime = 100 / avg
	print("expected liftime: " + str(lifetime) + " days")