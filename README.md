# Guide

The **Keylogger** folder cotains the compiled version of the keylogger that relies on its dependencies which are also inside the folder. There is a file called **logger.exe**, when this is ran from with inside the folder on the target machine, it will run in the backgroudna and start keylogging the keystrokes and some hardware information about the target machine.

Next, every minute the keylogger will send the data stored in the log file to the discord server based on the webhook URL provided.
