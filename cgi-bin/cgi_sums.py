#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

print("Content-type: text/plain")
print()
# print("Your job is to make this work")
form = cgi.FieldStorage()
values = form.getlist('operand')
print('Did you request Sum-Thing?')
print('The sum of the {} values is {}'.format(len(values), sum(map(int, values))))

