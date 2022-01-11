## Holiday Manager

Files
-Holiday Manager sourcecode : **HolidayManager.py**<br />
-Holiday Manager pseudocode : **HolidayManagerPseudocode.py**<br />
-Starting file of holiday data : **holidays.json**<br />

The holiday manager stores and retreives holiday names and dates from an internalized list of holiday objects. On startup, all holiday names and dates from the **holidays.json** file and from [timeanddate.com](https://www.timeanddate.com/holidays/us/) from the years 2020, 2021, 2022, 2023, and 2024 will be preloaded into the holiday list.

The UI will include five options:

1. Add a Holiday
2. Remove a Holiday
3. Save Holiday List
4. View Holidays
5. Exit


Add a Holiday:<br />
&nbsp;&nbsp;&nbsp;&nbsp;Adds a holiday to the list of holidays with user-defined name and date.<br />
Remove a Holiday:<br />
&nbsp;&nbsp;&nbsp;&nbsp;Removes a holiday from the list matching a user-defined name and date.<br />
Save Holiday List:<br />
&nbsp;&nbsp;&nbsp;&nbsp;Writes the current list of holidays to **holidays.json**<br />
View Holidays<br />
&nbsp;&nbsp;&nbsp;&nbsp;Displays holidays from a user-defined year and week number (1 -52).<br />
&nbsp;&nbsp;&nbsp;&nbsp;The user is able to leave the week entry blank and the holidays from<br />
&nbsp;&nbsp;&nbsp;&nbsp;the current week and year will be displayed. When having done so, the<br />
&nbsp;&nbsp;&nbsp;&nbsp;user will also be able to input 'Y' when prompted to see a description<br />
&nbsp;&nbsp;&nbsp;&nbsp;of the recorded or predicted weather on the holiday dates.<br />
Exit<br />
&nbsp;&nbsp;&nbsp;&nbsp;Will allow the user to terminate the progam. If no write to the **holidays.json**<br />
&nbsp;&nbsp;&nbsp;&nbsp;file has been detected since the list of holidays has been modified, the user<br />
&nbsp;&nbsp;&nbsp;&nbsp;will be prompted to save. 
