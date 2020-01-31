from utils.sqlConnection import SqlConnection
from models.user import User

class UserDataController:

    __connection = SqlConnection().getConnection()

    def getUsers(self, userIds=None):
        userSQL = '''SELECT pkId userId,
                     fname firstName,
                     lname lastName,
                     email email
                     FROM Users u WHERE 1=1'''
        params = None
        if (userIds != None and len(userIds) > 0):
            # enforce type to try and avoid sql security / data issues. We're using params here so it should be fine 
            # we just want to avoid incorrect data in the sql query. Look into a better way of handling this
            for uid in userIds:
                if type(uid) is not int:
                    raise TypeError("Ids must be of type int")
            params = userIds
            uidInClause = ","
            userSQL += f" AND u.pkId IN ({uidInClause.join(['?' for u in userIds])}) "

        data_table = self.__connection.cursor().execute(userSQL, params) if params != None else self.__connection.cursor().execute(userSQL)

        return [User(row.userId, row.firstName, row.lastName, row.email) for row in data_table]

    def saveUser(user):
        if user == None or type(user) is not User:
            raise TypeError("invalid user argument")
        
        params = [user.fname, user.lname, user.email]
        if user.id > 0:
            sql = "INSERT INTO Users (fname, lname, email) OUTPUT inserted.pkId userId VALUES (?, ?, ?)"
        else:
            sql = "UPDATE Users SET fname=?, lname=?, email=? OUTPUT inserted.pkId userId WHERE pkId=?"
            params.append(user.id)

        try:
            row = self.__connection.cursor().execute(sql, params).fetchone()
            self.__connection.cursor().commit()
        except:
            self.__connection.cursor().rollback()
            raise

        return self.getUsers([row.userId])
        
