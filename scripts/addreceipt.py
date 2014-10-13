import simplejson as json
import cgi
from dosql import *

def index(req,receipt_no):
	receipt_no = cgi.escape(receipt_no)
		
	x = doSql()
	
	amount = x.execqry("select amount from payBill where receiptNo = " + receipt_no + ";", False)[0][0]
	
	rets = x.execqry("select * from set_receipt('" + receipt_no + "', '" + str(amount) + "');", True)
	result = []
	for ret in rets:
		stringed = map(str, ret)
		result.append(stringed)

	return json.dumps(result)
		
	