import pathlib
import random

from dataclasses import dataclass
from typing import List

from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference


@dataclass
class Sale:
    quantity: int


@dataclass
class Product:
    id: str
    name: str
    sales: List[Sale]


products = []

for idx in range(1, 6):
    sales: List[Sale] = []
    for _ in range(5):
        sale = Sale(quantity=random.randrange(5, 100))
        sales.append(sale)
    product = Product(id=str(idx), name='Product %s' % idx, sales=sales)
    products.append(product)


workbook = Workbook()
sheet = workbook.active
sheet.append(['product Id', 'product name', 'month 1', 'month 2', 'month 3', 'month4', 'month 5'])
for product in products:
    data = [product.id, product.name]
    for sale in product.sales:
        data.append(sale.quantity)
    sheet.append(data)

chart = LineChart()
data = Reference(
    worksheet=sheet,
    min_row=2,
    max_row=6,
    min_col=2,
    max_col=7,
)
chart.add_data(data, titles_from_data=True, from_rows=True)
sheet.add_chart(chart, 'B8')

cats = Reference(
    worksheet=sheet,
    min_row=1,
    max_row=1,
    min_col=3,
    max_col=7,
)
chart.set_categories(cats)
chart.x_axis.title = "Months"
chart.y_axis.title = "Sales (per unit)"


filepath = pathlib.Path.home().joinpath('Downloads/test13.xlsx')
workbook.save(filepath)

