## Automation Script Pack (Python)

A simple Python automation tool that combines file renaming, data extraction, and email automation into one menu-driven program.

## Features
1. File Renaming Automation
Renames all files in a given folder
Adds a custom prefix with automatic numbering
Example: report_1.txt, report_2.txt, report_3.txt

2. Data Extraction (Emails & Phone Numbers)
Reads a text file
Extracts:
Email addresses
10-digit phone numbers
Removes duplicates automatically

3. Send Automated Email
Sends an email using Gmail SMTP
Uses a secure App Password
Supports custom subject and message

## Requirements

Python 3.8+
Internet connection (for email feature)
Gmail account with App Password enabled

## Libraries Used
All libraries are built-in (no installation required):

## How to Run
Save the script as automation_script.py
Open a terminal or command prompt

## Run:
python automation_script.py

Choose an option from the menu:

1. File Renaming Automation
2. Data Extraction (Emails & Phones)
3. Send Automated Email
4. Exit

Gmail App Password Setup (Required for Email)
Enable 2-Step Verification on your Google account
Go to Google Account → Security → App Passwords
Generate a password for Mail
Use that password when the script asks for it
Do NOT use your normal Gmail password
