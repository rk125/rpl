#
# RPL edit for XR using ncclient
# make .txt file with RPL (must be correct)
# run script with:
# - for edit:
#     python3 edit-cfg.py <server> <username> <password> <file> edit
# - for delete:
#     python3 edit-cfg.py <server> <username> <password> <file> delete
#
# one rpl per file
# 

import sys, os, warnings, time
warnings.simplefilter("ignore", DeprecationWarning)
from ncclient import manager
from jinja2 import Template

templ_edit=Template(open("rpl_template.xml").read())

def my_unknown_host_cb(host, fingerprint):
    return True

def conf(svr, usr, pwd, rpl_text, action):
    with manager.connect(host=svr, port=830, username=usr, password=pwd, look_for_keys=False, unknown_host_cb=my_unknown_host_cb, \
        hostkey_verify=False, timeout=120) as m:
        with open(rpl_text) as f:
          rpl=f.read()
        if action=="delete":
          operation='xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="delete"'
        elif action=="edit":
          operation=""
        else:
          raise Exception("bad parameter")
        p=templ_edit.render(rpl=rpl , rpl_name=rpl.split("\n")[0].split(" ")[1], operation=operation)
        c = m.edit_config(p, format='xml', target='candidate', default_operation='merge')
        print ("edit  "+str(c))
        c = m.commit()
        print ("commit "+str(c))

if __name__ == '__main__':
    conf(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
