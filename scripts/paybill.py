import simplejson as json
import cgi
from dosql import *

def index(req, accountno, pldtacct, amount):
	accountno = cgi.escape(accountno)
	pldtacct = cgi.escape(pldtacct)
	amount = cgi.escape(amount)
	
	x = doSql()
	try:
		balance = x.execqry("select get_balance('" + str(accountno) + "');", False)[0][0] #Bank
		bill = x.execqry("select get_bill('" + str(pldtacct) + "');", False)[0][0]	#PLDT

		transaction = pay_bill(float(balance), float(bill), str(accountno), str(pldtacct), float(amount))


		return json.dumps(str(transaction))	
	
	except:
		response ="Something Went Wrong!"
		
		return json.dumps(response)
	
def pay_bill(balance, bill, accountno, pldtacct, amount):
	x = doSql()
	

	if amount > balance:
		response = "Insufficient Funds."
		return response
	else:
		balance = balance - amount
		bill = bill - amount

		newbalance = x.execqry("update bankAccount set balance = '" + str(balance) + "' where accountno = '" + accountno + "';", True)
		rembill = x.execqry("update pldtAccount set bill = '" + str(bill) + "' where pldtacct ='" + pldtacct + "';", True)
		
		receipt = x.execqry("select set_payment('" + accountno  + "','" + pldtacct  + "','" + str(amount) + "');", True)[0][0]	

		return json.dumps(receipt)
