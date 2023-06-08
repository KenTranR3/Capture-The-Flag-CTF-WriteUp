# Grind 

## Description  
![image](https://github.com/KenTranR3/HCMUS-CTF-2023-Quals/blob/main/Misc/Grind/Description.png)

## Write Up
* This is an challenge to find the player infomation in .db file
* As a gamer, I knew it was Granbase Fantasy and GW was an event of the game.
* Using SQLite, we can know about the database schema.
```
CREATE TABLE ranking(rank,uid,name,points)
```
* Using the infomation from the author, we could know how to find the player in 4 clues.
    - Clue 1: my friend did greater than even he expected. Too bad he had real-life business to do on the last day and couldn't get into top 5k.
    - Clue 2: he put out like 900 million on day 3.
    - Clue 3: we started playing right before 2019. (Using Wiki, we can know that there were more than 23 million accounts created before)
    - Clue 4: his current IGN is related to a mathematical million-dollar problem or something?
* Known the clue, let's construct Python script for that
```
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
```

```
9614 23983477 ζ(2) 2391789368
```
```
HCMUS-CTF{23983477-1.6449340668-2391789368-9614}
```




