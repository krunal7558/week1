#!/usr/bin/env python

import yaml
import json


if __name__=="__main__":
   data = ['tor-rtr-01',15,{'ip_addr':'10.201.123.10','vendor':'Cisco Systems Inc.'} ]
   with open('router.json','w') as fh:
      fh.write(json.dumps(data,indent=4))
   #print(json.dumps(data,indent=4))
