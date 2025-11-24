🛒 Basic Console Shopping Cart Program

Project Overview

This project is a simple, command-line application written in Python that simulates the core functionality of a shopping cart. Users can interactively add multiple items (foods) and their corresponding prices to a list. Once the user is done, the program displays a list of all items purchased and calculates the final total cost.
Features

Interactive Input: Users are prompted sequentially to enter item names and prices.

Quit Command: Allows users to exit the item-entry loop easily by typing q.

Price Calculation: Automatically sums up all entered prices to provide a final total.

Cart Summary: Displays all items added to the cart upon exiting the input phase.

Input Validation: Includes basic error handling for non-numeric price inputs.
Technologies/Tools Used

Language: Python 3.x

Environment: Command Line Interface (CLI)

Steps to Install & Run the Project

Prerequisites

You must have Python 3.x installed on your system.

Installation

Download the shopping cart program.py file
Execution

Open your terminal or command prompt in the project directory.

Run the Python script:

shopping cart program.py


The program will guide you through entering items and prices.

Instructions for Testing

To test the program, follow the interactive prompts and verify the output:

Add Items: Enter item names (e.g., Apple, Banana) and various prices (e.g., 1.50, 0.75).

Test Total Calculation: Ensure the final displayed total is the correct sum of all prices.

Test the Quit Command: Type q (or Q) at the food input prompt to confirm the loop breaks correctly.

Test Price Validation: Try entering text (e.g., ten dollars) when prompted for the price to ensure the Invalid price entered message appears and the program allows re-entry.
