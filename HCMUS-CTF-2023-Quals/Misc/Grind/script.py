import sqlite3
db_final = sqlite3.connect('./data-64-final.db')
db_final.execute("attach database './data-64-day2.db' as day2")
db_final.execute("attach database './data-64-day3.db' as day3")
clue = db_final.execute("""
    select * from ranking where rank > 5000 and rank <= 10000 and uid in
    (select d3.uid from day2.ranking d2, day3.ranking d3 where d2.uid = d3.uid and d3.points - d2.points > 900000000 * 0.9 and d3.points - d2.points < 900000000 * 1.1)
    and cast(uid as decimal) > 23000000
""")
for rank, uid, ign, points in clue:
    print(rank, uid, ign, points)