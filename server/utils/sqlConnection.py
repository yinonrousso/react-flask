import pyodbc, os

class ConfigNotFoundException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class SqlConnection:    
    __conn = None

    def getConnection(self):
        if self.__conn == None:
            self.__conn = self.__openConnection()
        return self.__conn
    
    def __openConnection(self):
        print(os.getcwd())
        config = open('sqlserver/connection_config').read()
        configs = config.split('</config>')
        ubuntu_config = list(filter(lambda cfg: '<Ubuntu>' in cfg, configs))
        if len(ubuntu_config) == 0:
            raise ConfigNotFoundException("Ubuntu config not found")
        config_keys = ubuntu_config[0].split(os.linesep)
        driver = list(filter(lambda key: key.startswith('driver'), config_keys))[0].replace('driver=','')
        server = list(filter(lambda key: key.startswith('server'), config_keys))[0].replace('server=','')
        uid = list(filter(lambda key: key.startswith('uid'), config_keys))[0].replace('uid=','')
        pwd = list(filter(lambda key: key.startswith('pwd'), config_keys))[0].replace('pwd=','')
        database = (list(filter(lambda key: key.startswith('database'), config_keys)) or ['db1'])[0]
        return pyodbc.connect(driver=driver, server=server, database=database, uid=uid, pwd=pwd) 


    def closeConnection(self):
        if self.__conn != None:
            self.__conn.close()
            self.__conn = None
