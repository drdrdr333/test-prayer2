'''
    Wrapper class for
    making mysql connection
'''
# pylint:  disable=W1514,C0209,R1733,C0103,W0612,E0401,R1710,R1705,W0718,R0903
import pymysql.cursors

class MySQLConnect:
    '''
        Wrapper for defining a connection
        object
    '''
    def __init__(self, _db):
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='rootroot',
            database=_db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        self.connection = connection

    def query_db(self, query_string, data=None):
        '''
            Main driver for handling queries
             Update - returns updated row
             Select - all items within table
             Insert - returns the inserted row
            # TODO:
                modularized....
        '''
        with self.connection.cursor() as _c:
            try:
                # mogrify the data to make it stringified
                query = _c.mogrify(query_string, data)
                print(f'Running query: {query}')

                #execute your query w/ data
                _c.execute(query, data)

                if query.lower().find('insert') >= 0:
                    # commit query to db - INSERTS return the id of the most
                    # recently implemented row
                    self.connection.commit()
                    return _c.lastrowid
                elif query.lower().find('select') >= 0:
                    # you dont have to commit here because it is
                    # simply selecting - returns a list of dicts
                    result = _c.fetchall()
                    return result
                elif query.lower().find('update') >= 0:
                    _c.callproc('get_all_user_rows')
                    rows = _c.fetchall()
                    search = query[127:128]
                    for row in rows:
                        if row['id'] == int(search):
                            return row
                    return False
                else:
                    # DELETE
                    self.connection.commit()
            except Exception as e:
                #institute a logger here
                print(f"Something is off: {e}")
            finally:
                self.connection.close()

def connect_to_db(db_name):
    '''
        Receive a str() of the
        database name & connect to it
        return the connection obj
    '''
    return MySQLConnect(db_name)
