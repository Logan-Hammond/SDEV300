# Author:		Logan Hammond; lhammond12@student.umuc.edu
# Source File:  LogAnalyzer.py
# Description:  Script which analyzes log of website and creates file 
#               "analyzed_logs.txt" which contains a human-readable analysis 
#               of the file. 
# IDE:			AWS Cloud9

from collections import Counter
from datetime import datetime, timedelta
from ip2geotools.databases.noncommercial import DbIpCity

log_list             = [] # List of each individual log.   
ip_list              = [] # List of every unique ip address in log. 
timestamp_delta_list = [] # List of each unique ip and the change in time 
                          # between its first and last occurance. 
latlong_list         = [] # List of latitudes and longitudes. 
ip_count_delta_loc_list  = [] # List of each ip and its relevant data. 
dt_format = "%Y-%m-%d %H:%M:%S.%f"

# Create a list of each individual log, and each unique ip address. 
with open("Lab8/log.txt", "r+") as lf:
    for log in lf:
        date_time, ip_addr = log.split("\t")
        ip_addr = ip_addr.replace("\n", "")
        log_list.append([date_time, ip_addr])
        if ip_addr not in ip_list: 
            ip_list.append(ip_addr)

# Count the number of times and time delta between first and last occurance of
# each unique ip address. 
for unique_ip in ip_list:
    unique_ip_count = 0
    timestamp_list = []
    for log in log_list:
        if unique_ip in log:
            unique_ip_count += 1
            timestamp_list.append(log[0])
    dt_start = datetime.strptime(timestamp_list[0], dt_format)
    dt_end = datetime.strptime(timestamp_list[-1], dt_format)
    dt_delta_mins = int((dt_end - dt_start).total_seconds() / 60)
    
    # Get lat/long of each unique ip address. 
    response = DbIpCity.get(unique_ip, api_key="free")
    lat_long = "{}/{}".format(response.latitude, response.longitude)
    
    ip_count_delta_loc_list.append([unique_ip, unique_ip_count, dt_delta_mins
                                  , lat_long])

# Write noteworthy elements of ip_count_delta_loc_list to human readable file. 
with open("Lab8/analyzed_logs.txt", "w+") as af:
    return_str = ""
    for ele in ip_count_delta_loc_list:
        if ele[1] > 10 and ele[2] <= 5:
            return_str = """\
{} had {} failed login attempts in a {} minute period.
{} has a lat/long of {}.\
            """.format(ele[0], ele[1], ele[2], ele[0], ele[3])
            af.write("{}\n\n".format(return_str))
    if not return_str:
        af.write("Nothing to report.")
    

print("IP count list")
for ip in ip_count_delta_loc_list:
    print(ip)