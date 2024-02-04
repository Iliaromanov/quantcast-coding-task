import pytest
import os.path

from cookie_log_parser import CookieLogParser

DATA_DIR = "test_data"
cookie_log_parser = CookieLogParser()


def test_parse_csv_to_dict_empty():
    parsed = cookie_log_parser.parse_csv_to_dict(
        os.path.join(DATA_DIR, "empty.csv"))
    assert(parsed == {})

def test_parse_csv_to_dict_cookie_count_greater_than_one():
    parsed = cookie_log_parser.parse_csv_to_dict(
        os.path.join(DATA_DIR, "cookie_count_greater_than_one.csv"))
    assert(parsed == {'2018-12-08': {'SAZuXPGUrfbcn5UA': 3}})

def test_parse_csv_to_dict_sample():
    parsed = cookie_log_parser.parse_csv_to_dict(
        os.path.join(DATA_DIR, "sample.csv"))
    assert(parsed == {
        '2018-12-09': {
            'AtY0laUfhglK3lC7': 2,
            'SAZuXPGUrfbcn5UA': 1,
            '5UAVanZf6UtGyKVS': 1
        },
        '2018-12-08': {
            'SAZuXPGUrfbcn5UA': 1,
            '4sMM2LxV07bPJzwf': 1,
            'fbcn5UAVanZf6UtG': 1
        },
        '2018-12-07': {
            '4sMM2LxV07bPJzwf': 1
        }
    })

