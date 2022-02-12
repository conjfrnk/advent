from pathlib import Path
from requests import get, HTTPError


def fetch(year, day):
    base_path = Path(__file__)
    cookie_path = Path(base_path, "cookie.txt")
    input_path = Path(base_path, daystr, "input.txt")

    if input_path.exists():
        with open(input_path) as fh:
            return fh.read()

    try:
        with open(cookie_path) as fh:
            cookies = dict(session=fh.read().strip())
    except FileNotFoundError:
        print(f"No session cookie found at path: {cookie_path}")
        raise

    url = f"https://adventofcode.com/{year}/day/{day}/input"

    response = get(url, cookies=cookies)

    try:
        response.raise_for_status()
    except HTTPError as err:
        print(f"Something went wrong: {err=}")

    aoc_input = response.text.strip()
    print("-" * 15, " START OF INPUT ", "-" * 15)
    print(aoc_input)
    print("-" * 16, " END OF INPUT ", "-" * 16)

    with open(input_path, "w") as fh:
        fh.write(aoc_input)

    return aoc_input
