import numpy as np
import pandas as pd
import sqlite3
import os

def load_stocks_dataframe():
    conn = sqlite3.connect("../db/stocks.db")
    cursor = conn.cursor()
    cmd = '''
    SELECT g.Date AS Date,
            g."Adj Close" AS GrowthStock_AdjClose,
            (g."Adj Close" - LAG(g."Adj Close", 1) OVER (ORDER BY g.Date))/ 
                    LAG(g."Adj Close", 1) OVER (ORDER BY g.Date) AS GrowthStock_PercentChange,

            v."Adj Close" AS ValueStock_AdjClose,
            (v."Adj Close" - LAG(v."Adj Close", 1) OVER (ORDER BY v.Date))/ 
                    LAG(v."Adj Close", 1) OVER (ORDER BY v.Date) AS ValueStock_PercentChange,

            t."Adj Close" AS Treasury10yr_AdjClose,
            (t."Adj Close" - LAG(t."Adj Close", 1) OVER (ORDER BY t.Date))/ 
                    LAG(t."Adj Close", 1) OVER (ORDER BY t.Date) AS Treasury10yr_PercentChange,
            (t."Adj Close" - LAG(t."Adj Close", 1) OVER (ORDER BY t.Date)) AS Treasury10yr_Diff,

            e.DEXCAUS AS exchange,
            (e.DEXCAUS - LAG(e.DEXCAUS, 1) OVER (ORDER BY e.Date))/ 
                    LAG(e.DEXCAUS, 1) OVER (ORDER BY e.Date) AS exchange_PercentChange,
            (e.DEXCAUS - LAG(e.DEXCAUS, 1) OVER (ORDER BY e.Date)) AS exchange_Diff,

            i.T5YIE AS inflation5yr,
            (i.T5YIE - LAG(i.T5YIE, 1) OVER (ORDER BY i.Date))/ 
                    LAG(i.T5YIE, 1) OVER (ORDER BY i.Date) AS inflation5yr_PercentChange,
            (i.T5YIE - LAG(i.T5YIE, 1) OVER (ORDER BY i.Date)) AS inflation5yr_Diff,

            c.CPIAUCSL_PC1 AS CPI,
            (c.CPIAUCSL_PC1 - LAG(c.CPIAUCSL_PC1, 1) OVER (ORDER BY c.Date))/ 
                    LAG(c.CPIAUCSL_PC1, 1) OVER (ORDER BY c.Date) AS CPI_PercentChange,
            (c.CPIAUCSL_PC1 - LAG(c.CPIAUCSL_PC1, 1) OVER (ORDER BY c.Date)) AS CPI_Diff

    FROM growth_stock g
    LEFT JOIN value_stock v
    ON g.Date = v.Date
    LEFT JOIN treasury_10yr t
    ON g.Date = t.Date
    LEFT JOIN exchange e
    ON g.Date = e.Date
    LEFT JOIN inflation_5yr i
    ON g.Date = i.Date
    LEFT JOIN CPI c
    ON g.Date = c.Date
    '''

    df = pd.read_sql_query(cmd, conn)
    df['CPI'] = df.CPI.fillna(method = 'ffill', limit = 30)
    df['CPI_PercentChange'] = df.CPI_PercentChange.fillna(method = 'ffill', limit = 30)
    df['CPI_Diff'] = df.CPI_Diff.fillna(method = 'ffill', limit = 30)
    conn.close()
    return df