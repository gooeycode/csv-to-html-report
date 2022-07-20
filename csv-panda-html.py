import csv
import pandas as pd

#decelerations
combinedFile = pd.read_csv("C:\\Users\\Datallite\\Desktop\\python_programs\\scouting_reports\\combinedFile.csv")

fileTable = pd.DataFrame(combinedFile)

combinedFile.to_html("scoutReport.htm")
scoutingReport = combinedFile.to_html()
with open("scoutingReportFile.html","w") as htmlReport:
    htmlReport.write(scoutingReport)

print(combinedFile)




