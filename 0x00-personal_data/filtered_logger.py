"""
Module for redacting sensitive fields in log messages.

This module provides the `filter_datum` function and the `RedactingFormatter` class
for secure logging.

* `filter_datum` obfuscates specified fields in a log message using regular expressions.
* `RedactingFormatter` inherits from `logging.Formatter` and automatically redacts
  sensitive fields during log message formatting.
"""

import re


def filter_datum(fields: list[str], redaction: str, message: str, separator: str) -> str:
    """
    Filters specified fields in a log message.

    This function replaces the values of specified fields in a log message with
    a provided redaction string.

    Args:
        fields: A list of strings representing fields to obfuscate.
        redaction: The replacement value for obfuscated fields.
        message: The original log message.
        separator: The character separating fields in the log message.

    Returns:
        The obfuscated log message.
    """

    pattern = r"|".join([f"{field}=.*?{separator}" for field in fields])
    return re.sub(pattern, lambda m: f"{m.group(0).split('=')[0]}={redaction}{separator}", message)


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class for obfuscating sensitive fields in log messages.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list[str]):
        """
        Initializes the formatter with a list of fields to obfuscate.

        Args:
            fields: A list of field names to redact.
        """
        super().__init__(self.FORMAT)  # Call the base class constructor
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the log record with field obfuscation.

        Args:
            record: The log record to format.

        Returns:
            The formatted log message with redacted fields.
        """

        record.message = filter_datum(self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        return super().format(record)
