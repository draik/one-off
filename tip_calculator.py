#! /usr/bin/python2

MEAL = float(input("Cost of the meal w/ tax: "))

TIP_10 = round(MEAL * 0.10,2)
TOT_10 = round(MEAL * 1.10,2)
TIP_15 = round(MEAL * 0.15,2)
TOT_15 = round(MEAL * 1.15,2)
TIP_20 = round(MEAL * 0.20,2)
TOT_20 = round(MEAL * 1.20,2)

print ("10%: $" + str("%.2f" % TIP_10) + " TOTAL: $" + str("%.2f" % TOT_10))
print ("15%: $" + str("%.2f" % TIP_15) + " TOTAL: $" + str("%.2f" % TOT_15))
print ("20%: $" + str("%.2f" % TIP_20) + " TOTAL: $" + str("%.2f" % TOT_20))

