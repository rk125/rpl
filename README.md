script to edit RPL on IOS XR using ncclient
tested on v7.8.1

to use:
- make .txt file with RPL (must be correct syntax or "edit" will fail)
- run script with:
  - for edit:
      python3 edit-cfg.py <server> <username> <password> <file> edit
  - for delete:
      python3 edit-cfg.py <server> <username> <password> <file> delete

for now only one rpl per file
