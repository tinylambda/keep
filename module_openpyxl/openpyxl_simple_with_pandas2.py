import pathlib

import pandas as pd
from openpyxl import load_workbook


filepath = pathlib.Path.home().joinpath("Downloads/test14.xlsx")
workbook = load_workbook(filename=filepath)
sheet = workbook.active
data = sheet.values

cols = next(data)
data = list(data)

REVIEW_ID = "review_id"
idx = [row[REVIEW_ID] for row in data]
df = pd.DataFrame(data, index=idx, columns=cols)
