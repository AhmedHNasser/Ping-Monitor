# To handle different arguments `dests` and `timeout`
import argparse

# To ping destinations
import ping3

# To wait a bit before ping destinations again
import time

# To clear the screen befroe printing the table
import os

# To print the table
import prettytable

# Global variables
# Hold all destinations in string format, separated by comma
dests = None

# How much time the app needs to stop before consider the destination unreachable
timeout = None

parser = argparse.ArgumentParser(description="CLI tool to monitor multiple destinations.")
parser.add_argument("--dests", help="Destinations to be monitored, seperated by , (comma)")
parser.add_argument("--timeout", help="How much time the app needs to stop before consider the destination unreachable.")

args = parser.parse_args()

# Handle the `dests` argument
if hasattr(args, "dests") is True and args.dests is not None:
    dests  = args.dests # String, dests seperated by comma

    # List
    dests = dests.split(",")

# Handle the `timeout` argument
if hasattr(args, "timeout") is True and args.timeout is not None:
    try:
        timeout = int(args.timeout)

        if timeout < 0:
            timeout = 4
    except:
        timeout = 4

# Check if the user didn't pass the destinations
if dests is None:
    while True:
        user_input = input("Enter the IP Addresses/Domains to monitor seperated by , - comma - (Type quit to terminate the app): ")

        if user_input.strip() == "quit":
            print("The app is about to be terminated.")
            time.sleep(2)
            exit()

        if len(user_input.strip()) <= 0:
            print("Enter at least one valid destination")
            continue

        dests = user_input.split(",")
        break

# Check if the user didn't pass the timeout
if timeout is None:
    while True:
        user_input = input("Enter the timeout value in seconds - default is 4 - (Type quit to terminate the app): ")

        if user_input.strip() == "quit":
            print("The app is about to be terminated.")
            time.sleep(2)
            exit()

        try:
            timeout = int(user_input)

            if timeout < 0:
                timeout = 4
        except:
            print("Enter a valid timeout value - integer -")
            continue

        break

try:
    table = prettytable.PrettyTable(align="l")

    table.field_names = ["Destinations", "Status"]

    for dest in dests:
        dest = dest.strip()

        table.add_row([dest, "Pinging"])

    print(table)

    print("Press CTRL + C to stop the process.")

    make_beep = False

    while True:
        # Clear before adding new rows
        table.clear_rows()

        for dest in dests:
            dest = dest.strip()
            status = "Unknown"

            """
            # Dest is invalid => None
            # Dest is unreachable => False
            """
            ping_result = ping3.ping(dest, timeout=timeout)

            if isinstance(ping_result, float) is True:
                status = "Reachable"
            elif ping_result is None:
                status = "Invalid"
            else:
                status = "Unreachable"
                make_beep = True

            table.add_row([dest, status])

        os.system("clear")

        print(table)

        print("Press CTRL + C to stop the process.")

        if make_beep is True:
            os.system("play -nq -t alsa synth 0.5 sine 300")
            make_beep = False

        time.sleep(3)

except KeyboardInterrupt:
    print("The app is about to be terminated.")
    time.sleep(1)
    exit()

save_results = input("Do you want to save the last monitoring results to a file (Y/N): ")
if save_results.upper() == "Y":
    file_name = input("Enter the file name: ")
    try:
        with open(file_name, "w+") as file:
            file.write(str(table))
        print(f"Monitoring results saved to '{file_name}' successfully.")
    except Exception as e:
        print(f"Error saving the file: {e}")