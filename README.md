# Django Tires/Magwheels Database

A django project designed to hold inventory for a tire company. Project includes both front-end and back-end scripts. The dropdown dependent data is based on a complete list of the company's product list for tires, magwheels, and accessories. Technical requirements include Java, Python, and HTML. Other programs include Google Sheets.

## Dataset

The company utilizes their own product list. 

## Features

- Multiple pages based on adding/editing/deleting transactions. Capable of session-handling for multiple transactions at once.
- JavaScript for U/X improvements and dropdown dependency.
- Python handling for back-end coding.
- HTML used for developing front-end pages.
- Excel and printing functions needed by upper management, with sales aggregation logic.

## Design

- The focus of the project is to design an application with user-friendly interfaces, to be used by company management for day-to-day transactions.
- **Transactions** Transactions can be made with adding Payment/Tire/Magwheel/Accessory models
- **Query capabilities** Users can also query based on the specified requirements, depending on a combination of date, branch, quantity, or other product-dependent fields.
- **Report Sumary** Upper management can access a report summarizing sales created based on date and location, with excel export and printing.

## Requirements
- Python 3.X
- Pandas
- django
- gspread