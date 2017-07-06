#import openpyxl
#wb = openpyxl.load_workbook('csv\source1.csv')
#source1 = wb.get_sheet_by_name('source1')
#wb2 = openpyxl.load_workbook('csv\source2.csv')
#source2 = wb.get_sheet_by_name('source2')
import _csv
import pandas as pd

fileone = pd.read_csv('source1.csv')
fileonegroup = fileone.groupby(['campaign_id','audience'])["impressions"].sum()
fileonegroup.to_csv("source1group.csv", index=True, header=True)

fileonegroup = pd.read_csv('source1group.csv')
filetwo = pd.read_csv('source2.csv')
merged = fileonegroup.merge(filetwo, on='campaign_id')
merged.to_csv("sourcemerged.csv", index=False)

df = pd.read_csv('sourcemerged.csv')
for i, row in enumerate(df):
    if 'purple' in row[1]:
        print(i)
