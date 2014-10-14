from dosql import *
import cgi
import simplejson as json


def index(req, pldtNum):	
	pldtNum = cgi.escape(pldtNum)
	
	
	x = doSql()	
	res = x.execqry("select bill from PLDTaccounts where accountnumber = '" + pldtNum + "';", False)
	

	return json.dumps(res)
	