import pyodbc, platform

class OperatingSystemNotSupported(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class SqlConnection:    
    __conn = None

    def getConnection(self):
        if self.__conn == None:
            self.__conn = self.__openConnection()
        return self.__conn
    
    def __openConnection(self):
        conn_strings = open('sqlserver/connection_strings').read().split('</config>')
        os_name = platform.system()
        filtered_conn_strings = list(filter(lambda conn_str: conn_str.startswith(f'<{os_name}>'), conn_strings))
        if len(filtered_conn_strings) == 0:
            raise OperatingSystemNotSupported(f'{os_name} operating system not supported')
        conn_string = filtered_conn_strings[0].replace(f'<{os_name}>', '')
        return pyodbc.connect(conn_string) 


    def closeConnection(self):
        if self.__conn != None:
            self.__conn.close()
            self.__conn = None
