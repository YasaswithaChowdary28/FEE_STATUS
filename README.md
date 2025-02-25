# FEE_STATUS
## Overview

This is a simple fee management system that allows an admin to manage user fee statuses and send email notifications to users who have pending or cleared fees.

## Features

Admin authentication with OTP verification.

Ability to update user fee payment statuses.

Automatic email notifications to users with pending fees.

Automatic email notifications to users who have cleared their fees.

## Requirements

Ensure you have the following dependencies installed before running the project:

Python 3.x

Email service for sending OTP and notifications

Required external modules: feepending, feepaid, and otp

## File Structure

fee-management-system/
│── main.py          # Main script for admin login and management
│── feepending.py    # Module for sending emails to fee pending users
│── feepaid.py       # Module for sending emails to fee cleared users
│── otp.py           # Module for sending OTP verification
│── README.md        # Project documentation
