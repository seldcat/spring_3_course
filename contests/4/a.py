import calendar
import sys
from datetime import datetime


def days_until_birthday(current_date: datetime, birth_date: datetime) -> int:
    current_year = current_date.year
    if birth_date.month == 2 and birth_date.day == 29:
        if not calendar.isleap(current_year):
            next_birthday = birth_date.replace(day=1, month=3, year=current_year)
        else:
            next_birthday = birth_date.replace(year=current_year)
        if next_birthday < current_date:
            if calendar.isleap(current_year + 1):
                next_birthday = birth_date.replace(year=current_year + 1)
            else:
                next_birthday = next_birthday.replace(day=1, month=3, year=current_year + 1)
    else:
        next_birthday = birth_date.replace(year=current_year)
        if next_birthday < current_date:
            next_birthday = next_birthday.replace(year=current_year + 1)
    return (next_birthday - current_date).days


def main() -> None:
    lines: list[str] = [line.strip() for line in sys.stdin]

    today: datetime = datetime.strptime(lines[0].split()[2], '%d.%m.%Y')

    remaining_days: list[int] = []
    for line in lines[1:]:
        remaining_days.append(days_until_birthday(today, datetime.strptime(line, '%d.%m.%Y')))

    print(min(remaining_days))


if __name__ == '__main__':
    main()
