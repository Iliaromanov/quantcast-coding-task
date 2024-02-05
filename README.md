# quantcast-coding-task
CLI Program to find most active cookie from input log file

### Main Program

I wrote my program in Python; the main logic of my implementation is abstracted away within the `CookieLogPraser` class/module which can be found in `cookie_log_parser.py` while the CLI program that takes input from the user and uses the `CookieLogPraser` class to obtain results for the user is found under `most_active_cookie.py`.

I avoided importing any libraries other than Pytest and sys, for testing and retrieving command line args respectively.

**Most importantly, I wrote a bash script which calls my CLI python code in order to exactly fit the sample call provided in the task description. Once at the root of this repository, my program can be called as follows:**

```
./most_active_cookie <cookie_log_file_path.csv> -d <utc_timezone>
```

(assuming the most_active_cookie bash script has been provided with execute, permissions on your machine)


### Testing

I did my testing using the PyTest testing framework. Steps to install and run my tests are as follows:

1. Install pytest: `pip install pytest` (can skip if already installed)

2. Run pytest (must be at root of repo): `pytest cookie_log_parser_test.py`