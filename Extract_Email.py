#!/usr/bin/env python
import re, sys
email_pattern = re.compile('([.|\w]+@(\w+[.]\w+[.|\w+])\w+)')
data = sys.stdin.read()
matches = re.findall(email_pattern, data)
emails = [match[0] for match in matches]
unique_emails = list(set(emails))
print ', '.join(unique_emails)
