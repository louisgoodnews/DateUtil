# DateUtil

DateUtil is a Python utility library for easy and efficient date and time manipulation. It provides a set of functions to parse, format, compare, and perform arithmetic on dates and times.

## Features

- Parse dates from strings in multiple formats
- Format dates and times for display
- Perform date arithmetic (add/subtract days, months, years)
- Compare dates and calculate differences
- Timezone support

## Installation

```bash
pip install dateutil
```

## Usage

```python
from dateutil import DateUtil

# Parse a date string
dt = DateUtil.string_to_datetime('2024-06-01')

# Format a date
print(DateUtil.datetime_to_string(dt, '%d/%m/%Y'))

# Add days
new_dt = DateUtil.increment("days", 7)

# Compare dates
diff = DateUtil.calculate_difference_in_days(dt, new_dt)
```

## Documentation

See the [full documentation](docs/) for detailed API usage and examples.

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License.