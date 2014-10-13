import sys
import psycopg2



class doSql(object):
    _cxn = ""
    _cur = ""
    errmsg ="" 
	
    def __init__(self):
        self._cxn = psycopg2.connect("dbname='hygeia' user='postgres' password='ihopeyourehappy' host='127.0.0.1' port='5432'")
        self._cur = self._cxn.cursor()
        
    def __del__(self):
        self._cur.close()
        self._cxn.close()

    def execqry(self, sql, apply_):
        rows = []
        try:
            self._cur.execute(sql)
            rows = self._cur.fetchall()
	    if apply_:
                self._cxn.commit()
            if self._cur.rowcount == 0:
                rows.append(['None'])
        except:
            #errmsg = sys.exc_type + ":" + sys.exc_value 
            errmsg =  str(sys.exc_info()[1])
            rows.append([errmsg])
        return rows    

    