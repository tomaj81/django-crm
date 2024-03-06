import psycopg2

# Connect to the default 'postgres' database to create a new database
dataBase = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='admin123',
    dbname='postgres'
)

# Create a cursor object
cursorObject = dataBase.cursor()

# Create a new database
cursorObject.execute("CREATE DATABASE dcrm")

# Commit the changes
dataBase.commit()

# Close the cursor and connection to 'postgres'
cursorObject.close()
dataBase.close()

# Connect to the newly created 'dcrm' database
dataBase = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='admin123',
    dbname='dcrm'
)

# Create a cursor object for the 'dcrm' database
cursorObject = dataBase.cursor()

# Perform additional operations on the 'dcrm' database if needed

# Commit the changes
dataBase.commit()

# Close the cursor and connection to 'dcrm'
cursorObject.close()
dataBase.close()

print("All Done!")
