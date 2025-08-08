"""
Author: Louis Goodnews
Date: 2025-07-08
"""

from datetime import date, datetime, timedelta
from enum import Enum
from typing import Any, Callable, Dict, Final, List, Literal, Optional, Union


__all__: Final[List[str]] = ["DateFormat", "DateUtil"]


class DateUtilError(Exception):
    """Base class for all DateUtil exceptions."""

    pass


class InvalidDateFormatError(DateUtilError):
    """Exception raised for invalid date formats."""

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the InvalidDateFormatError with a message.

        :param message: The error message describing the invalid date format.
        :ptype message: str

        :return: None
        :rtype: None
        """

        # Call the base class constructor with the message.
        # This ensures that the exception is initialized properly
        # and the message is set correctly for the exception.
        super().__init__(message)

        # Store the message in a Final attribute to ensure
        # it remains constant and cannot be modified.
        # This is important for maintaining the integrity of the error message.
        self.message: Final[str] = message

        # Store the name of the exception for consistency
        # and to match the expected format in the codebase.
        # This is useful for debugging and logging purposes.
        self.name: Final[str] = "InvalidDateFormatError"


class DateOutOfRangeError(DateUtilError):
    """Exception raised when a date is out of the valid range."""

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the DateOutOfRangeError with a message.

        :param message: The error message describing the out-of-range date.
        :ptype message: str

        :return: None
        :rtype: None
        """

        # Call the base class constructor with the message.
        super().__init__(message)

        # Store the message in a Final attribute to ensure
        # it remains constant and cannot be modified.
        self.message: Final[str] = message

        # Store the name of the exception for consistency
        self.name: Final[str] = "DateOutOfRangeError"


class DateConversionError(DateUtilError):
    """Exception raised for errors during date conversion."""

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the DateConversionError with a message.

        :param message: The error message describing the conversion error.
        :ptype message: str

        :return: None
        :rtype: None
        """

        # Call the base class constructor with the message.
        super().__init__(message)

        # Store the message in a Final attribute to ensure
        # it remains constant and cannot be modified.
        self.message: Final[str] = message

        # Store the name of the exception for consistency
        self.name: Final[str] = "DateConversionError"


class DateParsingError(DateUtilError):
    """Exception raised for errors during date parsing."""

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the DateParsingError with a message.

        :param message: The error message describing the parsing error.
        :ptype message: str

        :return: None
        :rtype: None
        """

        # Call the base class constructor with the message.
        super().__init__(message)

        # Store the message in a Final attribute to ensure
        # it remains constant and cannot be modified.
        self.message: Final[str] = message

        # Store the name of the exception for consistency
        self.name: Final[str] = "DateParsingError"


class DateFormatError(DateUtilError):
    """Exception raised for errors in date format."""

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the DateFormatError with a message.

        :param message: The error message describing the format error.
        :ptype message: str

        :return: None
        :rtype: None
        """

        # Call the base class constructor with the message.
        super().__init__(message)

        # Store the message in a Final attribute to ensure
        # it remains constant and cannot be modified.
        self.message: Final[str] = message

        # Store the name of the exception for consistency
        self.name: Final[str] = "DateFormatError"


class DateRangeError(DateUtilError):
    """Exception raised for errors in date range operations."""

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the DateRangeError with a message.

        :param message: The error message describing the range error.
        :ptype message: str

        :return: None
        :rtype: None
        """

        # Call the base class constructor with the message.
        super().__init__(message)

        # Store the message in a Final attribute to ensure
        # it remains constant and cannot be modified.
        self.message: Final[str] = message

        # Store the name of the exception for consistency
        self.name: Final[str] = "DateRangeError"


class DateArithmeticError(DateUtilError):
    """Exception raised for errors in date arithmetic operations."""

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the DateArithmeticError with a message.

        :param message: The error message describing the arithmetic error.
        :ptype message: str

        :return: None
        :rtype: None
        """

        # Call the base class constructor with the message.
        super().__init__(message)

        # Store the message in a Final attribute to ensure
        # it remains constant and cannot be modified.
        self.message: Final[str] = message

        # Store the name of the exception for consistency
        self.name: Final[str] = "DateArithmeticError"


class DateValidationError(DateUtilError):
    """Exception raised for errors in date validation."""

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the DateValidationError with a message.

        :param message: The error message describing the validation error.
        :ptype message: str

        :return: None
        :rtype: None
        """

        # Call the base class constructor with the message.
        super().__init__(message)

        # Store the message in a Final attribute to ensure
        # it remains constant and cannot be modified.
        self.message: Final[str] = message

        # Store the name of the exception for consistency
        self.name: Final[str] = "DateValidationError"


class DateComparisonError(DateUtilError):
    """Exception raised for errors in date comparison operations."""

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the DateComparisonError with a message.

        :param message: The error message describing the comparison error.
        :ptype message: str

        :return: None
        :rtype: None
        """

        # Call the base class constructor with the message.
        super().__init__(message)

        # Store the message in a Final attribute to ensure
        # it remains constant and cannot be modified.
        self.message: Final[str] = message

        # Store the name of the exception for consistency
        self.name: Final[str] = "DateComparisonError"


class DateLocaleError(DateUtilError):
    """Exception raised for errors related to date locale settings."""

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the DateLocaleError with a message.

        :param message: The error message describing the locale error.
        :ptype message: str

        :return: None
        :rtype: None
        """

        # Call the base class constructor with the message.
        super().__init__(message)

        # Store the message in a Final attribute to ensure
        # it remains constant and cannot be modified.
        self.message: Final[str] = message

        # Store the name of the exception for consistency
        self.name: Final[str] = "DateLocaleError"


class DateTimezoneError(DateUtilError):
    """Exception raised for errors related to date timezone settings."""

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the DateTimezoneError with a message.

        :param message: The error message describing the timezone error.
        :ptype message: str

        :return: None
        :rtype: None
        """

        # Call the base class constructor with the message.
        super().__init__(message)

        # Store the message in a Final attribute to ensure
        # it remains constant and cannot be modified.
        self.message: Final[str] = message

        # Store the name of the exception for consistency
        self.name: Final[str] = "DateTimezoneError"


class DateParsingFormatError(DateUtilError):
    """Exception raised for errors in date parsing format."""

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the DateParsingFormatError with a message.

        :param message: The error message describing the parsing format error.
        :ptype message: str

        :return: None
        :rtype: None
        """

        # Call the base class constructor with the message.
        super().__init__(message)

        # Store the message in a Final attribute to ensure
        # it remains constant and cannot be modified.
        self.message: Final[str] = message

        # Store the name of the exception for consistency
        self.name: Final[str] = "DateParsingFormatError"


class DateSerializationError(DateUtilError):
    """Exception raised for errors during date serialization."""

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the DateSerializationError with a message.

        :param message: The error message describing the serialization error.
        :ptype message: str

        :return: None
        :rtype: None
        """

        # Call the base class constructor with the message.
        super().__init__(message)

        # Store the message in a Final attribute to ensure
        # it remains constant and cannot be modified.
        self.message: Final[str] = message

        # Store the name of the exception for consistency
        self.name: Final[str] = "DateSerializationError"


class DateDeserializationError(DateUtilError):
    """Exception raised for errors during date deserialization."""

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the DateDeserializationError with a message.

        :param message: The error message describing the deserialization error.
        :ptype message: str

        :return: None
        :rtype: None
        """

        # Call the base class constructor with the message.
        super().__init__(message)

        # Store the message in a Final attribute to ensure
        # it remains constant and cannot be modified.
        self.message: Final[str] = message

        # Store the name of the exception for consistency
        self.name: Final[str] = "DateDeserializationError"


class DateParsingLocaleError(DateUtilError):
    """Exception raised for errors in date parsing locale settings."""

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the DateParsingLocaleError with a message.

        :param message: The error message describing the parsing locale error.
        :ptype message: str

        :return: None
        :rtype: None
        """

        # Call the base class constructor with the message.
        super().__init__(message)

        # Store the message in a Final attribute to ensure
        # it remains constant and cannot be modified.
        self.message: Final[str] = message

        # Store the name of the exception for consistency
        self.name: Final[str] = "DateParsingLocaleError"


class DateParsingTimezoneError(DateUtilError):
    """Exception raised for errors in date parsing timezone settings."""

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the DateParsingTimezoneError with a message.

        :param message: The error message describing the parsing timezone error.
        :ptype message: str

        :return: None
        :rtype: None
        """

        # Call the base class constructor with the message.
        super().__init__(message)

        # Store the message in a Final attribute to ensure
        # it remains constant and cannot be modified.
        self.message: Final[str] = message

        # Store the name of the exception for consistency
        self.name: Final[str] = "DateParsingTimezoneError"


class DateParsingValidationError(DateUtilError):
    """Exception raised for errors in date parsing validation."""

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the DateParsingValidationError with a message.

        :param message: The error message describing the parsing validation error.
        :ptype message: str

        :return: None
        :rtype: None
        """

        # Call the base class constructor with the message.
        super().__init__(message)

        # Store the message in a Final attribute to ensure
        # it remains constant and cannot be modified.
        self.message: Final[str] = message

        # Store the name of the exception for consistency
        self.name: Final[str] = "DateParsingValidationError"


class DateFormat(Enum):
    """
    Enum class for various date formats.
    This class provides a set of predefined date formats that can be used
    for formatting and parsing dates in a consistent manner.
    """

    # Define the date formats as class attributes.
    # Each format is represented as a string.
    ISO_8601 = "%Y-%m-%dT%H:%M:%S.%fZ"
    RFC_2822 = "%a, %d %b %Y %H:%M:%S %z"
    US_DATE = "%m/%d/%Y"
    UK_DATE = "%d/%m/%Y"
    EU_DATE = "%d.%m.%Y"
    CUSTOM_DATE = "%Y-%m-%d %H:%M:%S"

    def __str__(self) -> str:
        """
        Returns the string representation of the date format.

        :return: The date format as a string.
        :rtype: str
        """

        # This method returns the string representation of the date format.
        return self.value


class DateUtil:
    """
    A utility class for various date and time operations.
    Provides methods for date arithmetic, formatting, validation, and conversion.

    This class is designed to handle common date-related tasks in a consistent manner.
    It includes methods for calculating differences between dates, converting between
    datetime objects and strings, checking if dates are valid, and manipulating dates
    (e.g., incrementing or decrementing by days, hours, etc.).

    Attributes:
        DAY (int): The current day of the month.
        DAY_BEFORE_YESTERDAY (date): The date for the day before yesterday.
        MONTH (int): The current month.
        STRING (str): A string representation of the current date and time.
        TIME (str): The current time in HH:MM:SS format.
        TODAY (date): The current date.
        TOMORROW (date): The date for tomorrow.
        TOMORROW_NEXT (date): The date for the day after tomorrow.
        WEEK (int): The current week number of the year.
        YEAR (int): The current year.
        YESTERDAY (date): The date for yesterday.
    """

    # Define class attributes for commonly used dates.
    DAY_BEFORE_YESTERDAY: Final[date] = datetime.now().date() - timedelta(days=2)
    TODAY: Final[date] = datetime.now().date()
    TOMORROW: Final[date] = TODAY + timedelta(days=1)
    TOMORROW_NEXT: Final[date] = TODAY + timedelta(days=2)
    DAY: Final[int] = TODAY.day
    MONTH: Final[int] = TODAY.month
    WEEK: Final[int] = TODAY.isocalendar()[1]
    YEAR: Final[int] = TODAY.year
    YESTERDAY: Final[date] = TODAY - timedelta(days=1)

    TIME: Final[str] = (
        f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
    )

    STRING: str = f"year={YEAR}, month={MONTH}, day={DAY}, week={WEEK}, time={TIME}"

    @classmethod
    def calculate_difference(
        cls,
        start: datetime,
        as_: Literal[
            "days",
            "hours",
            "milisconds",
            "minutes",
            "months",
            "seconds",
            "weeks",
            "years",
        ] = "seconds",
        end: Optional[datetime] = None,
    ) -> Union[Union[float, int], timedelta]:
        """
        Calculates the difference between two dates.

        :param start: The start date as a datetime object.
        :type start: datetime
        :param emd: The end date as a datetime object (default is now).
        :type end: datetime
        :param as_: The unit to return the difference in (default is seconds). Defaults to "seconds".
        :type as_: Literal["days", "hours", "milisconds", "minutes", "months", "seconds", "weeks", "years"]

        :return: The difference between the two dates as a timedelta object.
        :rtype: Union[Union[int, float], timedelta]

        :raises DateArithmeticError: If the end date is before the start date.
        """

        # Check if the end date is provided
        if not end:
            # If the end date is not provided, set it to the current date and time.
            end = cls.now()

        # Check if the end date is before the start date
        if end < start:
            # If the end date is before the start date, raise a DateArithmeticError
            # with a message indicating that the end date cannot be before the start date.
            raise DateArithmeticError(
                "End date cannot be before start date.",
            )

        # This method calculates the difference between two dates.
        # If the start date is not provided, it defaults to the current date and time.
        result: timedelta = end - start

        # Depending on the value of 'as_', it returns the difference in the specified unit.
        if as_ == "days":
            # If 'as_' is 'days', return the difference in days.
            return result.days
        elif as_ == "hours":
            # If 'as_' is 'hours', return the difference in hours.
            return result.total_seconds() // 3600
        elif as_ == "milisconds":
            # If 'as_' is 'milisconds', return the difference in milliseconds.
            return result.total_seconds() * 1000
        elif as_ == "minutes":
            # If 'as_' is 'minutes', return the difference in minutes.
            return result.total_seconds() // 60
        elif as_ == "months":
            # If 'as_' is 'months', return the difference in months.
            # This is a simplified calculation and may not be accurate for all cases.
            return (end.year - start.year) * 12 + end.month - start.month
        elif as_ == "seconds":
            # If 'as_' is 'seconds', return the difference in seconds.
            return result.total_seconds()
        elif as_ == "weeks":
            # If 'as_' is 'weeks', return the difference in weeks.
            return result.days // 7
        elif as_ == "years":
            # If 'as_' is 'years', return the difference in years.
            return result.days // 365
        else:
            # If 'as_' is not one of the specified values, raise a ValueError.
            raise ValueError(
                f"Invalid value for 'as_': {as_}. "
                "Must be one of: 'days', 'hours', 'milisconds', 'minutes', 'seconds', 'weeks', 'years'.",
            )

    @classmethod
    def calculate_difference_in_days(
        cls,
        start: datetime,
        end: Optional[datetime] = None,
    ) -> Union[float, int, timedelta]:
        """
        Calculates the difference between two dates in days.

        :param start: The start date as a datetime object.
        :type start: datetime
        :param end: The end date as a datetime object (default is now).
        :type end: datetime

        :return: The difference between the two dates in days.
        :rtype: Union[float, int, timedelta]

        :raises DateArithmeticError: If the end date is before the start date.
        """

        # This method calculates the difference between two dates in days.
        return cls.calculate_difference(
            start=start,
            end=end,
            as_="days",
        )

    @classmethod
    def calculate_difference_in_hours(
        cls,
        start: datetime,
        end: Optional[datetime] = None,
    ) -> Union[float, int, timedelta]:
        """
        Calculates the difference between two dates in hours.

        :param start: The start date as a datetime object.
        :type start: datetime
        :param end: The end date as a datetime object (default is now).
        :type end: datetime

        :return: The difference between the two dates in hours.
        :rtype: Union[float, int, timedelta]

        :raises DateArithmeticError: If the end date is before the start date.
        """

        # This method calculates the difference between two dates in hours.
        return cls.calculate_difference(
            start=start,
            end=end,
            as_="hours",
        )

    @classmethod
    def calculate_difference_in_milliseconds(
        cls,
        start: datetime,
        end: Optional[datetime] = None,
    ) -> Union[float, int, timedelta]:
        """
        Calculates the difference between two dates in milliseconds.

        :param start: The start date as a datetime object.
        :type start: datetime
        :param end: The end date as a datetime object (default is now).
        :type end: datetime

        :return: The difference between the two dates in milliseconds.
        :rtype: Union[float, int, timedelta]

        :raises DateArithmeticError: If the end date is before the start date.
        """

        # This method calculates the difference between two dates in milliseconds.
        return cls.calculate_difference(
            start=start,
            end=end,
            as_="milisconds",
        )

    @classmethod
    def calculate_difference_in_minutes(
        cls,
        start: datetime,
        end: Optional[datetime] = None,
    ) -> Union[float, int, timedelta]:
        """
        Calculates the difference between two dates in minutes.

        :param start: The start date as a datetime object.
        :type start: datetime
        :param end: The end date as a datetime object (default is now).
        :type end: datetime

        :return: The difference between the two dates in minutes.
        :rtype: Union[float, int, timedelta]

        :raises DateArithmeticError: If the end date is before the start date.
        """

        # This method calculates the difference between two dates in minutes.
        return cls.calculate_difference(
            start=start,
            end=end,
            as_="minutes",
        )

    @classmethod
    def calculate_difference_in_months(
        cls,
        start: datetime,
        end: Optional[datetime] = None,
    ) -> Union[float, int, timedelta]:
        """
        Calculates the difference between two dates in months.

        :param start: The start date as a datetime object.
        :type start: datetime
        :param end: The end date as a datetime object (default is now).
        :type end: datetime

        :return: The difference between the two dates in months.
        :rtype: Union[float, int, timedelta]

        :raises DateArithmeticError: If the end date is before the start date.
        """

        # This method calculates the difference between two dates in months.
        return cls.calculate_difference(
            start=start,
            end=end,
            as_="months",
        )

    @classmethod
    def calculate_difference_in_seconds(
        cls,
        start: datetime,
        end: Optional[datetime] = None,
    ) -> Union[float, int, timedelta]:
        """
        Calculates the difference between two dates in seconds.

        :param start: The start date as a datetime object.
        :type start: datetime
        :param end: The end date as a datetime object (default is now).
        :type end: datetime

        :return: The difference between the two dates in seconds.
        :rtype: Union[float, int, timedelta]

        :raises DateArithmeticError: If the end date is before the start date.
        """

        # This method calculates the difference between two dates in seconds.
        return cls.calculate_difference(
            start=start,
            end=end,
            as_="seconds",
        )

    @classmethod
    def calculate_difference_in_weeks(
        cls,
        start: datetime,
        end: Optional[datetime] = None,
    ) -> Union[float, int, timedelta]:
        """
        Calculates the difference between two dates in weeks.

        :param start: The start date as a datetime object.
        :type start: datetime
        :param end: The end date as a datetime object (default is now).
        :type end: datetime

        :return: The difference between the two dates in weeks.
        :rtype: Union[float, int, timedelta]

        :raises DateArithmeticError: If the end date is before the start date.
        """

        # This method calculates the difference between two dates in weeks.
        return cls.calculate_difference(
            start=start,
            end=end,
            as_="weeks",
        )

    @classmethod
    def calculate_difference_in_years(
        cls,
        start: datetime,
        end: Optional[datetime] = None,
    ) -> Union[float, int, timedelta]:
        """
        Calculates the difference between two dates in years.

        :param start: The start date as a datetime object.
        :type start: datetime
        :param end: The end date as a datetime object (default is now).
        :type end: datetime

        :return: The difference between the two dates in years.
        :rtype: Union[float, int, timedelta]

        :raises DateArithmeticError: If the end date is before the start date.
        """

        # This method calculates the difference between two dates in years.
        return cls.calculate_difference(
            start=start,
            end=end,
            as_="years",
        )

    @classmethod
    def datetime_to_string(
        cls,
        date: datetime,
        date_format: DateFormat = DateFormat.ISO_8601,
    ) -> str:
        """
        Converts a datetime object to a string in the specified format.

        :param date: The datetime object to convert.
        :type date: datetime
        :param date_format: The format to convert the datetime to (default is "%Y-%m-%d %H:%M:%S").
        :type date_format: str

        :return: The formatted date string.
        :rtype: str
        """

        # This method converts a datetime object to a string in the specified format.
        return date.strftime(date_format.value)

    @classmethod
    def day(cls) -> int:
        """
        Returns the current day of the month.

        :return: The current day of the month as an integer (1-31).
        :rtype: int
        """

        # This method returns the current day of the month as an integer.
        return cls.now().day

    @classmethod
    def days_in_month(
        cls,
        month: int,
        year: int,
    ) -> int:
        """
        Returns the number of days in a given month of a given year.

        :param month: The month for which to get the number of days (1-12).
        :type month: int
        :param year: The year for which to get the number of days.
        :type year: int

        :return: The number of days in the specified month and year.
        :rtype: int
        """

        # This method returns the number of days in a given month of a given year.
        # It uses the datetime module to determine the last day of the month.
        return (datetime(year, month + 1, 1) - timedelta(days=1)).day

    @classmethod
    def days_in_this_month(cls) -> int:
        """
        Returns the number of days in the current month.

        :return: The number of days in the current month.
        :rtype: int
        """

        # This method returns the number of days in the current month.
        return cls.days_in_month(
            month=cls.month(),
            year=cls.year(),
        )

    @classmethod
    def decrement(
        cls,
        obj: datetime,
        what: Literal["days", "hours", "minutes", "seconds", "weeks", "years"],
        amount: int,
    ) -> datetime:
        """
        Decrements a datetime object by a specified amount of time.

        :param obj: The datetime object to decrement.
        :type obj: datetime
        :param what: The unit of time to decrement by (e.g., "days", "hours", "minutes", "seconds", "weeks", "years").
        :type what: Literal["days", "hours", "minutes", "seconds", "weeks", "years"]
        :param amount: The amount to decrement the datetime object by.
        :type amount: int

        :return: The decremented datetime object.
        :rtype: datetime
        """

        # This method decrements a datetime object by a specified amount of time.
        return cls.increment(
            obj=obj,
            what=what,
            amount=-amount,
        )

    @classmethod
    def end_of_day(cls) -> datetime:
        """
        Returns the current date with the time set to the end of the day (23:59:59).

        :return: The current date as a datetime object with time set to the end of the day.
        :rtype: datetime
        """

        # This method returns the current date with the time set to the end of the day.
        return cls.now().replace(
            hour=23,
            minute=59,
            second=59,
            microsecond=999999,
        )

    @classmethod
    def end_of_month(cls) -> datetime:
        """
        Returns the current date with the time set to the end of the month (last day of the month at 23:59:59).

        :return: The current date as a datetime object with time set to the end of the month.
        :rtype: datetime
        """

        # This method returns the current date with the time set to the end of the month.
        last_day: datetime = cls.now().replace(day=1) + timedelta(days=31)
        last_day: datetime = last_day.replace(day=1) - timedelta(days=1)

        # The last day of the month is adjusted to the last day of the month
        # by replacing the day with the last day of the month.
        # The time is set to the end of the day (23:59:59).
        # This ensures that the returned datetime object represents the last moment of the month.
        # The microsecond is set to 999999 to represent the last microsecond of the
        # last day of the month.
        return last_day.replace(
            hour=23,
            minute=59,
            second=59,
            microsecond=999999,
        )

    @classmethod
    def end_of_week(cls) -> datetime:
        """
        Returns the current date with the time set to the end of the week (Sunday at 23:59:59).

        :return: The current date as a datetime object with time set to the end of the week.
        :rtype: datetime
        """

        # This method returns the current date with the time set to the end of the week.
        # The end of the week is considered to be Sunday at 23:59:59.
        return cls.now().replace(
            hour=23,
            minute=59,
            second=59,
            microsecond=999999,
        ) + timedelta(days=(6 - cls.now().weekday()))

    @classmethod
    def end_of_year(cls) -> datetime:
        """
        Returns the current date with the time set to the end of the year (December 31st at 23:59:59).

        :return: The current date as a datetime object with time set to the end of the year.
        :rtype: datetime
        """

        # This method returns the current date with the time set to the end of the year.
        return cls.now().replace(
            month=12,
            day=31,
            hour=23,
            minute=59,
            second=59,
            microsecond=999999,
        )

    @classmethod
    def increment(
        cls,
        obj: datetime,
        what: Literal["days", "hours", "minutes", "seconds", "weeks", "years"],
        amount: int,
    ) -> datetime:
        """
        Increments a datetime object by a specified amount of time.

        :param obj: The datetime object to increment.
        :type obj: datetime
        :param what: The unit of time to increment by (e.g., "days", "hours", "minutes", "seconds", "weeks", "years").
        :type what: Literal["days", "hours", "minutes", "seconds", "weeks", "years"]
        :param amount: The amount to increment the datetime object by.
        :type amount: int

        :return: The incremented datetime object.
        :rtype: datetime
        """

        # This method increments a datetime object by a specified amount of time.
        # The 'what' parameter specifies the unit of time to increment by.
        if what == "days":
            return obj + timedelta(days=amount)
        elif what == "hours":
            return obj + timedelta(hours=amount)
        elif what == "minutes":
            return obj + timedelta(minutes=amount)
        elif what == "seconds":
            return obj + timedelta(seconds=amount)
        elif what == "weeks":
            return obj + timedelta(weeks=amount)
        elif what == "years":
            return obj.replace(year=obj.year + amount)
        else:
            raise ValueError(
                f"Invalid value for 'what': {what}. Must be one of: 'days', 'hours', 'minutes', 'seconds', 'weeks', 'years'."
            )

    @classmethod
    def is_date_in_range(
        cls,
        date: datetime,
        start: datetime,
        end: datetime,
    ) -> bool:
        """
        Checks if a given date is within a specified range.

        :param date: The date to check.
        :type date: datetime
        :param start: The start of the range.
        :type start: datetime
        :param end: The end of the range.
        :type end: datetime

        :return: True if the date is within the range, False otherwise.
        :rtype: bool

        :raises DateOutOfRangeError: If the date is not within the specified range.
        """

        # This method checks if a given date is within a specified range.
        result: bool = start <= date <= end

        # If the date is not within the range, raise a DateOutOfRangeError.
        if not result:
            # If the date is not within the range, raise a DateOutOfRangeError.
            raise DateOutOfRangeError(
                f"The date {date} is not within the range {start} to {end}.",
            )

        # If the date is within the range, return True.
        return result

    @classmethod
    def is_leap_year(
        cls,
        year: int,
    ) -> bool:
        """
        Checks if a given year is a leap year.

        :param year: The year to check.
        :type year: int

        :return: True if the year is a leap year, False otherwise.
        :rtype: bool
        """

        # This method checks if a given year is a leap year.
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @classmethod
    def is_today(cls, date: datetime) -> bool:
        """
        Checks if a given date is today.

        :param date: The date to check.
        :type date: datetime

        :return: True if the date is today, False otherwise.
        :rtype: bool
        """

        # This method checks if a given date is today.
        return date.date() == cls.today().date()

    @classmethod
    def is_tomorrow(cls, date: datetime) -> bool:
        """
        Checks if a given date is tomorrow.

        :param date: The date to check.
        :type date: datetime

        :return: True if the date is tomorrow, False otherwise.
        :rtype: bool
        """

        # This method checks if a given date is tomorrow.
        return date.date() == cls.tomorrow().date()

    @classmethod
    def is_valid_date(
        cls,
        date: datetime,
    ) -> bool:
        """
        Checks if a given date is valid.

        :param date: The date to check.
        :type date: datetime

        :return: True if the date is valid, False otherwise.
        :rtype: bool

        :raises DateValidationError: If the date is invalid.
        """

        # This method checks if a given date is valid.
        try:
            # Attempt to create a datetime object with the provided date.
            datetime(
                date.year,
                date.month,
                date.day,
            )

            # If successful, the date is valid.
            return True
        except DateValidationError:
            # If a DateValidationError is raised, the date is invalid.
            return False

    @classmethod
    def is_valid_date_format(
        cls,
        date_str: str,
        date_format: str = "%Y-%m-%d",
    ) -> bool:
        """
        Checks if a given date string is in a valid format.

        :param date_str: The date string to check.
        :type date_str: str
        :param date_format: The expected format of the date string (default is "%Y-%m-%d").
        :type date_format: str

        :return: True if the date string is in a valid format, False otherwise.
        :rtype: bool

        :raises InvalidDateFormatError: If the date string is not in the expected format.
        """

        # This method checks if a given date string is in a valid format.
        try:
            # Attempt to parse the date string using the specified format.
            datetime.strptime(
                date_str,
                date_format,
            )

            # If successful, the date string is in a valid format.
            return True
        except InvalidDateFormatError:
            # If a InvalidDateFormatError is raised, the date string is not in a valid format.
            return False

    @classmethod
    def is_yesterday(cls, date: datetime) -> bool:
        """
        Checks if a given date is yesterday.

        :param date: The date to check.
        :type date: datetime

        :return: True if the date is yesterday, False otherwise.
        :rtype: bool
        """

        # This method checks if a given date is yesterday.
        return date.date() == cls.yesterday().date()

    @classmethod
    def month(cls) -> int:
        """
        Returns the current month.

        :return: The current month as an integer (1-12).
        :rtype: int
        """

        # This method returns the current month as an integer.
        return cls.now().month

    @classmethod
    def now(cls) -> datetime:
        """
        Returns the current date and time.

        :return: The current date and time as a datetime object.
        :rtype: datetime
        """

        # This method returns the current date and time using the datetime module.
        return datetime.now()

    @classmethod
    def parse_date_string(
        cls,
        date_str: str,
        date_format: DateFormat = DateFormat.ISO_8601,
    ) -> datetime:
        """
        Parses a date string into a datetime object.

        :param date_str: The date string to parse.
        :type date_str: str
        :param date_format: The format of the date string (default is "%Y-%m-%d %H:%M:%S").
        :type date_format: str

        :return: The parsed datetime object.
        :rtype: datetime

        :raises DateParsingFormatError: If the date string cannot be parsed.
        """

        try:
            # This method parses a date string into a datetime object.
            return cls.string_to_datetime(
                date_str=date_str,
                date_format=date_format,
            )
        except ValueError as e:
            # If the date string cannot be parsed, raise a DateParsingFormatError.
            raise DateParsingFormatError(
                f"Invalid date format: {date_str}. Expected format: {date_format}.",
            ) from e

    @classmethod
    def record_runtime(
        cls,
        function: Callable[[Any], Any],
        *args: Any,
        **kwargs: Any,
    ) -> Dict[str, Union[Any, Dict[str, float]]]:
        """
        Records the runtime of a function and returns the result along with the execution time.

        :param function: The function to execute and record the runtime for.
        :type function: Callable[[Any], Any]
        :param args: Positional arguments to pass to the function.
        :param kwargs: Keyword arguments to pass to the function.

        :return: A dictionary containing the result of the function and the execution time in seconds.
        :rtype: Dict[str, Union[Any, float, int]]
        """

        start: datetime = cls.now()

        try:
            result: Optional[Any] = function(
                *args,
                **kwargs,
            )
        except Exception as e:
            raise e

        return {
            "result": result,
            "execution_time": {
                "seconds": cls.calculate_difference_in_seconds(start=start),
                "milliseconds": cls.calculate_difference_in_milliseconds(start=start),
            },
        }

    @classmethod
    def start_of_day(cls) -> datetime:
        """
        Returns the current date with the time set to midnight.

        :return: The current date as a datetime object with time set to midnight.
        :rtype: datetime
        """

        # This method returns the current date with the time set to midnight.
        return cls.now().replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )

    @classmethod
    def start_of_month(cls) -> datetime:
        """
        Returns the current date with the time set to the start of the month (first day of the month at midnight).

        :return: The current date as a datetime object with time set to the start of the month.
        :rtype: datetime
        """

        # This method returns the current date with the time set to the start of the month.
        return cls.now().replace(
            day=1,
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )

    @classmethod
    def start_of_week(cls) -> datetime:
        """
        Returns the current date with the time set to the start of the week (Monday at midnight).

        :return: The current date as a datetime object with time set to the start of the week.
        :rtype: datetime
        """

        # This method returns the current date with the time set to the start of the week.
        return cls.now().replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        ) - timedelta(days=cls.now().weekday())

    @classmethod
    def start_of_year(cls) -> datetime:
        """
        Returns the current date with the time set to the start of the year (January 1st at midnight).

        :return: The current date as a datetime object with time set to the start of the year.
        :rtype: datetime
        """

        # This method returns the current date with the time set to the start of the year.
        return cls.now().replace(
            month=1,
            day=1,
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )

    @classmethod
    def string_to_datetime(
        cls,
        date_str: str,
        date_format: DateFormat = DateFormat.ISO_8601,
    ) -> datetime:
        """
        Converts a string to a datetime object in the specified format.

        :param date_str: The date string to convert.
        :type date_str: str
        :param date_format: The format of the date string (default is "%Y-%m-%d %H:%M:%S").
        :type date_format: str

        :return: The converted datetime object.
        :rtype: datetime
        """

        try:
            # This method converts a string to a datetime object in the specified format.
            return datetime.strptime(
                date_str,
                date_format.value,
            )
        except ValueError as e:
            # If the string cannot be parsed, raise a DateParsingFormatError.
            raise DateParsingFormatError(
                f"Invalid date format: {date_str}. Expected format: {date_format}.",
            ) from e

    @classmethod
    def today(cls) -> datetime:
        """
        Returns the current date with the time set to midnight.

        :return: The current date as a datetime object with time set to midnight.
        :rtype: datetime
        """

        # This method returns the current date with the time set to midnight.
        return cls.start_of_day()

    @classmethod
    def tomorrow(cls) -> datetime:
        """
        Returns the date of tomorrow with the time set to midnight.

        :return: The date of tomorrow as a datetime object with time set to midnight.
        :rtype: datetime
        """

        # This method returns the date of tomorrow with the time set to midnight.
        return cls.today() + timedelta(days=1)

    @classmethod
    def year(cls) -> int:
        """
        Returns the current year.

        :return: The current year as an integer.
        :rtype: int
        """

        # This method returns the current year as an integer.
        return cls.now().year

    @classmethod
    def yesterday(cls) -> datetime:
        """
        Returns the date of yesterday with the time set to midnight.

        :return: The date of yesterday as a datetime object with time set to midnight.
        :rtype: datetime
        """

        # This method returns the date of yesterday with the time set to midnight.
        return cls.today() - timedelta(days=1)
