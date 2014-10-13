import simplejson as json
import cgi
from dosql import *

def index(req,receipt_no):
	receipt_no = cgi.escape(receipt_no)
		
    x = doSql()
	
	amount = set.execqry("select birthday from personalinfo where userID = " + receipt_no + ";", False)[0][0]
	
    rets = x.execqry("select * from get_receipt('" + receipt_no + "', '" + amount + "');", False)
    result = []
    for ret in rets:
        stringed = map(str, ret)
        result.append(stringed)

    return json.dumps(result)
		
	