# Program to launch a specified process and periodically collect data about it

- CPU usage (percent);
- Memory consumption: Resident Set Size and Virtual Memory Size;
- Number of file descriptors.

Collected data will be stored on the disk (data.txt). Each line represents a Json object which allows automated parsing.

### Run the program with two mandatory arguments:
- Path to the executable file for the process;
- Time interval between data collection iterations.

E.g. `python main.py /usr/lib/firefox/firefox 1`

**Language:** Python

**OS:** Ubuntu 20.04.4 LTS