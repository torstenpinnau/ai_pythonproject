import pandas as pd
from pyweb import pydom
from pyodide.http import open_url
from pyscript import display
from js import console
#import io
#import requests

title = "Pandas (and basic DOM manipulation)"
page_message = "This example loads a remote CSV file into a Pandas dataframe, and displays it."
#url = "https://raw.githubusercontent.com/datasets/airport-codes/master/data/airport-codes.csv"
url = "https://raw.githubusercontent.com/torstenpinnau/pythonproject/main/AusApparalSales4thQrt2020.csv"

pydom["title#header-title"].html = title
pydom["a#page-title"].html = title
pydom["div#page-message"].html = page_message
pydom["input#txt-url"][0].value = url

def log(message):
    # log to pandas dev console
    print(message)
    # log to JS console
    console.log(message)

g = 'https://raw.githubusercontent.com/torstenpinnau/ai_pythonproject/main/AusApparalSales4thQrt2020.csv'
#def kein(event):
pydom["div#pandas-output-inner"].html = ""
TextFileReader = pd.read_csv(open_url(g), skipinitialspace=True, chunksize=5)
#display(TextFileReader, target="pandas-output-inner", append="False")

dfList = []
for df in TextFileReader:
    df1 = df[['State', 'Sales']]
    df4 = df1.groupby(['State'], as_index=False).sum()
    dfList.append(df4)

#print(dfList)
df2 = pd.concat(dfList,sort=False)
df3 = df2.groupby(['State'], as_index=False).sum()

formatted_products = df3.copy()
formatted_products['Sales'] = formatted_products['Sales'].apply(lambda x: '{:,.0f}'.format(x))

display(formatted_products, target="pandas-output-inner", append="False")
#print(formatted_products)
