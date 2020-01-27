from utils.sqlConnection import SqlConnection
from models.user import User

class UserDataController:

    __connection = SqlConnection().getConnection()

    def getUsers(self, userIds=None):
        userSQL = '''SELECT id userId,
                     CONCAT(fname, ' ', lname) userName
                     FROM Users u WHERE 1=1'''
        params = None
        if (userIds != None and len(userIds) > 0):
            # enforce type to try and avoid sql security / data issues. We're using params here so it should be fine 
            # we just want to avoid incorrect data in the sql query. Look into a better way of handling this
            for uid in userIds:
                if type(uid) is not int:
                    raise TypeError("Ids must be of type int")
            params = userIds
            uidInClause = ",",
            userSQL += " AND u.id IN ({}) ".format(uidInClause.join([str(u) for u in userIds]))

        data_table = self.__connection.cursor().execute(userSQL, params) if params != None else self.__connection.cursor().execute(userSQL)

        return [User(row.userId, row.userName) for row in data_table]