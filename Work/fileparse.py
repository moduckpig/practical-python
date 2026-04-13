# fileparse.py
#
# Exercise 3.3
import csv
def parse_csv(lines,select=None,types=None,has_headers=True,delimiter=',',silence_error=True):
    '''
    将csv文件解析为记录列表，每条记录是一个字典
    '''
    if select and not has_headers:
        raise RuntimeError('select文件需要列头')
    rows = csv.reader(lines,delimiter=delimiter)
    header = next(rows) if has_headers else []
    if select:
       indices = [header.index(colname) for colname in select]
       header = select
    records = []
    for rowcount,row in enumerate(rows,1):
        if not row:
           continue
        if has_headers and select:
            row = [row[i] for i in indices]
        if types:
            try:
                row = [funC(val) for funC,val in zip(types,row)]
            except ValueError:
                if not silence_error:
                   print(f'第{rowcount}列:无法转化{row}')
                   print(f'第{rowcount}列：原因：无效的整数字面量:' '')
                continue
               
        if has_headers:
            record = dict(zip(header, row))
        else:
            record = (row)
        records.append(record)
    return records