#!/usr/bin/env python3
"""
Module for filtering log messages.

This module provides a function `filter_datum` that obfuscates specified fields
in a log message using regular expressions.

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
