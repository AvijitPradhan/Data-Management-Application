from pyspark.sql.functions import col, expr

PositionDetails = spark.read.csv('/Users/app/in/PositionDetails.csv', sep=',', inferSchema=True, header=True)
Instrument_details = spark.read.csv('/Users/app/in/Instrument_details.csv', sep=',', inferSchema=True, header=True)

joined_df = PositionDetails.join(Instrument_details, "ID")

new_df = joined_df.withColumn("total_price", expr("Quantity * `Unit Price`")) \
    .select("ID", "InstrumentID", "ISIN", "Quantity", "total_price")

new_df = new_df.withColumnRenamed("InstrumentID", "PositionID")

new_df.show()


new_df.write.csv('/Users/app/out/PositionReport.csv', header=True)

"""
A DataFrame is a data structure that organizes data into a 2-dimensional table of rows and columns
"""

import pandas as pd
  
df = pd.DataFrame(PositionReport.csv,'r+')
  
# displaying the DataFrame
display(df)
  
# fetching the number of rows and columns
rows = len(df.axes[0])
cols = len(df.axes[1])
  
# displaying the number of rows and columns
print("Rows: " + str(rows))
print("Columns: " + str(cols))

"""
This will give the count of rows and column in the dataframe
"""
