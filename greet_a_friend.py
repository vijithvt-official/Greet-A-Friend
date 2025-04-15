# 🎉 Greet A Friend
# Author: [Write Your Name]
# Date: [Write Today's Date]
# Description: Sends automated birthday greetings to your friends via email.


# -------------------------- #
# TASK-1: Import Libraries
# -------------------------- #
# ➤ Import required modules (datetime, pandas or csv, smtplib, random, os, etc.)
# Reference: 
# https://docs.python.org/3/library/datetime.html
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
# https://docs.python.org/3/library/smtplib.html


# -------------------------- #
# TASK-2: Load Birthday Data
# -------------------------- #
# ➤ Read from a CSV file and access rows and columns.
# ➤ You may use pandas or csv module.
# ➤ Add extra fields such as 'message_type' to choose from different templates.
# Reference: 
# https://realpython.com/python-csv/
# https://pandas.pydata.org/docs/user_guide/io.html#csv-text-files



# -------------------------- #
# TASK-3: Check for Today’s Birthdays
# -------------------------- #
# ➤ Use datetime to get today’s date.
# ➤ Compare with 'month' and 'day' columns in your data.
# ➤ Try to make it flexible by supporting multiple date formats.
# Reference:
# https://docs.python.org/3/library/datetime.html#datetime.date



# -------------------------- #
# TASK-4: Choose a Template
# -------------------------- #
# ➤ Load a letter from a .txt file using file I/O.
# ➤ Create multiple templates (template_1.txt, template_2.txt, etc.)
# ➤ Add a challenge: let each user have a preferred message type.
# Reference:
# https://www.w3schools.com/python/python_file_open.asp



# -------------------------- #
# TASK-5: Personalize the Message
# -------------------------- #
# ➤ Replace placeholders like [NAME], [AGE] if available.
# Reference:
# https://www.geeksforgeeks.org/python-string-replace/



# -------------------------- #
# TASK-6: Setup Email Details
# -------------------------- #
# ➤ Define sender, recipient, subject, and body of the email.
# ➤ Store email credentials in a config.env file and read securely.
# Reference:
# https://realpython.com/python-send-email/
# https://docs.python.org/3/library/os.html#os.environ



# -------------------------- #
# TASK-7: Send the Email
# -------------------------- #
# ➤ Connect to an SMTP server and send the email.
# ➤ Add retry logic and proper error handling.
# Reference:
# https://realpython.com/python-send-email/#sending-an-html-email-using-smtplib



# -------------------------- #
# TASK-8: Add Logging (Optional)
# -------------------------- #
# ➤ Keep a record of sent emails with timestamp and name.
# ➤ Add failed attempts to a separate log file.



# -------------------------- #
# TASK-9: Add Random Template (Bonus)
# -------------------------- #
# ➤ Store multiple template files and select one randomly.



# -------------------------- #
# TASK-10: Final Testing
# -------------------------- #
# ➤ Update the CSV with today’s date for testing.
# ➤ Run the script and verify functionality.



# -------------------------- #
# CHALLENGE TASKS
# -------------------------- #
# ➤ Add feature to send WhatsApp messages using Twilio (optional).
# ➤ Create a simple GUI using Tkinter or web form to add birthdays.
# ➤ Send image-based e-cards using HTML email format.


# -------------------------- #
# ✅ PROJECT COMPLETE!
# -------------------------- #
