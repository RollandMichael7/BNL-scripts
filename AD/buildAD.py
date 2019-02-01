# This script downloads and compiles EPICS base, EPICS modules, and AreaDetector as a synApps package
#
# Author: Michael Rolland
# Copyright (c): Brookhaven National Laboratory
# Created: February 1, 2019



import subprocess
import fileinput
import sys
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

# ensure dependencies
# run("sudo apt install libreadline-dev")
# run("sudo apt install libx11-dev")
# run("sudo apt install libboost-dev")
# run("sudo apt install libboost-test-dev")
# run("sudo apt install re2c")
# run("sudo apt install libxext-dev")

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

# compile EPICS stuff
run("make -C epics-base-7-0-1-1 -sj")
run("make -C support -sj")


################ areaDetector ################

# copy from examples
wd = os.getcwd()
os.chdir(wd + "/support/areaDetector/configure")
run("bash copyFromExample")
os.chdir(wd)
run("rm support/areaDetector/configure/EXAMPLE*")

# modify configuration files
config_files = ["RELEASE_LIBS.local", "RELEASE_PRODS.local", "RELEASE_SUPPORT.local"]
for config in config_files:
	for line in fileinput.input("support/areaDetector/configure/"+config, inplace=True):
		if line.strip().startswith("#"):
			print(line, end="")
			continue
		found=False
		macro = line.split("=")[0]
		for module in epics_modules:
			if module.upper() == macro:
				print(macro+"=$(SUPPORT)/"+module)
				found=True
				break
		if not found:
			if "AREA_DETECTOR=" in line:
				print("AREA_DETECTOR=$(SUPPORT)/areaDetector")
			elif "EPICS_BASE=" in line:
				print("EPICS_BASE="+wd+"/epics-base-7-0-1-1")
			elif "SUPPORT=" in line:
				print("SUPPORT="+wd+"/support")
			elif "DEVIOCSTATS=" in line:
				print("DEVIOCSTATS=$(SUPPORT)/iocStats")
			elif "SNCSEQ=" in line:
				print("SNCSEQ=$(SUPPORT)/seq-2-2-5")
			else:
				print(line, end="")

# compile
run("make -C support/areaDetector/ADSupport -sj")
run("make -C support/areaDetector/ADCore -sj")
