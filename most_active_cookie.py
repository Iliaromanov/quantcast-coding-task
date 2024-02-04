import sys
from CookieLogParser import CookieLogParser


def main():
    if len(sys.argv) < 3:
        print("Usage: most_active_cookie <cookie_log_file_path.csv> -d <utc_timezone>")
        sys.exit(1)

    print(f"$1 = {sys.argv[1]}, $3 = {sys.argv[2]}")


if __name__ == "__main__":
    main()