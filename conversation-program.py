from sys import argv

script, user = argv
prompt = '> '

print "Hi {}, this script is {}".format(user, script)
print "Can I ask you something about your food preference?"
can_ask = raw_input(prompt)
c
if can_ask == 'yes':
    print "How do you like your steak? (rare, medium or well done)"
    steak = raw_input(prompt)
    print "So, {}, you like your steak {}.".format(user, steak)
else:
    print "Gee, my bad."
