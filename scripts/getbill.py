from dosql import *
import cgi
import simplejson as json


def index(req, pldtNum):	
	pldtNum = cgi.escape(pldtNum)
	
	x = doSql()
	rets = x.execqry("select * from get_bill('" + pldtNum + "');", False)
	result = []
	for ret in rets:
		stringed = map(str, ret)
		result.append(stringed)
		
	return json.dumps(result)
		
	