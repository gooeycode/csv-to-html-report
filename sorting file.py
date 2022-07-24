import csv
import pandas as pd

#decelerations
combinedFile = pd.read_csv("C:\\Users\\Datallite\\Desktop\\python_programs\\scouting_reports\\combinedFile.csv")

fileTable = pd.DataFrame(combinedFile)
finalTable = fileTable.sort_values(by='rating', ascending=False)
print(finalTable)

finalTable.to_html("sortedReport.htm")
sortedReport = finalTable.to_html()
with open("sortedReportFile.html","w") as finalReport:
    finalReport.write(sortedReport)