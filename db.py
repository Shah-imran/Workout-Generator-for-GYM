import pymysql
import var


def create_db():
    databaseServerIP = var.db_ip # IP address of the MySQL database server
    port = var.db_port
    databaseUserName = var.db_user       # User name of the database server
    databaseUserPassword = var.db_pass           # Password for the database user
    newDatabaseName = var.db_name # Name of the database that is to be created
    charSet = "utf8mb4"     # Character set
    cusrorType = pymysql.cursors.DictCursor
    connectionInstance = pymysql.connect(host=databaseServerIP, port=port, user=databaseUserName, password=databaseUserPassword, charset=charSet,cursorclass=cusrorType)

    try:

        # Create a cursor object
        cursorInsatnce = connectionInstance.cursor()

        # try:
        #     sqlStatement            = "DROP DATABASE "+self.newDatabaseName
        #     # Execute the create database SQL statment through the cursor instance
        #     cursorInsatnce.execute(sqlStatement)
        # except Exception as e:
        #       print("Exeception occured:{}".format(e))

        try:
            # SQL Statement to create a database
            sqlStatement = "CREATE DATABASE " + newDatabaseName

            # Execute the create database SQL statment through the cursor instance
            cursorInsatnce.execute(sqlStatement)

             # SQL query string
            sqlQuery = "SHOW DATABASES"

            # Execute the sqlQuery
            cursorInsatnce.execute(sqlQuery)

            #Fetch all the rows
            databaseList = cursorInsatnce.fetchall()

            for datatbase in databaseList:
                print(datatbase)

        except Exception as e:
            print("Exeception occured:{}".format(e))

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        connectionInstance.close()

    con = DB()
    con.create_table()
    con.close()

class DB():
    def __init__(self):
        db_ip = var.db_ip # IP address of the MySQL database server
        db_port = var.db_port
        db_user = var.db_user       # User name of the database server
        db_pass = var.db_pass           # Password for the database user
        db_name = var.db_name # Name of the database that is to be created
        self.db = pymysql.connect(host=db_ip, port=db_port, user=db_user, password=db_pass, db=db_name)

    def create_table(self):
        try:

            # Create a cursor object
            cursor = self.db.cursor()

            # Drop table if it already exist using execute() method.
            # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

            # Create table as per requirement
            sql = """CREATE TABLE muscle_groups (
            id INT AUTO_INCREMENT PRIMARY KEY,
            muscle_name  VARCHAR(255) UNIQUE NOT NULL,
            visible_for_user BOOLEAN NOT NULL DEFAULT 1
            )"""

            cursor.execute(sql)

        except Exception as e:
            print("Exeception occured:{}".format(e))

        try:

            sql = """CREATE TABLE exercise (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            info TEXT NULL,
            muscle_group_id INT,
            calories INT NULL,
            time INT NULL,
            images VARCHAR(255) NULL,
            visible_for_user BOOLEAN NOT NULL DEFAULT 1,
            FOREIGN KEY (muscle_group_id) REFERENCES muscle_groups(id)
            )"""

            cursor.execute(sql)


        except Exception as e:
            print("Exeception occured:{}".format(e))

        try:

            sql = """CREATE TABLE workouts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            w_name VARCHAR(255) NOT NULL,
            info TEXT NULL,
            exercise_id INT,
            set_count INT NULL,
            type VARCHAR(255) NOT NULL,
            time INT DEFAULT 0,
            reps INT DEFAULT 0,
            rounds INT DEFAULT 1,
            visible_for_user BOOLEAN NOT NULL DEFAULT 1,
            FOREIGN KEY (exercise_id) REFERENCES exercise(id)
            )"""

            cursor.execute(sql)


        except Exception as e:
            print("Exeception occured:{}".format(e))

    def update_exercise(self, info, id):
        try:
            cursor = self.db.cursor()

            sql = """UPDATE exercise
            SET name = "{}", info = "{}", muscle_group_id = {} ,
            calories = {} , time = {} , images = "{}" , visible_for_user = {}
            WHERE id = {};""".format(info[0],info[1], info[2], info[3], info[4], info[5], info[6],  id)

            cursor.execute(sql)

            self.db.commit()
            return True
        except Exception as e:
            print("Exeception occured:{}".format(e))
            self.db.rollback()
            return e

    def add_muscle_group(self, info, visible_for_user):
        try:
            cursor = self.db.cursor()

            sql = """INSERT INTO muscle_groups(muscle_name, visible_for_user)
            VALUES ("{}",{})""".format(info, visible_for_user)

            cursor.execute(sql)

            self.db.commit()
            return True
        except Exception as e:
            print("Exeception occured:{}".format(e))
            self.db.rollback()
            return e

    def add_exercise(self, info, visible_for_user):
        try:
            cursor = self.db.cursor()

            sql = """INSERT INTO exercise(name, info, muscle_group_id, calories, time, images, visible_for_user)
            VALUES ("{}", "{}", {}, {}, {}, "{}", {})""".format(info[0], info[1], info[2], info[3], info[4], info[5], visible_for_user)

            cursor.execute(sql)

            self.db.commit()
            return True
        except Exception as e:
            print("Exeception occured:{}".format(e))
            self.db.rollback()
            return e

    def add_workout(self, info, visible_for_user):
        try:
            cursor = self.db.cursor()

            sql = """INSERT INTO workouts(w_name, info, exercise_id, set_count, type, time, reps, rounds, visible_for_user)
            VALUES ("{}", "{}", {}, {}, "{}", {}, {}, {}, {})
            """.format(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], visible_for_user)

            cursor.execute(sql)

            self.db.commit()
            return True
        except Exception as e:
            print("Exeception occured:{}".format(e))
            self.db.rollback()
            return e

    def search_exercise(self, keyword):
        try:
            cursor = self.db.cursor()

            if var.admin_mode == True:
                sql = """Select name FROM exercise where name LIKE "%{}%"
                """.format(keyword)
            else:
                sql = """Select name FROM exercise where visible_for_user = 1 AND exercise.name LIKE "%{}%"
                """.format(keyword)

            cursor.execute(sql)
            result = cursor.fetchall()

            data = [result[i][0] for i in range(len(result))]
            # data = list(set(data))
            return data

        except Exception as e:
            print("Exeception occured:{}".format(e))

    def fetch_muscle_groups(self):
        try:
            cursor = self.db.cursor()

            if var.admin_mode == True:
                sql = """Select muscle_name FROM muscle_groups"""
            else:
                sql = """Select muscle_name FROM muscle_groups where visible_for_user = 1 """

            cursor.execute(sql)
            result = cursor.fetchall()

            data = []

            data = [result[i][0] for i in range(len(result))]

            return data

        except Exception as e:
            print("Exeception occured:{}".format(e))

    def fetch_exercise(self, muscle_group):
        try:
            cursor = self.db.cursor()
            if var.admin_mode == True:
                sql = """Select name, muscle_name FROM exercise join muscle_groups on
            muscle_groups.id = exercise.muscle_group_id where muscle_name = "{}"
            """.format(muscle_group)
            else:
                sql = """Select name, muscle_name FROM exercise join muscle_groups on
            muscle_groups.id = exercise.muscle_group_id where (exercise.visible_for_user = 1 AND 1) AND (muscle_name = "{}" AND 1)
            """.format(muscle_group)

            cursor.execute(sql)
            result = cursor.fetchall()

            data = []

            data = [result[i][0] for i in range(len(result))]

            return data

        except Exception as e:
            print("Exeception occured:{}".format(e))

    def fetch_exercise_info(self, name):
        try:
            cursor = self.db.cursor()

            sql = """Select info, images, muscle_name FROM exercise join muscle_groups on
            muscle_groups.id = exercise.muscle_group_id where exercise.name = "{}"
            """.format(name)

            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            info = result[0][0]
            image_path = result[0][1]
            data = []

            data = [result[i][2] for i in range(len(result))]

            return info, data, image_path

        except Exception as e:
            print("Exeception occured:{}".format(e))

    def fetch_exercise_info2(self, name):
        try:
            cursor = self.db.cursor()

            sql = """Select calories, time FROM exercise join muscle_groups on
            muscle_groups.id = exercise.muscle_group_id where exercise.name = "{}"
            """.format(name)

            cursor.execute(sql)
            result = cursor.fetchone()
            calories = result[0]
            time = result[0]
            return calories, time

        except Exception as e:
            print("Exeception occured:{}".format(e))

    def fetch_exercise_info3(self, name):
        try:
            cursor = self.db.cursor()

            sql = """Select exercise.id, exercise.info, muscle_group_id, muscle_name, calories, exercise.time, images, exercise.visible_for_user
            FROM exercise join muscle_groups on
            muscle_groups.id = exercise.muscle_group_id where exercise.name = "{}"
            """.format(name)

            cursor.execute(sql)
            result = cursor.fetchall()

            exercise_id = [result[i][0] for i in range(len(result))]
            exercise_info = result[0][1]
            muscle_group_id = [result[i][2] for i in range(len(result))]
            muscle_name = [result[i][3] for i in range(len(result))]
            calories = result[0][4]
            exercise_time = result[0][5]
            image_path = result[0][6]
            visible_for_user = result[0][7]
            return exercise_id, exercise_info, muscle_group_id, muscle_name, calories, exercise_time, image_path, visible_for_user

        except Exception as e:
            print("Exeception occured:{}".format(e))

    def fetch_workout_info(self, name):
        try:
            cursor = self.db.cursor()

            sql = """Select name, workouts.info, set_count, type, calories, exercise.time, workouts.time, reps, rounds FROM workouts join exercise on
            workouts.exercise_id = exercise.id where  workouts.w_name = "{}"
            """.format(name)

            cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)
            exercise_name = [result[i][0] for i in range(len(result))]
            info = result[0][1]
            sets = [result[i][2] for i in range(len(result))]
            types = [result[i][3] for i in range(len(result))]
            calories = [result[i][4] for i in range(len(result))]
            exercise_time = [result[i][5] for i in range(len(result))]
            workout_time = [result[i][6] for i in range(len(result))]
            reps = [result[i][7] for i in range(len(result))]
            rounds = [result[i][8] for i in range(len(result))]

            return exercise_name, info, sets, types, calories, exercise_time, workout_time, reps, rounds

        except Exception as e:
            print("Exeception occured:{}".format(e))

    def fetch_muscle_id(self, muscle):
        try:
            cursor = self.db.cursor()

            sql = """Select id FROM muscle_groups where muscle_name = "{}" """.format(muscle)

            cursor.execute(sql)
            result = cursor.fetchone()

            return result[0]

        except Exception as e:
            print("Exeception occured:{}".format(e))

    def fetch_exercise_id(self, exercise):
        try:
            cursor = self.db.cursor()

            sql = """Select id FROM exercise where name = "{}" """.format(exercise)

            cursor.execute(sql)
            result = cursor.fetchone()

            return result[0]

        except Exception as e:
            print("Exeception occured:{}".format(e))

    def fetch_workout_name(self):
        try:
            cursor = self.db.cursor()

            if var.admin_mode == True:
                sql = """Select w_name FROM workouts"""
            else:
                sql = """Select w_name FROM workouts where visible_for_user = 1"""

            cursor.execute(sql)
            result = cursor.fetchall()

            data = [result[i][0] for i in range(len(result))]

            return data

        except Exception as e:
            print("Exeception occured:{}".format(e))

    def fetch_table(self, table_name):
        try:
            cursor = self.db.cursor()

            sql = """Select * FROM {}""".format(table_name)

            cursor.execute(sql)
            result = cursor.fetchall()

            return result

        except Exception as e:
            print("Exeception occured:{}".format(e))

    def remove_workout(self, name):
        try:
            cursor = self.db.cursor()

            sql = """DELETE FROM workouts WHERE w_name = "{}";""".format(name)

            cursor.execute(sql)

            self.db.commit()
            return True
        except Exception as e:
            print("Exeception occured:{}".format(e))
            self.db.rollback()
            return e

    def remove_exercise(self, name):
        try:
            cursor = self.db.cursor()

            sql = """DELETE FROM exercise WHERE name = "{}";""".format(name)

            cursor.execute(sql)

            self.db.commit()
            return True
        except Exception as e:
            print("Exeception occured:{}".format(e))
            self.db.rollback()
            return e

    def remove_exercise_by_id(self, id):
        try:
            cursor = self.db.cursor()

            sql = """DELETE FROM exercise WHERE id = {};""".format(id)

            cursor.execute(sql)

            self.db.commit()
            return True
        except Exception as e:
            print("Exeception occured:{}".format(e))
            self.db.rollback()
            return e

    def remove_muscle_groups(self, name):
        try:
            cursor = self.db.cursor()

            sql = """DELETE FROM muscle_groups WHERE muscle_name = "{}";""".format(name)

            cursor.execute(sql)

            self.db.commit()
            return True
        except Exception as e:
            print("Exeception occured:{}".format(e))
            self.db.rollback()
            return e

    def close(self):
        self.db.close()


# def populate_muscle_table():
#     with open("muscle.txt", "r") as f:
#         data = f.read()
#         data = data.strip()
#     data = data.split("\n")
#     conn = DB()
#     for item in data:
#         conn.add_muscle_group(item)
#     conn.close()

# def populate_exercise_table():
#     with open("exercise.txt", "r") as f:
#         data = f.read()
#         data = data.strip()
#     data = data.split("\n")
#     conn = DB()
#     conn.add_exercise([item.split(",") for item in data])
#     conn.close()

# def populate_workout_table():
#     with open("workouts.txt", "r") as f:
#         data = f.read()
#         data = data.strip()
#     data = data.split("\n")
#     conn = DB()
#     data = [item.split(",") for item in data]
#     for item in data:
#         print(item)
#         conn.add_workout(item)
#     conn.close()

if __name__ == "__main__":
    # create_db()
    # conn = DB()
    # result = conn.fetch_muscle_groups()
    # print(type(result[0]))
    # conn.close()
    # populate_muscle_table()
    # populate_exercise_table()
    # populate_workout_table()
    pass