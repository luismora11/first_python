SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100 

def calculate_price(number_of_tickets):
	return number_of_tickets * TICKET_PRICE + SERVICE_CHARGE

while tickets_remaining >= 1:
	print("There are {} ticket remaining.".format(tickets_remaining))
	name = input("What is your name?  ")
	number_tickets = input("How many tickets would you like {}?, ".format(name))
	try:
	    number_tickets = int(number_tickets)
	    if number_tickets > tickets_remaining:
		    raise ValueError("there are only {} tickets remaining".format(tickets_remaining))
	except ValueError as err:
		print("Oh no we ran into an issue, {}. please try again".format(err))
	else:
		amount_due = calculate_price(number_tickets)
		print("this is the amount due ${} ".format(amount_due))
		should_proceed = input("Do you want to preceed  y/n ?")
		if should_proceed.lower() == "y":
			print("SOLD")
			tickets_remaining -= number_tickets
			
		else:
			print("thank you anyways {}".format(name))
		
else:
	print("sorry")


