import simplejson as json
import cgi
from dosql import *

def index(req, accountno, pldtacct):
	accountno = cgi.escape(accountno)
	pldtacct = cgi.escape(pldtacct)
	
	x = doSql()
	try:
		balance = x.execqry("select get_balance('" + str(accountno) + "');", False) #Bank
		bill = x.execqry("select get_bill('" + str(pldtacct) + "');", False)	#PLDT
	
		transaction = pay_bill(float(balance), float(bill), str(accountno))
	
		return json.dumps(transaction)	
	
	except:
		response ="Something Went Wrong!"
		
		return json.dumps(transaction)
	
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