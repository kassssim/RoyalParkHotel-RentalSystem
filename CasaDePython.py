# ============================================================
# Royal Park Hotel @ UNITEN - Sustainable Room Rental System
# ============================================================

from datetime import datetime, date, timedelta
import time
import sys
import os


# ── Step 1: Room type selection ──────────────────────────────
def room_choice():
    # Loop until a valid room type, back, or exit is chosen
    while True:
        print("\nSelect Room Type:")
        print("1. Single Room")
        print("2. Double Room")
        print("3. Deluxe Room")
        print("4. Suite Room\n")
        print("B. Back to Previous Menu")
        print("0. Exit to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        # Handle navigation shortcuts
        if choice == '0':
            return 'exit'
        elif choice.lower() == 'b':
            return 'back'

        # Validate and return numeric room choice
        try:
            choice_int = int(choice)
            if choice_int == 1:
                print("\nYou inserted number 1, Single Room.")
                return choice_int
            elif choice_int == 2:
                print("\nYou inserted number 2, Double Room.")
                return choice_int
            elif choice_int == 3:
                print("\nYou inserted number 3, Deluxe Room.")
                return choice_int
            elif choice_int == 4:
                print("\nYou inserted number 4, Suite Room.")
                return choice_int
            else:
                print("\nError: Please enter a number from 1-4 only.")
        except ValueError:
            print("\nError: Please type a valid number or option.")


# ── Step 2: User category selection (Student or Public) ──────
def user_category():
    # Loop until a valid category, back, or exit is chosen
    while True:
        print("\nAre you a Student or Public?")
        print("1. Student")
        print("2. Public\n")
        print("B. Back to Previous Menu")
        print("0. Exit to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        # Handle navigation shortcuts
        if choice == '0':
            return 'exit'
        elif choice.lower() == 'b':
            return 'back'

        # Validate and return category
        try:
            category = int(choice)
            if category == 1:
                print("\nYou choose Uniten Student as option.")
                return category
            elif category == 2:
                print("\nYou choose Public as option.")
                return category
            else:
                print("\nError: Please enter 1 or 2.")
        except ValueError:
            print("\nError: Please type a valid number or option.")


# ── Step 3: Check-in date input ──────────────────────────────
def checkin_date():
    # Loop until a valid future date, back, or exit is entered
    while True:
        date_str = input("\nEnter check-in date (DD/MM/YYYY) or 'B' for Back, '0' for Exit: ").strip()

        # Handle navigation shortcuts
        if date_str == '0':
            return 'exit'
        elif date_str.lower() == 'b':
            return 'back'

        # Parse date and ensure it's at least tomorrow
        try:
            input_date = datetime.strptime(date_str, "%d/%m/%Y").date()
            today = date.today()

            if input_date <= today:
                print("\nError: Check-in date must be from tomorrow onwards.")
            else:
                print(f"\nCheck-in date: {date_str}")
                return date_str
        except ValueError:
            print("\nError: Please enter a valid date in DD/MM/YYYY format (example: 01/06/2025).")


# ── Step 4: Number of nights input ───────────────────────────
def nights_count():
    # Loop until a valid positive integer, back, or exit is entered
    while True:
        choice = input("\nEnter number of nights to stay (or 'B' for Back, '0' for Exit): ").strip()

        # Handle navigation shortcuts
        if choice == '0':
            return 'exit'
        elif choice.lower() == 'b':
            return 'back'

        # Validate and return number of nights
        try:
            nights = int(choice)
            if nights > 0:
                print(f"\nYou choose {nights} night(s) as the option.")
                return nights
            else:
                print("\nError: Needs to be at least 1 night.")
        except ValueError:
            print("\nError: Please type a valid number.")


# ── Helper: Return nightly price based on room and category ──
def price_lookup(room, category):
    # Student (1) gets discounted rates; Public (2) pays standard rates
    if category == 1:
        if room == 1: return 50
        elif room == 2: return 75
        elif room == 3: return 100
        elif room == 4: return 150
    else:
        if room == 1: return 80
        elif room == 2: return 120
        elif room == 3: return 150
        elif room == 4: return 200


# ── Helper: Return room type label from room number ──────────
def room_name(room):
    if room == 1: return "Single Room"
    elif room == 2: return "Double Room"
    elif room == 3: return "Deluxe Room"
    elif room == 4: return "Suite Room"


# ── Display booking summary and return total cost ────────────
def display_summary(room, category, nights, checkin, checkout):
    # Resolve human-readable labels and compute total
    rname     = room_name(room)
    price     = price_lookup(room, category)
    total     = price * nights
    cat_label = "Student" if category == 1 else "Public"

    print("\n========== Rental Details ==========")
    print(f"Room Type        : {rname}")
    print(f"User Category    : {cat_label}")
    print(f"Check-in Date    : {checkin}")
    print(f"Check-out Date   : {checkout}")
    print(f"Number of Nights : {nights}")
    print(f"Price per Night  : RM{price}")
    print(f"Total Cost       : RM{total}")
    print("=====================================")

    return total


# ── Handle cash payment and print receipt ────────────────────
def handle_payment(total, room, category, nights, checkin, checkout):
    balance_due = total

    print("\nPlease continue your payment.")
    print("(System accepts notes: RM1, RM5, RM10, RM50, RM100)")

    # Keep accepting notes until balance is fully covered
    while balance_due > 0:
        print(f"\nTotal amount you need to pay: RM{balance_due}")

        try:
            note = int(input("Choose note to insert (1, 5, 10, 50, 100): RM"))

            if note in [1, 5, 10, 50, 100]:
                # Ask how many of this note the user is inserting
                try:
                    quantity = int(input(f"How many RM{note} notes?: "))
                    if quantity > 0:
                        payment = note * quantity
                        balance_due = balance_due - payment
                        print(f"\nYou inserted RM{payment} in total.")
                    else:
                        print("Error: Quantity must be at least 1.")
                except ValueError:
                    print("Error: Please enter a valid quantity number.")
            else:
                print("\nNote: System only accepts RM1, RM5, RM10, RM50, and RM100.")
        except ValueError:
            print("\nError: Please type a valid number.")

    print("\nPayment completed!")

    # Calculate and show change if overpaid
    if balance_due < 0:
        change = balance_due * -1 # Alternative: can use change = abs(balance_due), will get same result anyway
        print(f"Balance to be returned: RM{change}")
    else:
        print("Balance to be returned: RM0")

    # Print final receipt summary
    display_summary(room, category, nights, checkin, checkout)

    # Closing reminders and thank-you message
    print("\nThank you for booking the Room using Royal Park Hotel @ Uniten Rental System")
    print("Towels will only be changed upon request from the customer.")
    print("The lowest temperature that can be set on the Aircond is 21 degrees.")
    print("Thank you for supporting a greener community!\n")


# ── Main program entry point ──────────────────────────────────
def main():
    # ASCII art assets for the intro screen
    uniten_logo = r"""
           __________________________________________
          /                                          \
         |   _    _  _   _  ___  _____  ____  _   _   |
         |  | |  | || \ | ||_ _||_   _||  __|| \ | |  |
         |  | |  | ||  \| | | |   | |  | |_  |  \| |  |
         |  | |__| || |\  | | |   | |  |  _| | |\  |  |
         |   \____/ |_| \_||___|  |_|  |____||_| \_|  |
         |                                            |
         |         UNIVERSITI TENAGA NASIONAL         |
          \                                          /
           \________________________________________/
"""

    hotel_banner = r"""
      .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.

  ____     ___   __   __     _      _           ____       _      ____    _  __ 
 |  _ \   / _ \  \ \ / /    / \    | |         |  _ \     / \    |  _ \  | |/ / 
 | |_) | | | | |  \ V /    / _ \   | |         | |_) |   / _ \   | |_) | | ' /  
 |  _ <  | |_| |   | |    / ___ \  | |___      |  __/   / ___ \  |  _ <  | . \  
 |_| \_\  \___/    |_|   /_/   \_\ |_____|     |_|     /_/   \_\ |_| \_\ |_|\_\ 
                                                                                
  _   _    ___    _____   _____   _             __ _        _   _   _   _   ___   _____   _____   _   _  
 | | | |  / _ \  |_   _| | ____| | |           / _` |      | | | | | \ | | |_ _| |_   _| | ____| | \ | | 
 | |_| | | | | |   | |   |  _|   | |          | (_| |      | | | | |  \| |  | |    | |   |  _|   |  \| | 
 |  _  | | |_| |   | |   | |___  | |___        \__, |      | |_| | | |\  |  | |    | |   | |___  | |\  | 
 |_| |_|  \___/    |_|   |_____| |_____|       |___/        \___/  |_| \_| |___|   |_|   |_____| |_| \_| 

      .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
"""
    first_run = True

    # ── Main menu loop ───────────────────────────────────────
    while True:
        if first_run:
            # First launch: play full animated intro
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n")

            # Slide-down animation for UNITEN logo
            for line in uniten_logo.strip('\n').split('\n'):
                sys.stdout.write(line + '\n')
                sys.stdout.flush()
                time.sleep(0.08)

            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')

            # Slide-down animation for hotel banner
            for line in hotel_banner.strip('\n').split('\n'):
                sys.stdout.write(line + '\n')
                sys.stdout.flush()
                time.sleep(0.05)

            # Typewriter animation for subtitle text
            subtitle = "\n   This is Sustainable Room Rental Management System for Royal Park Hotel @ UNITEN Putrajaya\n\n"
            for char in subtitle:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.015)

            first_run = False
        else:
            # Returning from a booking: skip animation, just reprint banner
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\n{hotel_banner.strip('\n')}")
            print("\n   This is Sustainable Room Rental Management System for Royal Park Hotel @ UNITEN Putrajaya\n")

        # Main menu options
        print("1. Start New Booking")
        print("2. Exit The Program")

        start = input("\nEnter choice: ").strip()
        if start == '2':
            print("\nGoodbye!\n")
            break
        elif start != '1':
            print("Invalid choice. Please enter 1 or 2.\n")
            time.sleep(1)
            continue

        # ── Booking wizard: 4 steps with back/exit support ──
        step = 1
        room = category = checkin = nights = checkout = None

        while step <= 4:
            if step == 1:
                # Step 1: Choose room type
                room = room_choice()
                if room == 'exit' or room == 'back':
                    print("\nReturning to Main Menu...\n")
                    time.sleep(1)
                    break
                step += 1

            elif step == 2:
                # Step 2: Choose user category
                category = user_category()
                if category == 'exit':
                    print("\nReturning to Main Menu...\n")
                    time.sleep(1)
                    break
                elif category == 'back':
                    step -= 1
                else:
                    step += 1

            elif step == 3:
                # Step 3: Enter check-in date
                checkin = checkin_date()
                if checkin == 'exit':
                    print("\nReturning to Main Menu...\n")
                    time.sleep(1)
                    break
                elif checkin == 'back':
                    step -= 1
                else:
                    step += 1

            elif step == 4:
                # Step 4: Enter number of nights; compute checkout date
                nights = nights_count()
                if nights == 'exit':
                    print("\nReturning to Main Menu...\n")
                    time.sleep(1)
                    break
                elif nights == 'back':
                    step -= 1
                else:
                    checkin_dt  = datetime.strptime(checkin, "%d/%m/%Y").date()
                    checkout_dt = checkin_dt + timedelta(days=nights)
                    checkout    = checkout_dt.strftime("%d/%m/%Y")
                    step += 1

        # ── Post-booking: show summary and handle payment ────
        if step > 4:
            total = display_summary(room, category, nights, checkin, checkout)
            handle_payment(total, room, category, nights, checkin, checkout)

            # Ask user what to do after completing a booking
            while True:
                print("-" * 45)
                print("1. Return to Main Menu")
                print("2. Exit Program")
                end_choice = input("\nEnter choice: ").strip()

                if end_choice == '1':
                    print("\nReturning to Main Menu...\n")
                    time.sleep(1)
                    break
                elif end_choice == '2':
                    print("\nGoodbye!\n")
                    return
                else:
                    print("\nInvalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()