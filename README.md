<h1 align="center">Casa De Python</h1>

<p align="center">
  A terminal room booking system for Royal Park Hotel @ UNITEN Putrajaya.<br>
  Pick a room, enter your dates, pay with cash notes, get a receipt.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.12%2B-3776AB?logo=python&logoColor=white" alt="Python 3.12+">
  <img src="https://img.shields.io/badge/dependencies-none-brightgreen" alt="No dependencies">
  <img src="https://img.shields.io/badge/course-CMPF144-orange" alt="CMPF144">
</p>

## Walkthrough

<!--
  Add the video here. GitHub cannot play YouTube inside a README, so use a clickable thumbnail:

  [![Watch the walkthrough](images/thumbnail.png)](https://youtu.be/YOUR_VIDEO_ID)

  You can also drag a small .mp4 (under 10 MB) into the GitHub README editor and it will host the file for you.
-->

## About

Casa De Python was built by group ScubaSolver for CMPF144 (Introduction to Problem Solving and Basic Computer) at Universiti Tenaga Nasional (UNITEN).

The program walks a guest through a booking one step at a time, checks every input, and takes payment in cash notes. It also prints a few eco reminders at the end (towel reuse, aircond limit), which ties into the project's SDG 11 theme. Nothing is saved between runs.

## Features

- Step-by-step booking with Back (`B`) and Exit to Main Menu (`0`) at each step
- Four room types with separate Student and Public rates
- Input checks that ask again instead of crashing
- Cash payment in RM1, RM5, RM10, RM50 and RM100 notes, with change
- Booking summary and receipt

## Getting started

You need Python 3.12 or newer. There is nothing to install, the program only uses the standard library.

```bash
python CasaDePython.py
```

On Linux or macOS, use `python3` if `python` is not found.

## How a booking works

1. Choose a room type.
2. Choose Student or Public.
3. Enter the check-in date as `DD/MM/YYYY`. It must be tomorrow or later.
4. Enter the number of nights.
5. Check the summary, then pay. The check-out date is worked out for you.

Back on the first step returns to the main menu, since there is nothing before it.

### Prices per night

| Room   | Student | Public |
|--------|---------|--------|
| Single | RM50    | RM80   |
| Double | RM75    | RM120  |
| Deluxe | RM100   | RM150  |
| Suite  | RM150   | RM200  |

### Example

A student books a Double room for 3 nights from 15/01/2027 and pays with two RM100 notes and one RM50 note.

```
========== Rental Details ==========
Room Type        : Double Room
User Category    : Student
Check-in Date    : 15/01/2027
Check-out Date   : 18/01/2027
Number of Nights : 3
Price per Night  : RM75
Total Cost       : RM225
=====================================

Total amount you need to pay: RM225
Choose note to insert (1, 5, 10, 50, 100): RM100
How many RM100 notes?: 2

You inserted RM200 in total.

Total amount you need to pay: RM25
Choose note to insert (1, 5, 10, 50, 100): RM50
How many RM50 notes?: 1

You inserted RM50 in total.

Payment completed!
Balance to be returned: RM25
```

## Project files

```
CasaDePython.py                 the program
CasaDePython_Documentation.pdf  assignment report
README.md
```

The report covers the problem analysis, IPO chart, pseudocode, flow chart, screenshots, a description of each function, and the SDG 11 reflection.

## Limitations

- Bookings are not stored. Closing the program clears everything.
- There is no room availability check, so the same room can be booked twice for the same dates.
- Payment is simulated. No real money or payment service is involved.

## Team

**ScubaSolver**

<!--
  Put the selfies in an images/ folder, then replace each comment below with an image tag, for example:
  <img src="images/harith.jpg" width="140" alt="Harith">
-->

| Muzh |
| Hakim |
| Haiman |
| Iz |

|:------:|:-----:|:------:|:--:|

<!-- Optional group selfie: <img src="images/group.jpg" width="500" alt="ScubaSolver"> -->
