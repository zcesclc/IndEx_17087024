import sqlite3

# Step 1: Create a connection object that represents the database
conn = sqlite3.connect('rainrainrain.db')
c = conn.cursor()
# Step 2: Create the tables
c.execute('''
          CREATE TABLE user
          (user_id INTEGER PRIMARY KEY,
          username TEXT NOT NULL,
          email TEXT NOT NULL)
          ''')

c.execute('''
          CREATE TABLE city
          (city_id INTEGER PRIMARY KEY,
          city TEXT NOT NULL)
          ''')

c.execute('''
          CREATE TABLE forecast
          (forecast_id INTEGER PRIMARY KEY,
          forecast_datetime TEXT,
          user_id integer,
          city_id integer,
          forecast TEXT,
          comment TEXT,
          FOREIGN KEY (city_id) REFERENCES city(city_id),
          FOREIGN KEY(user_id) REFERENCES user(user_id))
          ''')

# Step 3: Insert data

sql = "INSERT INTO user (username, email) VALUES (?, ?)"
values = [('weatherman', 'jo@bloggs.com'),
          ('itrains', 'itrains@alot.co.uk'),
          ('sunny', 'sunny_grl@sunsine.co.uk')]
c.executemany(sql, values)

sql = "INSERT INTO city (city) VALUES (?)"
values = [['London'], ['Mancheter'], ['Birmingham'], ['Edinburgh'], ['Belfast'], ['Cardiff']]
c.executemany(sql, values)

sql = "INSERT INTO forecast ( city_id, user_id, forecast_datetime, forecast, comment) VALUES (?, ?, ?, ?, ?)"
values = [(2, 2, '2020-01-27 09:00:00', 'Moderate rain', 'It is really likely to rain today, sorry folks'),
          (6, 1, '202-01-27 09:00:00', 'Heavy rain' ,'Don''t leave home without full waterproofs today!'),
          (1, 3, '2020-01-27 09:00:00', 'No rain', 'No umbrealla required')]
c.executemany(sql, values)


# Step 4: Save (commit) the changes
conn.commit()

# Step 5 (optional): Close the connection if you are done with it
# Be sure any changes have been committed or they will be lost.
conn.close()
