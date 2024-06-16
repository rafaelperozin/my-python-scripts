# Simple Bank System

This Python script simulates a basic banking system, allowing users to perform simple transactions such as deposits, withdrawals, and viewing their transaction history (extract). It's designed to run in a terminal and provides a simple, interactive experience for managing a virtual bank account.

## Features

- **Deposits:** Users can add funds to their balance.
- **Withdrawals:** Users can withdraw funds, with certain restrictions.
- **Extract:** Users can view their transaction history, including deposits and withdrawals, along with their current balance and the total number of transactions made.

## Usage

To use the script, simply run it in a Python environment. The script will present a menu with options to deposit (`d`), withdraw (`w`), view the extract (`e`), or quit (`q`). Follow the on-screen prompts to perform transactions or view your account extract.

## Screenshots

Here are some screenshots of the Simple Bank System in action:

<p align="center">
  <img src="https://github.com/rafaelperozin/my-python-scripts/blob/main/02.%20Simple%20Bank%20System/screenshots/withdraw-sucess-and-extract.png" width="30%" alt="Sucess withdraw + show extract" />
  <img src="https://github.com/rafaelperozin/my-python-scripts/blob/main/02.%20Simple%20Bank%20System/screenshots/success-deposit-and-extract.png" width="30%" alt="Sucess deposit + show extract" />
  <img src="https://github.com/rafaelperozin/my-python-scripts/blob/main/02.%20Simple%20Bank%20System/screenshots/invalid-option.png" width="30%" alt="Invalid options handling" />
</p>
<p align="center">
  <img src="https://github.com/rafaelperozin/my-python-scripts/blob/main/02.%20Simple%20Bank%20System/screenshots/max-num-withdraw-daily-and-extract.png" width="30%" alt="Max number of daily withdraws reached + show extract" />
  <img src="https://github.com/rafaelperozin/my-python-scripts/blob/main/02.%20Simple%20Bank%20System/screenshots/not-allowed-amounts.png" width="30%" alt="Not allowed amounts handling" />
</p>

## Rules Summary

- The system only accepts positive numbers for both deposits and withdrawals.
- The deposit amount must be greater than zero.
- Withdrawals are limited to 3 per day and cannot exceed R$ 500 per transaction.
- The system only accepts amounts with two decimal places (e.g., 123,45) or whole numbers for transactions.
- Users can view their transaction history and account balance at any time by selecting the extract option.
