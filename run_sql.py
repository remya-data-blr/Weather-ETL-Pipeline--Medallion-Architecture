import sqlite3
conn = sqlite3.connect("weather.db")
cur = conn.cursor()
print(cur.execute("SELECT * FROM weather_data ORDER BY temperature_c DESC LIMIT 1").fetchall())
# Result will show hottest city