"""Verify public aggregate derivatives with Python's standard library."""
from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parent
def read(name):
 with (ROOT/name).open(newline='') as f:return list(csv.DictReader(f))
rows=read('charge-counts.csv');assert len(rows)==52
for r in rows:
 a,b=int(r['h1_2025']),int(r['h1_2026'])
 assert b-a==int(r['net_change'])
 assert round((b-a)/a*100,1)==float(r['change_pct'])
 assert r['source_report'].startswith('https://commercialmortgagesbroker.co.uk/research/')
national=[r for r in rows if r['level']=='national'];regions=[r for r in rows if r['level']=='region'];counties=[r for r in rows if r['level']=='county']
assert len(national)==1 and len(regions)==7 and len(counties)==44
for year in ('h1_2025','h1_2026'):assert sum(int(r[year]) for r in regions)==int(national[0][year])
assert sum(int(r['net_change']) for r in regions)==136
assert [sum(int(r['net_change'])>0 for r in counties),sum(int(r['net_change'])<0 for r in counties),sum(int(r['net_change'])==0 for r in counties)]==[26,16,2]
expected=sorted(regions,key=lambda r:float(r['change_pct']),reverse=True)
for a,b in zip(expected,read('regional-contributions.csv')):
 for k,v in b.items():assert a[k]==v
chart=read('datawrapper-regions.csv');assert len(chart)==7
assert [(r['area'],float(r['change_pct'])) for r in expected]==[(r['Region'],float(r['H1 change (%)'])) for r in chart]
print('PASS: 52 observations; count differences, rates, seven-region reconciliation, county directions and chart values.')
