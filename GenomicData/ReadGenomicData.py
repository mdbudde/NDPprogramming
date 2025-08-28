import pandas as pd

'''
The data in this folder is downloaded from:
https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE61326
from this publication:
https://pubmed.ncbi.nlm.nih.gov/25267625/
It is cropped to include only the datatable without header/metadata.
Stored as a tab-separated file (tsv) can be loaded into excel

Additional information about the samples, noting control is medium (normal) levels of vitamin D:
#GSM1502412 = Value for GSM1502412: rat hippocampus, low vitamin D, 18 months old, marked, subject 1; src: low vitamin D_18 months old_marked
#GSM1502413 = Value for GSM1502413: rat hippocampus, low vitamin D, 18 months old, unmarked, subject 2; src: low vitamin D_18 months old_unmarked
#GSM1502414 = Value for GSM1502414: rat hippocampus, low vitamin D, 18 months old, marked, subject 3; src: low vitamin D_18 months old_marked
#GSM1502415 = Value for GSM1502415: rat hippocampus, low vitamin D, 18 months old, unmarked, subject 4; src: low vitamin D_18 months old_unmarked
#GSM1502416 = Value for GSM1502416: rat hippocampus, low vitamin D, 18 months old, marked, subject 5; src: low vitamin D_18 months old_marked
#GSM1502417 = Value for GSM1502417: rat hippocampus, low vitamin D, 18 months old, unmarked, subject 6; src: low vitamin D_18 months old_unmarked
#GSM1502418 = Value for GSM1502418: rat hippocampus, low vitamin D, 18 months old, marked, subject 7; src: low vitamin D_18 months old_marked
#GSM1502419 = Value for GSM1502419: rat hippocampus, low vitamin D, 18 months old, unmarked, subject 8; src: low vitamin D_18 months old_unmarked
#GSM1502420 = Value for GSM1502420: rat hippocampus, control, 18 months old, unmarked, subject 9; src: control_18 months old_unmarked
#GSM1502421 = Value for GSM1502421: rat hippocampus, control, 18 months old, marked, subject 10; src: control_18 months old_marked
#GSM1502422 = Value for GSM1502422: rat hippocampus, control, 18 months old, unmarked, subject 11; src: control_18 months old_unmarked
#GSM1502423 = Value for GSM1502423: rat hippocampus, control, 18 months old, marked, subject 12; src: control_18 months old_marked
#GSM1502424 = Value for GSM1502424: rat hippocampus, control, 18 months old, unmarked, subject 13; src: control_18 months old_unmarked
#GSM1502425 = Value for GSM1502425: rat hippocampus, control, 18 months old, marked, subject 14; src: control_18 months old_marked
#GSM1502426 = Value for GSM1502426: rat hippocampus, control, 18 months old, unmarekd, subject 15; src: control_18 months old_unmarkd
#GSM1502427 = Value for GSM1502427: rat hippocampus, control, 18 months old, marked, subject 16; src: control_18 months old_marked
#GSM1502428 = Value for GSM1502428: rat hippocampus, control, 18 months old, unmarked, subject 17; src: control_18 months old_unmarked
#GSM1502429 = Value for GSM1502429: rat hippocampus, high vitamin D, 18 months old, marked, subject 18; src: high vitamin D_18 months old_marked
#GSM1502430 = Value for GSM1502430: rat hippocampus, high vitamin D, 18 months old, unmarked, subject 19; src: high vitamin D_18 months old_unmarked
#GSM1502431 = Value for GSM1502431: rat hippocampus, high vitamin D, 18 months old, marked, subject 20; src: high vitamin D_18 months old_marked
#GSM1502432 = Value for GSM1502432: rat hippocampus, high vitamin D, 18 months old, unmarked, subject 21; src: high vitamin D_18 months old_unmarked
#GSM1502433 = Value for GSM1502433: rat hippocampus, high vitamin D, 18 months old, marked, subject 22; src: high vitamin D_18 months old_marked
#GSM1502434 = Value for GSM1502434: rat hippocampus, high vitamin D, 18 months old, unmarked, subject 23; src: high vitamin D_18 months old_unmarked
#GSM1502435 = Value for GSM1502435: rat hippocampus, high vitamin D, 18 months old, marked, subject 24; src: high vitamin D_18 months old_marked
#GSM1502436 = Value for GSM1502436: rat hippocampus, high vitamin D, 18 months old, marked, subject 25; src: high vitamin D_18 months old_marked
#GSM1502437 = Value for GSM1502437: rat hippocampus, high vitamin D, 18 months old, unmarked, subject 26; src: high vitamin D_18 months old_unmarked

'''


# Load the tab-delimited file
file_path = "GDS5345_sub.tsv" 
data = pd.read_csv(file_path, sep='\t')

# Display the first few rows of the data
print(data.head())

print(data.columns)