## Holiday Manager

Files
-Holiday Manager sourcecode : **HolidayManager.py**
-Holiday Manager pseudocode : **HolidayManagerPseudocode.py**
-Starting file of holiday data : **holidays.json**

The holiday manager stores and retreives holiday names and dates from an internalized list of holiday objects. On startup, all holiday names and dates from the **holidays.json** file and from [timeanddate.com](https://www.timeanddate.com/holidays/us/) from the years 2020, 2021, 2022, 2023, and 2024 will be preloaded into the holiday list.

The UI will include five options:

1. Add a Holiday
2. Remove a Holiday
3. Save Holiday List
4. View Holidays
5. Exit


Add a Holiday:
    Adds a holiday to the list of holidays with user-defined name and date.
Remove a Holiday:
    Removes a holiday from the list matching a user-defined name and date.
Save Holiday List:
    Writes the current list of holidays to **holidays.json**
View Holidays
    Displays holidays from a user-defined year and week number (1 -52).
    The user is able to leave the week entry blank and the holidays from
    the current week and year will be displayed. When having done so, the
    user will also be able to input 'Y' when prompted to see a description
    of the recorded or predicted weather on the holiday dates.
Exit
    Will allow the user to terminate the progam. If no write to the **holidays.json**
    file has been detected since the list of holidays has been modified, the user
    will be prompted to save. 
