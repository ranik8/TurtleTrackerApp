#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Rani Kumar (rani.kumar@duke.edu)
# Date:   Fall 2020
#--------------------------------------------------------------

#Ask user for the search date
user_date = input("Enter date to search for Sara:")

#Create a variable pointing to a data file
file_name= './data/raw/sara.txt'

#Create a file object from the file
file_object= open(file_name, 'r')


#Read contents of file into a list
line_list= file_object.readlines()

#Close the file
file_object.close()

#create two empty dictionary objects
date_dict = {}
coord_dict = {}


#Iterate through all lines in the linelist
for lineString in line_list:
    if lineString[0]=="#" or lineString[0] == 'u': continue
    #Split the string in ot a list of data items
    lineData = lineString.split()
    
    #Extract items in the list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    #Print the location of sara
    #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat}, lon:{obs_lon} on {obs_date}")
    if obs_lc in ('1','2','3'): 
        date_dict[record_id]= obs_date
        coord_dict[record_id]= (obs_lat,obs_lon)

#create empty list to hold matching keys
matching_keys = []
    

#loop through items in the date_dict,and collect keys for matching ones
for date_item in date_dict.items():
    #get the key and date of the dictionary item
    the_key, the_date= date_item
    #see if the date matches the user date
    if the_date == user_date:
        #if so, add the key to the list 
        matching_keys.append(the_key)

#reveal  locations for each key in matching keys
for matching_key in matching_keys:
        obs_lat, obs_lon = coord_dict[matching_key]
        obs_date = date_dict[matching_key]
        print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat}, lon:{obs_lon} on {obs_date}")
