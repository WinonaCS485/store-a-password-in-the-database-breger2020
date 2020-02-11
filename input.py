
import hashlib, uuid, pymysql.cursors

connection = pymysql.connect(host='mrbartucz.com',
                             user='cv7511jj',
                             password='#Movingon2022#',
                             db='cv7511jj_Password',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        x = input("Please create a password.")
        salt = uuid.uuid4().hex
        print("password + salt is: " + x + str(salt))

        hashed_password = hashlib.sha512((x + salt).encode('utf-8')).hexdigest()

        print("The hashed password is: ", hashed_password)
        sql = "INSERT INTO HashPass (Password) VALUES (%s)"

        # execute the SQL command
        cursor.execute(sql, hashed_password)
        connection.commit();


finally:
    connection.close()

user = input("Please reenter your password.")
salt = uuid.uuid4().hex
hashed_password2 = hashlib.sha512((user + salt).encode('utf-8')).hexdigest()

if  user == x:
    print("Log in successful!")
else:
    print("Incorrect please try again.")



