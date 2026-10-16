"""Refresh flat CSV tables and source-qualified knowledge files from the reviewed workbook.

Requires Python 3.10+ and openpyxl. Reads XLSX only; never modifies the workbook.
Run from anywhere: python scripts/export_workbook.py
"""
from pathlib import Path
import csv,json,re,hashlib
from openpyxl import load_workbook

ROOT=Path(__file__).resolve().parents[1]
BOOK=ROOT/'excel'/'ESP_Knowledge_Base.xlsx'
TABLES=['Failures','Rules','Indicators','Actions','Parameters','AI Models','Q and A','Papers','Study Groups','Data Dictionary']
def main():
    wb=load_workbook(BOOK,read_only=True,data_only=False)
    tables={}
    for name in TABLES:
        sh=wb[name]; values=list(sh.values)
        headers=list(values[0])
        if any(not isinstance(h,str) or not h for h in headers) or len(set(headers))!=len(headers):raise ValueError(f'{name}: invalid headers')
        rows=[dict(zip(headers,[v if v is not None else '' for v in row])) for row in values[1:] if any(v is not None for v in row)]
        key='Paper ID' if name=='Papers' else 'Entry ID' if 'Entry ID' in headers else 'Group ID' if name=='Study Groups' else None
        if key and len({r[key] for r in rows})!=len(rows):raise ValueError(f'{name}: duplicate identifiers')
        if key and any(not r[key] for r in rows):raise ValueError(f'{name}: missing identifier')
        for row in rows:
            for h,v in row.items():
                if isinstance(v,str) and v.startswith('='):raise ValueError(f'{name}: unexpected formula in {h}. Keep library records as values.')
            if 'Review status' in row and row['Review status'] not in ['Pending','Reviewed','Rejected']:raise ValueError(f'{name}: invalid review status')
        tables[name]=rows
    papers={p['Paper ID']:p for p in tables['Papers']}
    for name,rows in tables.items():
        for row in rows:
            if name!='Papers' and 'Paper ID' in row and row['Paper ID'] not in papers:raise ValueError(f'{name}: unknown Paper ID')
    (ROOT/'data/csv').mkdir(exist_ok=True,parents=True)
    for name,rows in tables.items():
        with (ROOT/'data/csv'/f'{name}.csv').open('w',encoding='utf-8-sig',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    count=0
    for pid,paper in papers.items():
        out=[f'ESP research knowledge: {pid}',f'Title: {paper["Title"]}',f'Authors: {paper["Authors"]}',f'Year: {paper["Year"]}',f'Publication: {paper["Journal or conference"]}',f'DOI: {paper["DOI"]}',f'Related study group: {paper["Related study group"] or "None assigned"}',f'Source caveats: {paper["Source caveats"]}',
             'Scope: Research-reference knowledge. These records do not describe a live well. Reviewed means content review, not approval to operate equipment. Preserve alternatives, input requirements and source restrictions in answers.']
        for name in ['Failures','Rules','Indicators','Actions','AI Models','Q and A']:
            for r in tables[name]:
                if r['Paper ID']!=pid:continue
                if r.get('Review status')=='Rejected':continue
                count+=1
                out.append('\n---\n'+f'Knowledge record: {r["Entry ID"]}\nType: {name}')
                out.extend(f'{k}: {v}' for k,v in r.items() if k not in ['Entry ID','Paper ID'] and v!='')
                # Repeat essential source qualifications so independently retrieved records retain them.
                if 'Source caveats' not in r:out.append('Source caveats: '+paper['Source caveats'])
                out.append(f'Source report: reports/{pid}.md. PDF page references refer to the original paper, not this text file.')
        (ROOT/'knowledge'/f'{pid}.txt').write_text('\n\n'.join(out)+'\n',encoding='utf-8')
    manifest={'workbook_sha256':hashlib.sha256(BOOK.read_bytes()).hexdigest(),'tables':{n:len(r) for n,r in tables.items()},'knowledge_records':count,'rejected_rows_excluded_from_knowledge':True,'pending_rows_included_as_research_reference':True,'source_json_role':'Original extraction snapshot; does not receive workbook edits.'}
    (ROOT/'data/export_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(json.dumps(manifest,indent=2))
if __name__=='__main__':main()
