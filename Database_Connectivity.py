import pymysql
from password_utils import get_decrypted_password

#step 1: Connect to the Database
connection = pymysql.Connect(
    host='localhost',
    user='root',
    password= get_decrypted_password(),
    database='test',    # Make sure this DB exists
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:

        #step 2: Create a Table
        create_query = """
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            department VARCHAR(100)
        );
        """
        cursor.execute(create_query)

        # Step 3: Insert Data
        insert_query = "INSERT INTO employees (name, department) VALUES (%s, %s)"
        values = [("john","IT"),("Alice","HR"),("Bob","Fianance")]
        cursor.executemany(insert_query, values)
        connection.commit()

        # Step 4: Select Data
        select_query = "SELECT * FROM employees"
        cursor.execute(select_query)
        result =  cursor.fetchall()

        with open("employees_output.txt","w") as f:
            for row in result:
                f.write(f"{row}\n")
                #print(row)

finally:
    connection.close()

