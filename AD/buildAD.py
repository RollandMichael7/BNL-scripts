import subprocess
import os

# for some reason EPICS modules has no central repo, so we have to hardcode in a list of modules
epics_modules = [
	"alive", "asyn", "autosave", "busy", "calc", "camac", "caputRecorder", "dac128V", "delaygen", "dxp", 
	"dxpSITORO", "iocStats", "ip", "ipac", "ip330", "ipUnidig", "love", "lua", "mca", "measComp", "modbus", 
	"motor", "optics", "quadEM", "softGlue", "softGlueZynq", "sscan", "std", "stream", "vac", "vme", 
	"Yokogawa_DAS", "xxx"
]
# EPICS modules that require areaDetector to be compiled first
ad_dependents = [ "quadEM", "dxp", "dxpSITORO" ]

# subprocess.run takes a list of arguments
def run(command):
	subprocess.run(command.split())

# download EPICS base
run("git clone -b 7.0 https://git.launchpad.net/epics-base epics-base-7-0-1-1")
run("git -C epics-base-7-0-1-1 submodule update --init --reference ./")

# download EPICS modules
run("git clone https://github.com/EPICS-synApps/support")
for module in epics_modules:
	run("git -C support clone https://github.com/epics-modules/"+module)
# get StreamDevice submodule
run("git -C support/stream submodule init")
run("git -C support/stream submodule update")
# seq is not on github
run("wget http://www-csr.bessy.de/control/SoftDist/sequencer/releases/seq-2.2.5.tar.gz")
run("tar -zxf seq-2.2.5.tar.gz")
run("rm -f seq-2.2.5.tar.gz")
run("mv seq-2.2.5 support/seq-2-2-5")

# download synapps configuration for compiling
run("git -C support clone https://github.com/EPICS-synApps/configure")

# download AreaDetector
run("git -C support clone --recursive https://github.com/areaDetector/areaDetector.git")
for folder in os.listdir("support/areaDetector"):
	if os.path.isdir("support/areaDetector/" + folder): #and folder.startswith("AD"):
		print(folder)
		run("git -C support/areaDetector/"+folder+" checkout master")

# configuration
# throw out the old RELEASE file
run("rm support/configure/RELEASE")
with open("RELEASE", "w") as release:
	release.write("SUPPORT="+os.getcwd()+"/support\n")
	release.write("-include $(TOP)/configure/SUPPORT.$(EPICS_HOST_ARCH)\n")
	release.write("EPICS_BASE="+os.getcwd()+"/epics-base-7-0-1-1\n")
	release.write("-include $(TOP)/configure/EPICS_BASE\n")
	release.write("-include $(TOP)/configure/EPICS_BASE.$(EPICS_HOST_ARCH)\n\n")
	release.write("#AREA_DETECTOR=$(SUPPORT)/areaDetector\n")
	for module in epics_modules:
		if module is "iocStats":
			release.write("DEVIOCSTATS=$(SUPPORT)/iocStats\n")
			continue
		# some modules can't be compiled before area detector; comment them out
		if module in ad_dependents:
			release.write("#")
		release.write(module.upper()+"=$(SUPPORT)/"+module+"\n")
	release.write("SNCSEQ=$(SUPPORT)/seq-2-2-5\n")
run("mv RELEASE support/configure/")
run("make -C support/ release")

# compile
run("make -C epics-base-7-0-1-1 -sj")
run("make -C support -sj")