# GoogleMailAccountCheck

A simple way to check if a Google Gmail Account exists. This script allows to use a word list to run a bulk check. This script does not send any email. This script does not require you to create a REST or other API app. 

Requirements:

Python 3+

Requests library

Run:

Download the google.py script
Download the "names" file

Set permissions to include execute (*inux: chmod +x google.py)
Execute google.py (./google.py)

Search for specific accounts:

Edit the "names" file. 

	One potential account name canidate per line.
	Example:
		johndoe
		johndoe1
		john.doe
		...
Save file

Execute google.py (./google.py)


