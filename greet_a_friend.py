# 🎉 Greet A Friend
# Author: [Write Your Name]
# Date: [Write Today's Date]
# Description: Sends automated birthday greetings to your friends via email.

# Task Instructions

# -------------------------- #
# TASK-1: Import Libraries
# -------------------------- #
# Import the required Python modules. You will need the following:
# datetime: To get the current date.
# csv or pandas: To read data from a CSV file.
# smtplib: For sending the email.
# random: For randomly selecting templates.
# os: For handling environment variables for secure credentials storage.

# References:
# datetime: https://docs.python.org/3/library/datetime.html
# csv module: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
# smtplib module: https://docs.python.org/3/library/smtplib.html

# -------------------------- #
# TASK-2: Load Birthday Data
# -------------------------- #
# Read the birthday data from a CSV file.
# The CSV file should have columns like: Name, Email, Birthday, and MessageType.
# Example CSV format:
# Example CSV format:
# Name, Email, Birthday, MessageType
# John, john@example.com, 1990-06-15, template_1

# Reference: 
# https://realpython.com/python-csv/
# https://pandas.pydata.org/docs/user_guide/io.html#csv-text-files



# -------------------------- #
# TASK-3: Check for Today’s Birthdays
# -------------------------- #
# Use datetime to get today’s date and match it with the Birthday column in your data.
# Make sure your code supports multiple date formats, e.g., YYYY-MM-DD, MM/DD/YYYY, etc.

# Reference:
# https://docs.python.org/3/library/datetime.html#datetime.date



# -------------------------- #
# TASK-4: Choose a Template
# -------------------------- #
# Load a birthday greeting template from a .txt file.
# You can create multiple templates (e.g., template_1.txt, template_2.txt).
# Each user will have a MessageType field in the CSV which determines which template to use.

# Reference:
# https://www.w3schools.com/python/python_file_open.asp



# -------------------------- #
# TASK-5: Personalize the Message
# -------------------------- #
# Use placeholders in the template files like [NAME], [AGE], [BIRTHDAY].
# Replace these placeholders with the corresponding values from the CSV for each user.

# Reference:
# https://www.geeksforgeeks.org/python-string-replace/



# -------------------------- #
# TASK-6: Setup Email Details
# -------------------------- #
# Use the smtplib module to send emails. Store your email credentials (e.g., SMTP server login) securely in a .env file.
# Example .env file:
# EMAIL_USER=your-email@example.com
# EMAIL_PASSWORD=your-email-password
# Read these credentials using os.environ.

# Reference:
# https://realpython.com/python-send-email/
# https://docs.python.org/3/library/os.html#os.environ



# -------------------------- #
# TASK-7: Send the Email
# -------------------------- #
# Set up the email details: sender, recipient, subject, and body.
# Ensure proper error handling for invalid email addresses, network failures, etc.
# Retry logic is recommended in case sending fails.

# Reference:
# https://realpython.com/python-send-email/#sending-an-html-email-using-smtplib



# -------------------------- #
# TASK-8: Add Logging (Optional)
# -------------------------- #
# Log each email sent with timestamp and recipient name.
# Create a separate log for failed attempts



# -------------------------- #
# TASK-9: Add Random Template (Bonus)
# -------------------------- #
# Create multiple templates and randomly choose one for each user when sending greetings.



# -------------------------- #
# TASK-10: Final Testing
# -------------------------- #
# ➤ Update the CSV with today’s date for testing.
# ➤ Run the script and verify functionality.



# -------------------------- #
# CHALLENGE TASKS
# -------------------------- #
# Send WhatsApp Messages Using Twilio (Optional): Send greetings via WhatsApp using Twilio API.
# Create a simple GUI using Tkinter or web form to add birthdays.Create a Simple GUI with Tkinter (Optional): Allow the user to add birthdays through a simple form.
# Send Image-Based E-cards using HTML Email (Optional): Attach an image-based e-card and send it in HTML format.➤ Send image-based e-cards using HTML email format.


# -------------------------- #
# ✅ PROJECT COMPLETE!
# -------------------------- #
