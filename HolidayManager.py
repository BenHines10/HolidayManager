import datetime
import calendar
import json
from bs4 import BeautifulSoup
import requests
import re
import json
import os

#Holds an instance of a holiday with name and date
class Holiday:

    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __str__(self):
        return str(self.name) + ", " + str(self.date)

# -------------------------------------------
# The HolidayList class acts as a wrapper and container for the list of holidays.
# --------------------------------------------
class HolidayList:

    def __init__(self):
       self.innerHolidays = []

    #Adds a holiday object to the list of holidays
    def addHoliday(self, holidayObj):
        if type(holidayObj) == Holiday:
            self.innerHolidays.append(holidayObj)
            print("Added " + str(holidayObj))

    #Returns a holiday object according to the name and date arguments
    def findHoliday(self, holidayName, date):
        for i in self.innerHolidays:
            if type(i) == Holiday:
                if i.name == holidayName and i.date == date:
                    return i

    #Removes a holiday object from the passed list of holidays according to name and date arguments 
    def removeHoliday(self, holidayName, date):
        failure = True
        for i in self.innerHolidays:
            if type(i) == Holiday:
                if i.name == holidayName and i.date == date:
                    self.innerHolidays.remove(i)
                    print("Success:\n" + str(i) + " removed from the holiday list.")
                    failure = False
        if failure:
            print("Error:\n" + str(holidayName) + ", "  + str(date) + " not found.")

    #Creates and adds a holiday object populated with name and date given from read json file in directory
    def read_json(self, filelocation):
        try:
            with open(filelocation, 'r') as f:
                d = json.load(f)
            for i in d['Holidays']:
                self.addHoliday(Holiday(i['Name'], str(i['Date'])))
        except:
            print("Error reading from holidays.json")   

    #Writes the list of holidays to json file in directory
    def save_to_json(self, filelocation):
        try:
            listOfDictionaries = []
            OuterDict = {}
            for i in self.innerHolidays:
                listOfDictionaries.append({'Name': i.name, 'Date': i.date})
            OuterDict.update({'Holidays':listOfDictionaries})
            with open(filelocation, 'w') as f:
                json.dump(OuterDict, f, indent = 4)
        except:
            print("Error saving to holidays.json")
    
    # Used to get the date from the initial page for holidays where the date is displayed, for example, 'Jan 1, 2020'
    def convertDateStringToDateObject(self, dateString, year): 
        monthString = dateString[0:3]
        year = year
        month = 0
        day = 0
        date = None
        if monthString == "Jan":
            month = 1
        elif monthString == "Feb":
            month = 2
        elif monthString == "Mar":
            month = 3
        elif monthString == "Apr":
            month = 4
        elif monthString == "May":
            month = 5
        elif monthString == "Jun":
            month = 6
        elif monthString == "Jul":
            month = 7
        elif monthString == "Aug":
            month = 8
        elif monthString == "Sep":
            month = 9
        elif monthString == "Oct":
            month = 10
        elif monthString == "Nov":
            month = 11
        elif monthString == "Dec":
            month = 12
        try:
            day = int(dateString[4:].strip()) 
        except:
            print("Couldn't convert dateString day to int.")
        
        try:
            date = datetime.date(year, month, day)
        except:
            print("Couldn't create date object for dateString to date object conversion.")
        
        return date

    def scrapeHolidays(self):
        yearList = [2020, 2021, 2022, 2023, 2024]
        pageString = "https://www.timeanddate.com/holidays/us/"
        try:
            for h in range(len(yearList)):
                page = requests.get(pageString + str(yearList[h]))
                soup = BeautifulSoup(page.content, "html.parser")
                bodyContent = soup.find_all("tr", id = re.compile("^tr"))
                previousHoliday = ''
                for i in bodyContent:
                    #If the current holiday name differs from the last, print it. Else, ignore it.
                    if previousHoliday != i.find('a').text:
                        name = i.find('a').text
                        dateString = i.find('th', {'class':'nw'}).text
                        date = self.convertDateStringToDateObject(str(dateString), yearList[h])
                        # add holiday object with name, date for i-th element to innerHolidays list
                        # date has to be a string because json doesn't understand date objects apparently
                        self.innerHolidays.append(Holiday(name, str(date)))
                    previousHoliday = i.find('a').text
        except:
            print("timeanddate.com is not reachable.")    

    def numHolidays(self):
        return len(self.innerHolidays)
        # Return the total number of holidays in innerHolidays
    
    def filter_holidays_by_week(self, year, week_number):
        holidaysInWeek = []
        g = lambda date: date if datetime.date(date.year, date.month, date.day).isocalendar()[1] == week_number else False
        for i in self.innerHolidays:
            # Date is a string for json purposes, so we need to extract fragments from the date string to build a date object. 
            date = datetime.date(int(i.date[:4]), int(i.date[5:7]), int(i.date[8:10]))
            if date.year == year:
                if g(date) != False:
                        holidaysInWeek.append(i)
        return holidaysInWeek

    #Displays holidays in a week for when the function is executed
    def displayHolidaysInWeek(self, holidayList, week, year):
        holidayList = self.filter_holidays_by_week(year, week)
        if len(holidayList) == 0:
            print("No holidays found with given parameters.")
        else:
            for i in holidayList:
                print(i)
        
        def __str__():
            returnString = ""
            for i in holidayList:
                returnString += str(i) + "\n"
            return returnString

    def getWeather(self, weekNumber, year):
            timeMachineURL = "https://community-open-weather-map.p.rapidapi.com/onecall/timemachine"
            forcastURL = "https://community-open-weather-map.p.rapidapi.com/forecast"

            headers = {
                'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
                'x-rapidapi-key': "52ec862f17msh375f4fc19dd50dep1691c4jsna4169f9d831a"
                }
            
            #Get holidays for the week
            holidayList = self.filter_holidays_by_week(year, weekNumber)
            try:
                #Using /timemachine for past weather
                for i in holidayList:
                    date = datetime.date(int(i.date[:4]), int(i.date[5:7]), int(i.date[8:10]))
                    #if the date in consideration is today or earlier, get weather description
                    if date <= date.today():
                        uDate = calendar.timegm(date.timetuple())
                        querystring = {"lat":"37.774929","lon":"-122.419418","dt":str(uDate)}
                        response = requests.request("GET", timeMachineURL, headers=headers, params=querystring)
                        #Convert response string to dictionary
                        weather = json.loads(response.text)
                        weather = weather['hourly'][0].get("weather")[0]['description']
                        print(str(i) + " - " + str(weather))
                    else:
                        #get future weather with this call
                        uDate = calendar.timegm(date.timetuple())
                        querystring = {"q":"san francisco,us"}
                        response = requests.request("GET", forcastURL, headers=headers, params=querystring)
                        weather = json.loads(response.text)
                        #look through all weather data for matching dates and get weather for holiday
                        for j in weather['list']: 
                            APIDate = datetime.datetime.utcfromtimestamp(j.get("dt"))
                            if str(APIDate)[:10] == i.date[:10]:
                                weather = j['weather'][0].get("description")
                                print(str(i) + " - " + str(weather))
                                break
            except:
                print("Weather API is not reachable.")

    #Returns holidays with date corresponding to current week. User can choose to view weather for holidays.
    def viewCurrentWeek(self):
        todaysWeekNumber =  datetime.date.today().isocalendar().week
        todaysYear = datetime.date.today().year
        holidayList = self.filter_holidays_by_week(todaysYear, todaysWeekNumber)

        userInput = input("Do you want to see the weather? (Y/N): ")
        if userInput.strip().upper() == "Y":
            self.getWeather(todaysWeekNumber, todaysYear)
        else:
            self.displayHolidaysInWeek(holidayList, todaysWeekNumber, todaysYear)

        def __str__():
            returnString = ""
            for i in holidayList:
                returnString += str(i) + "\n"
            return returnString

def main():
    script_directory = os.path.dirname(os.path.abspath(__file__)) + "/holidays.json"
    
    #with open(script_directory, 'w') as f:
    #    print("Created holidays.json file.")

    listOfHolidays = HolidayList()
    listOfHolidays.read_json(script_directory)
    listOfHolidays.scrapeHolidays()
    unsavedChanges = 0

    print("\nHoliday Management\n==================")
    print("There are " + str(listOfHolidays.numHolidays()) + " holidays stored in the system.")

    menuLoop = True
    while(menuLoop):        
        print("\nHoliday Menu\n==============")
        print("1. Add a Holiday")
        print("2. Remove a Holiday")
        print("3. Save Holiday List")
        print("4. View Holidays")
        print("5. Exit")

        userInput = input("Input a number from menu (1 - 5): ")
        #Add a Holiday
        if userInput.strip() == '1':
            name = input("Input holiday name: ")
            dateInvalid = True
            while(dateInvalid):
                dateYear = input("Input date year: ")
                dateMonth = input("Input date month: ")
                dateDay = input("Input date day: ")
                # check if input is valid date
                try:
                    date = datetime.date(int(dateYear), int(dateMonth), int(dateDay))
                    dateInvalid = False
                    listOfHolidays.addHoliday(Holiday(name, str(date)))
                    unsavedChanges += 1
                except:
                    print("Date invalid. Try again.")

        #Remove a holiday
        elif userInput.strip() == '2':
            name = input("Input name of holiday to remove: ")
            dateInvalid = True
            while(dateInvalid):
                dateYear = input("Input date year: ")
                dateMonth = input("Input date month: ")
                dateDay = input("Input date day: ")
                # check if input is valid date
                try:
                    date = datetime.date(int(dateYear), int(dateMonth), int(dateDay))
                    dateInvalid = False
                    listOfHolidays.removeHoliday(name, str(date))
                    unsavedChanges += 1
                except:
                    print("Date invalid. Try again.")

        #Save Holiday List
        elif userInput.strip() == '3':
            userInput = input("Are you sure you want to save your changes? (Y/N): ")
            if userInput.strip().upper()[:1] == "Y":  
                listOfHolidays.save_to_json(script_directory)
                print("Success\nYour changes have been saved.")
                unsavedChanges = 0
            else:
                print("Canceled:\nHoliday list file save canceled.")
        #View Holidays
        elif userInput.strip() == '4':
            #Get Year
            inputInvalid = True
            while(inputInvalid):
                year = input("Which year?: ")
                try:
                    year = int(year)
                    inputInvalid = False
                except:
                    print("Input cannot be parsed as integer. Try again.")
            #Get Week
            inputInvalid = True
            while(inputInvalid):   
                week = input("Which week? (1 - 52, blank for current week): ")
                if week == None or week == '\n' or week == '':
                    inputInvalid = False
                    listOfHolidays.viewCurrentWeek()
                else:
                    try:
                        week = int(week)
                        listOfHolidays.displayHolidaysInWeek(listOfHolidays, week, year)
                        inputInvalid = False
                    except:
                        print("Input cannot be parsed as integer. Try again.") 
        #Exit
        elif userInput.strip() == '5':
            userInput = input("Are you sure you want to exit? (Y/N): ")
            if userInput.strip().upper()[:1] == 'Y':   
                if unsavedChanges != 0:
                    userInput = input("Your changes will be lost. (Y/N)")
                    if userInput.strip().upper()[:1] == 'Y':
                        print("Goodbye!")
                        menuLoop = False
                else:
                    print("Goodbye!")
                    menuLoop = False
        else:
            print("Input not recognized. Try again.")

if __name__ == "__main__":
    main();



