# 🎉 Greet a Friend Project 

## Objective
Create a Python program that sends birthday wishes automatically via email.

## Instructions
This folder contains a starter Python file broken down into **tasks**. Each section is labeled as `TASK-1`, `TASK-2`, ..., with hints and reference links. You are expected to complete the code section by section.

### Steps to Follow:
1. Import necessary libraries.
Begin by importing the required modules like datetime, pandas, smtplib, and others.

2. Read birthday data from a CSV file.
Store the birthday data in a CSV file with fields like Name, Email, Birthday, and MessageType.

3. Check if today matches any birthday.
Use datetime to check if today is a birthday from the CSV.

4. Choose a letter template and personalize it.
Based on the MessageType from the CSV, load and personalize the email template by replacing placeholders like [NAME], [AGE], etc.

5. Send the birthday wish via email.
Use smtplib to send the personalized email. Ensure proper error handling and use environment variables to securely store email credentials.

### Tools You May Need
- [datetime module](https://docs.python.org/3/library/datetime.html)
- [pandas](https://pandas.pydata.org/)
- [smtplib](https://docs.python.org/3/library/smtplib.html)
- [file I/O](https://www.w3schools.com/python/python_file_open.asp)

> 💡 Try to complete each task on your own before referring to external resources.

## Bonus Challenges
- Randomly choose from multiple templates: Add multiple birthday message templates and select one randomly for each user.
- Log sent emails: Keep a record of each sent email with a timestamp and the recipient's name in a log file.
- Create a simple GUI to input birthday data.
Use Tkinter or another library to build a graphical user interface (GUI) for adding and viewing birthday data.

## Helpful Links and Resources
- [How to Read and Write CSV Files in Python](https://realpython.com/python-csv/)
- [Sending Emails with Python](https://realpython.com/python-send-email/)
- [Python Environment Variables](https://realpython.com/python-dotenv/)
- [Using pandas for Data Manipulation] (https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html)

### Project Structure Example
- CSV file (birthdays.csv): Contains columns like Name, Email, Birthday, and MessageType.

- Template files (template_1.txt, template_2.txt): 
    Example of a template:
    Happy Birthday, [NAME]!
    Wishing you a wonderful year ahead. You are now [AGE] years old! 🎉

- Python Code (greet_friend.py):
    The main Python script that implements the logic.