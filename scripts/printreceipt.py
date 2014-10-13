import simplejson as json
import cgi
from dosql import *

def index(req,receipt_no):
	receipt_no = cgi.escape(receipt_no)
		
	x = doSql()
	rets = x.execqry("select * from get_receipt('" + receipt_no + "');", False)
	result = []
	for ret in rets:
		stringed = map(str, ret)
		result.append(stringed)
		
	return json.dumps(result)
		
	