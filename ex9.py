#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse



if __name__=='__main__':
   conf = CiscoConfParse('cisco_ipsec.txt')
   parents = conf.find_objects(r'^crypto map CRYPTO.*')
   for parent in parents:
      print parent.text
      for child in parent.children:
          print child.text
