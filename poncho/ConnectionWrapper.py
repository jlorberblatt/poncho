'''
Created on Feb 7, 2018

@author: Jakob Lorberblatt
'''

class ConnectionWrapper(object):
    '''
    A simple connection wrapper
    '''


    def __init__(self,con):
        '''
        Constructor
        '''
        self.__con = con
        self.__cursor = self.__con.cursor()
        
    def close(self):
        return self.__con.close()
    
    
    def query(self,sql):
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()
    
    def get_single_value(self,sql):
        self.__cursor.execute(sql)
        v = self.__cursor.fetchone()
        if v: 
            return v[0]
        
    
    def get_single_row(self,sql):
        self.__cursor.execute(sql)
        v = self.__cursor.fetchone()
        return v
    
    def get_single_col(self,sql):
        self.__cursor.execute(sql)
        v = self.__cursor.fetchall()
        if v:
            return map(lambda l: l[0],v)
        
    def execute(self,sql):
        self.__cursor.execute(sql)
        
    
    def use(self,db):
        self.execute('use %s' % db)
        
    
    def kill(self,list_or_id):
        if type(list_or_id) == type('') or type(list_or_id) == type(1):
            self.execute('kill %s' % list_or_id)
        else:
            for id in list_or_id:
                self.execute('kill %s' % list_or_id)
                
    
    