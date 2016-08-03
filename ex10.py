#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse



if __name__=='__main__':
   conf = CiscoConfParse('cisco_ipsec.txt')
   parents = conf.find_objects_w_child(parentspec=r'^crypto map CRYPTO.*',childspec=r'set pfs group2')
   for parent in parents:
      print parent.text
      for child in parent.children:
          print child.text
