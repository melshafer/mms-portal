# File: format_output.py
# Melanie Shafer, 2015

import extract_data
import config

def get_assignment_number(assignment_text):
  for s in assignment_text:
    if s.isdigit():
      return s

current_assignments_num = get_assignment_number(extract_data.current_assignments)
missing_assignments_num = get_assignment_number(extract_data.missing_assignments)

message = """
MMS Portal Grade Update for {0}

{1} currently has {2} open assignments with upcoming due dates.

There are {3} missing assignments with past due dates.
""".format(config.student_name, config.student_name.split()[0], current_assignments_num, missing_assignments_num)
