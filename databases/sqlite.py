'''
Created on Apr 7, 2010

@author: emil
'''

try:
    import sqlite3 as db
except ImportError:
    import sqlite2 as db
    
import os
import re


class SQLite(object):
    '''
    classdocs
    '''
    database = None

    def __init__(self, string):
        if self._validSqliteMemory(string) or self._validSqliteFile(string):
        #if string == ":memory:" or self._validSqliteFile(string):
            self.database = string
            
    def _validSqliteMemory(self, string):
        if re.search("^:", string) is not None:
            if string == ':memory:':
                return True
            else:
                raise ValueError("%s is not valid memory connection" % string)
               
        
    def _validSqliteFile(self, file):
        dir = os.path.dirname(file)
        if dir != "":
            if os.path.isdir(dir):
                if os.access(dir, os.W_OK):
                    if os.path.isfile(file):
                        if os.access(file, os.W_OK):
                            return True 
                        else:
                            raise ValueError("%s is not writable" % file)
                    else:
                        """ We might not have the file but we can write a file so go ahead """
                        return True
                else:
                    raise ValueError("%s is not writeable" % dir)
            else:
                raise ValueError("%s does not exist" % dir)
        else:
            if os.path.isfile(file):
                if os.access(file, os.W_OK):
                    return True 
                else:
                    raise ValueError("%s is not writable" % file)
            else:
                return True
            
                

    def connect(self):
        return db.connect (self.database)
        
