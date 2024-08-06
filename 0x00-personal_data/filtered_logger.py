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

  pattern = r"(" + "|".join(fields) + r")=" + re.escape(separator) + r".*"
  return re.sub(pattern, r"\1=" + redaction, message)

