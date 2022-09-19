import pandas as pd
import wbdata
import datetime


def retrieveData():
    date = datetime.datetime(2018, 1, 1)
    # GDP per capita (current US$)
    data_x = wbdata.get_data("NY.GDP.PCAP.CD", data_date=date, pandas=True)
    # Unemployment, total (% of total labor force) (modeled ILO estimate)
    data_y = wbdata.get_data("SL.UEM.TOTL.ZS", data_date=date, pandas=True)
    data = pd.concat([data_x, data_y], axis=1)
    # Drop NaNs
    data = data.dropna(axis=0, how='any')
    # Write to .csv file
    data_df = pd.DataFrame({"GDP": data_x, "UNEMPLOYMENT": data_y})
    data_df.to_csv("data.csv", index=False)

    data.columns = ["GDP", "UNEMPLOYMENT"]
    data_x = data["GDP"].tolist()
    data_y = data["UNEMPLOYMENT"].tolist()

    return data_x, data_y
