import pandas as pd
import os

years = ['2006-01', '2006-02',
         '2007-01', '2007-02',
         '2008-01', '2008-02',
         '2009-01', '2009-02',
         '2010-01', '2010-02',
         '2011-01', '2011-02',
         '2012-01', '2012-02',
         '2013-01', '2013-02',
         '2014-01', '2014-02',
         '2015-01', '2015-02',
         '2016-01', '2016-02',
         '2017-01', '2017-02',
         '2018-01', '2018-02',
         '2019-01', '2019-02',
         '2020-01', '2020-02',
         '2021-01', '2021-02']

for year in years:
    try:
        skran = pd.read_excel("data/skraning/{}.xls".format(year), encoding='utf-16')
    except FileNotFoundError:
        skran = pd.read_excel("data/skraning/{}.xlsx".format(year), encoding='utf-16')

    # Create a folder under data/skraning/csv with the same name as the excel file
    os.mkdir("data/skraning/csv/{}".format(year))

    # Loop through the sheets and save them as csv files
    for sheet in skran.sheet_names:
        # Create a folder with the same name as the excel file

        df = skran.parse(sheet)
        df.to_csv("data/skraning/csv/{}/{}.csv".format(year, sheet))
