#!/usr/bin/env python3
"""
Module for filtering log messages.
"""

import re

def filter_datum(fields, redaction, message, separator):
  """Filters specified fields in a log message.

  Args:
    fields: A list of fields to obfuscate.
    redaction: The replacement value for obfuscated fields.
    message: The original log message.
    separator: The character separating fields in the log message.

  Returns:
    The obfuscated log message.
  """

  pattern = '|'.join([f'{field}=.*?{separator}' for field in fields])
  return re.sub(pattern, lambda m: f'{m.group(0).split("=")[0]}={redaction}{separator}', message)

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
