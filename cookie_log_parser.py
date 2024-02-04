from typing import List, Dict

class CookieLogParser:
    def __init__(self) -> None:
        # dict format: {"YYYY-MM-DD": {"cookie_str": int_count}}
        self.cookie_counts_by_date: Dict[str, Dict[str, int]] = {}

    def parse_csv_to_dict(self, path: str) -> Dict[str, Dict[str, int]]:
        """
        Parses the csv into self.cookie_counts_by_date dict

        returns self.cookie_counts_by_date (for testability)
        """
        self.cookie_counts_by_date.clear()
        
        with open(path, 'r') as csv_file:
            first_line = True
            for line in csv_file:
                if first_line: # ignore first line since its column names
                    first_line = False
                    continue
                cookie, date = line.split(",")

                # parsing UTC time (assuming I cant import datetime)
                day = date[:date.find("T")] 

                # updating date-to-cookie count map
                if day in self.cookie_counts_by_date:
                    if cookie in self.cookie_counts_by_date[day]:
                        self.cookie_counts_by_date[day][cookie] += 1
                    else:
                        self.cookie_counts_by_date[day][cookie] = 1
                else:
                    self.cookie_counts_by_date[day] = {cookie: 1}

        return self.cookie_counts_by_date
                

    def get_most_active_cookie(self, day: str) -> List[str]:
        """
        Prints most active cookies for given UTC date, 
          and returns them in a List
        """
        return []
