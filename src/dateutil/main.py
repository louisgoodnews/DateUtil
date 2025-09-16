"""
Author: Louis Goodnews
Date: 2025-07-08
"""

from datetime import datetime

from core.core import DateFormat, DateUtil


def main() -> None:
    """ """

    obj: datetime = DateUtil.now()

    print(f"Current Date and Time: {obj}")

    print(f"Formatted Date: {DateUtil.datetime_to_string(obj, DateFormat.ISO_8601)}")

    print(DateUtil.STRING)


if __name__ == "__main__":
    main()
