import pandas as pd
import dataset as dt
import unittest
from datatest import register_accessors, accepted, Invalid, validate



combinedFile = pd.read_csv("C:\\Users\\Datallite\\Desktop\\python_programs\\scouting_reports\\combinedFile.csv")

class TestReport(unittest.TestCase):
    def test_headers(self):
        validate(combinedFile.columns,
    {'first','last','idNo','position','goals','assists','gamesNo','rating'}
        )

if __name__ == '__main__':
    unittest.main()