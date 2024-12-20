This repository contains a network monitoring tool that allows you to monitor multiple destinations (IP addresses or domains). The tool has two versions:

CLI (Command-Line Interface) version
GUI (Graphical User Interface) version
Both versions of the tool allow you to check the reachability of multiple IP addresses or domains and monitor their status in real-time.

Requirements
Python 3.x
Required Python packages (can be installed via requirements.txt):
bash
Copy code
pip install -r requirements.txt
CLI Tool
The CLI version of the Ping Monitor tool is a simple command-line interface that allows you to monitor multiple destinations using a terminal.

Requirements
Python 3.x
Required Python packages (can be installed via requirements.txt):
bash
Copy code
pip install -r requirements.txt
Usage
To use the CLI version, you can either pass arguments directly when running the script or provide input during runtime if no arguments are given.

Using Arguments
You can specify destinations and a timeout value when running the script:

bash
Copy code
python cli/monitor.py --dests <destination1,destination2> --timeout <timeout>
--dests: A comma-separated list of destinations (IP addresses or domains) to monitor.
--timeout: The timeout (in seconds) before considering a destination unreachable (default is 4 seconds).
Interactive Mode
If you don't provide the destinations and timeout as arguments, the tool will prompt you to enter them interactively during runtime. You will be asked to input the destinations and timeout value manually.

Example:

bash
Copy code
python cli/monitor.py --dests google.com,example.com --timeout 4
This will start the monitoring process for google.com and example.com with a timeout of 4 seconds.

Output
The tool will display a table of destinations and their status (Reachable, Unreachable, Invalid) in real-time. The status will be updated continuously as the tool pings the destinations. If a destination becomes unreachable, a beep sound will be triggered.

GUI Tool
The GUI version of the Ping Monitor tool provides a graphical interface for monitoring destinations.

Requirements
Python 3.x
Required Python packages (can be installed via requirements.txt):
bash
Copy code
pip install -r requirements.txt
Usage
To use the GUI version, simply run the script from the terminal:

bash
Copy code
python gui/monitor.py
This will open a graphical window where you can enter the IP addresses/domains and timeout value. You can then click "Start Monitor" to begin monitoring the reachability of the provided destinations.

Example
Open the GUI by running:

bash
Copy code
python gui/monitor.py
Enter the IP addresses or domains separated by commas (e.g., google.com, example.com).

Set the timeout value (e.g., 4 seconds).

Click "Start Monitor" to begin monitoring.

Contributing
If you'd like to contribute to the development of this project, feel free to fork the repository, make changes, and submit a pull request.

