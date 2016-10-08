#Header: I don't care if it's clutter, I like the way it makes the code
#look in terminal.
print ""; print "=" * 30; print ""; print "DISCOURAGEMENT CALCULATOR v1.0"; print ""
print "=" * 30; print ""

#Intro for program:
print """
This program was built to help my wife and me to decide if it would really be
worth it to go out and eat or not.  Sometimes it is easy to justify a simple
$20 meal, but the Discouragement Calculator quickly reveals that those
small meals add up to some big bucks.
"""

#User Input for bill total:
print "What was the total of your bill?"
total = float(input("> $"))

#User Input for number of diners:
print "How many people were on the bill?"
diners = int(input("> "))

#Formulas for figuring out costs.
average_per_diner = total / diners
total_per_day = average_per_diner * 3
total_per_week = total_per_day * 7
house_cost = total_per_week * diners

#Outputs for Discouragement:
print ""
print "The average cost of this meal per diner was: $%.2f" % average_per_diner
print ""
print "If every diner spent this much on breakfast, lunch, & dinner,",
print "It would cost them: $%.2f per day" % total_per_day
print ""
print "If every diner spent that much money on every meal for seven days,",
print "This is how much it would cost them to eat: $%.2f" % total_per_week
print ""
print "If everyone on the bill lives in the same house, this is how much"
print "they would spend on groceries every week: $%.2f" % house_cost
print ""

#Footer break:
print ""; print "=" * 30; print ""; print "   CONJURED_BY: K1llj0y616"; print ""
print "=" * 30; print ""
