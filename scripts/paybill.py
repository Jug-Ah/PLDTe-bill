import simplejson as json
import cgi
from dosql import *
from payment import *

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
	
