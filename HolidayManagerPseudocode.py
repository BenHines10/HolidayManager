#get (as in scrape) holiday dates from 2019, 2020, 2021, 2022, 2023. 
#https://www.timeanddate.com/holidays/us/XXXX is the url for holidays, where XXXX = year
#Populate the json file with scraped holidays from said years.

#Display size of json file list for holiday count for start-up screen
#print() statements build UI:
#   1. Add a Holiday
#   2. Remove a Holiday
#   3. Save Holiday List
#   4. View Holidays
#   5. Exit

#Get user input for selected option

#add holiday:
#   get input for date
#   check validity of given date
#       if invalid, ask for new date
#   get input for holiday string
#   add to save list

#remove holiday:
#   get input for string
#   check validity of given string as existing in json file
#       if invalid, ask for new string
#       else add to remove list

#save holiday list:
#   write content in add list to json file
#   remove content in remove list from json file

#view holidays:
#   get year
#       if invalid, ask again
#   get week
#       if invalid, ask again
#   if current week == given week
#       ask if user wants to see weather
#       if yes, display weather from weather api 
#   display holidays for given week

#exit
#   if save command has not been issued and remove and add list have been modified
#       ask if changes want to be saved
#       if yes
#           execute save function
#   terminate program

