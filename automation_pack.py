import os
import re
import smtplib
import getpass
from email.message import EmailMessage

def rename_files():
    try:
        folder = input("Enter folder path: ").strip()
        if not os.path.isdir(folder):
            print("Folder does not exist.")
            return

        prefix = input("Enter new file name prefix: ").strip()
        files = os.listdir(folder)

        if not files:
            print("No files found in folder.")
            return

        count = 1
        for file in files:
            old_path = os.path.join(folder, file)
            if os.path.isfile(old_path):
                ext = os.path.splitext(file)[1]
                new_name = f"{prefix}_{count}{ext}"
                new_path = os.path.join(folder, new_name)
                os.rename(old_path, new_path)
                count += 1

        print("Files renamed successfully.")

    except Exception as e:
        print(f"Error: {e}")

def extract_data():
    try:
        file_path = input("Enter text file path: ").strip()
        if not os.path.isfile(file_path):
            print("File not found.")
            return

        with open(file_path, "r") as file:
            content = file.read()

        emails = re.findall(
            r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", content
        )
        phones = re.findall(r"\b\d{10}\b", content)

        print("\nEmails Found:")
        for email in set(emails):
            print(email)

        print("\nPhone Numbers Found:")
        for phone in set(phones):
            print(phone)

    except Exception as e:
        print(f"Error: {e}")

def send_email():
    try:
        sender_email = input("Enter sender email: ").strip()
        sender_password = getpass.getpass("Enter APP password: ")
        receiver_email = input("Enter receiver email: ").strip()
        subject = input("Enter email subject: ").strip()
        message_body = input("Enter email message: ").strip()

        msg = EmailMessage()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.set_content(message_body)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print("Email sent successfully.")

    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Use Gmail APP PASSWORD.")
    except smtplib.SMTPConnectError:
        print("Connection error. Check internet.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        print("\n=== AUTOMATION SCRIPT PACK ===")
        print("1. File Renaming Automation")
        print("2. Data Extraction (Emails & Phones)")
        print("3. Send Automated Email")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            rename_files()
        elif choice == "2":
            extract_data()
        elif choice == "3":
            send_email()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
