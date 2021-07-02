This script should run after FreeIPA replication install to ensure:
- it overtakes an unassigned DNA ID range, so no range would be lost
- if no unassigned range is available, then ask for a range by creating and deleting user

Run file:
```
ipa -e in_server=True console initdnarange.py
```
Sync with rsync:
```
rsync -aP initdnarange.py cloudbreak@10.112.22.251:~/
```
Versions:
- FreeIPA: 4.6.8
- Python: >=2.7.5 but not 3

For local dev FreeIPA server lib has to be copied under `site-packages` from:
https://github.com/freeipa/freeipa/tree/ipa-4-6/ipaserver