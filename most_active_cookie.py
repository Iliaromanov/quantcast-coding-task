import sys
import os.path
from cookie_log_parser import CookieLogParser


def main():
    if len(sys.argv) < 3:
        print("Usage: most_active_cookie <cookie_log_file_path.csv> -d <utc_timezone>")
        sys.exit(1)

    path = sys.argv[1]
    date = sys.argv[2]
    if not os.path.exists(path):
        print(f"Path '{path}' is not a valid path. " + 
              "Try entering full path if relative path doesn't work.")
        exit(1)

    cookie_log_parser = CookieLogParser()
    cookie_log_parser.parse_csv_to_dict(path)
    most_active = cookie_log_parser.get_most_active_cookie(date)

    for cookie in most_active:
        print(cookie)


if __name__ == "__main__":
    main()