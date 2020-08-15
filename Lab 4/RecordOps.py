# Author:		Logan Hammond; lhammond12@student.umuc.edu
# Source File:  RecordOps.py
# Description:  
# IDE:			AWS Cloud9

import json
import numpy as np
import pandas as pd
import re

class RecordOps:
    """Loads and formats customer data from local file. 

    Attributes:
        f_name_series:  list of customer first names that will form a pd series.  
        l_name_series:  list of customer last names that will form a pd series.  
        zip_series:     list of customer zipcodes that will form a pd series. 
        phone_series:   list of customer phone numbers that will form a pd
                        series. 
    """

    f_name_series = []
    l_name_series = []
    zip_series =    []
    phone_series =  []
    
    def loadData(self):
        """Loads customer data from local json. 
        """

        with open("Lab4/data.json") as json_file:
            try:
                data = json.load(json_file)
                for r in data["records"]:
                    record = [r["f_name"], r["l_name"], r["zipcode"], 
                              r["phone"]]
                    self.f_name_series.append(record[0])
                    self.l_name_series.append(record[1])
                    self.zip_series.append(record[2])
                    self.phone_series.append(record[3])
            except (ValueError, KeyError, TypeError):
                print("\n\tJSON format error.")
        print("\n\tJSON data loaded.")

    def formatData(self):
        """Parses data from local json and formats it. 
        """

        # Format f_name series. 
        # If name contains whitespace or numbers; exclude it.  
        i = 0
        for name in self.f_name_series: 
            if(re.search(r"\s", name) or re.search(r"\d", name)): 
                self.f_name_series[i] = ""
            i += 1
        self.f_name_series = pd.Series(self.f_name_series)

        # Format l_name series.
        # If name contains whitespace or numbers; exclude it. 
        i = 0
        for name in self.l_name_series: 
            if(re.search(r"\s", name) or re.search(r"\d", name)): 
                self.l_name_series[i] = ""
            i += 1
        self.l_name_series = pd.Series(self.l_name_series)

        # Format zipcode series.
        # If zip contains whitespace or characters excluding hyphens; exclude 
        # it. 
        i = 0
        for ele in self.zip_series:
            if(re.search(r"\s", ele) or re.search(r"[a-zA-Z]", ele)):
                self.zip_series[i] = ""
            i += 1
        # If zip is not exactly 5, 9, or 10 in length; exclude it. 
        i = 0
        for ele in self.zip_series:
            if not len(ele) == 5 and not len(ele) == 9 and not len(ele) == 10:
                self.zip_series[i] = ""
            i += 1
        # If zip contains 9 characters; add a hyphen to seperate to {5}-{4}
        i = 0
        for ele in self.zip_series:
            if len(ele) == 9 and not ele[5] is "-":
                new_ele = ele[:5] + "-" + ele[5:]
                self.zip_series[i] = new_ele
            i += 1
        self.zip_series = pd.Series(self.zip_series)
        
        # Format phone series. 
        # If number does not have exactly 10 digits; exclude it. 
        i = 0
        for ele in self.phone_series: 
            test_num = ele.replace("-", "")
            if not len(test_num) == 10:
                self.phone_series[i] = ""
            i += 1
        # If number does not follow {3}-{3}-{4} format; format it. 
        i = 0
        for ele in self.phone_series:
            if len(ele) == 10:
                new_ele = ele[:3] + "-" + ele[3:6] + "-" + ele[6:10]
                self.phone_series[i] = new_ele
            i += 1
        self.phone_series = pd.Series(self.phone_series)

    def printData(self):
        """Concatenates series of customer data and prints dataframe to user. 
        """

        print()
        df = pd.concat([self.f_name_series, self.l_name_series, 
                        self.zip_series, self.phone_series], axis=1)
        df.columns = ["First", "Last", "Zip", "Phone"]
        print(df)
        print()

def main():
    """Initializes class and displays customer data to user. 
    """

    rops = RecordOps()
    rops.loadData()
    rops.formatData()
    rops.printData()
    pass

if __name__ == "__main__":
    main()
