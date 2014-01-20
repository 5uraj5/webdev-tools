#!/usr/bin/env python
"""
Create html options based on stdin.

One option is generated for each line of the input. If the line is enclosed
in asterisks (*content*) an optgroup is created instead. '----' in the input
closes the optgroup.

Lines starting with '#' are included in the output as comments.

Values are checked for duplication to avoid name collisions when processing
the form.
"""


import fileinput

# checking for value collisions
values = set()


def check_collisions(value):
    if value in values:
        raise Exception('Value "%s" duplicated in options!' % value)
    else:
        values.add(value)

for line in fileinput.input():
    value = line.strip()
    if value:
        if value[0] == '#':
            print '<!-- %s -->' % value
        elif value[0] == '*' and value[-1] == '*':
            print '<optgroup label="%s">' % value[1:-1]
        elif value == '----':
            print '</optgroup>'
        else:
            check_collisions(value)
            print '<option value="%s">%s</option>' % (value, value)
    else:
        print
