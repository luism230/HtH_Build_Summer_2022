import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

top5000_data = pandas.read_csv("Finding-an-Interesting-Dataset/Top5000.csv")

print (top5000_data)