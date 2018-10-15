import sys
import time
import json
from arvpyf import mgmt, cf
from arvpyf.mgmt import ArchiverConfig
from arvpyf.cf import PVFinder

url = "http://xf10id-ca1.cs.nsls2.local:17665/mgmt/bpl"
try:
    print("webapp URL: " + url)
    print("PV prefix: " + sys.argv[1])
except IndexError:
    print("Arguments required: (1) prefix for PVs to delete")
    exit()

arvconf = ArchiverConfig(url)
    
prefix = sys.argv[1]  + "*"
pvs = arvconf.get_all_pvs(regex=prefix)

for pv in pvs:
    print(pv)

paused_pvs = arvconf.pause_archiving_pvs(pvs)
print("PVs paused.")
print("waiting 30 seconds before deleting...")
time.sleep(30)

for i, pv in enumerate(pvs):
      resp = arvconf.delete_pv(pv, deleteData=True)
      print(json.dumps(resp))
