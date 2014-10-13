def pay_bill(balance, bill):
	x = doSql()
	
	if bill > balance:
		response = "Insufficient Funds"
		return response
	else:
		balance -= bill
		newbalance = x.execqry("update bankAccount set balance = '" + str(balance) + "' where accountno = '" + accountno + "');", True)
		
		response = "OK"
		return response
