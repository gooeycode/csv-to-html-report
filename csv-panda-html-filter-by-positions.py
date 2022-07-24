import csv
import pandas as pd

#decelerations
combinedFile = pd.read_csv("C:\\Users\\Datallite\\Desktop\\python_programs\\scouting_reports\\combinedFile.csv")

fileTable = pd.DataFrame(combinedFile)

is_Striker = fileTable['position'] == 'ST'
strikersOnly = fileTable[is_Striker]
print(strikersOnly.head())

strikersOnly.to_html("strikerReport.htm")
strikersReport = combinedFile.to_html()
with open("strikerReports.html","w") as hlReport:
    hlReport.write(strikersReport)





