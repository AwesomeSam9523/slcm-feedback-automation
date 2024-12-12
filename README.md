# Semester-End Feedback Automation Script
An automation script for filling out semester-end feedback on my college portal - [SLCM](https://mujslcm.jaipur.manipal.edu:122/) at [Manipal, Jaipur](https://jaipur.manipal.edu/). If you need help with a similar task for a different college, feel free to reach out to me!

## Steps to Run the Script on Your Computer
Before you try to run this on your machine, ensure that you have Python and pip installed in your environment.

_For my not so technological advanced friends (and using Windows), download [Python 3](https://www.python.org/downloads/) and [pip](https://phoenixnap.com/kb/install-pip-windows)._

### Note: For MacOS Users:
Run this in your terminal first:
```
brew install chromium
```

### For both Mac and Windows, follow these steps:

1. Clone this repository ```git clone https://github.com/AwesomeSam9523/slcm-feedback-automation.git``` (or you can [download it as a zip file from here](https://github.com/AwesomeSam9523/slcm-feedback-automation)) and open it in your terminal.

2. Update the Environment Variables File
	1. Right click the `.env` file and open it in a text editor.
	2. Update the `FIRST_NAME`, `REGISTRATION_NUMBER` and `PASSWORD` fields with your SLCM username and password respectively.

3. Install the required libraries: ```pip install -r requirements.txt```

4. Run the script
	1. Make sure you're in the slcm-feedback-automation directory in the terminal.
	2. Run the script: ```python script.py```

