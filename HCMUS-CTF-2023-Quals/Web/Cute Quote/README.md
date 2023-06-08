# Cute Quote 

## Description  
![image](https://github.com/KenTranR3/HCMUS-CTF-2023-Quals/blob/main/Web/Cute%20Quote/Description.png)

## Write Up
* There are some note in the source code:
```
const quotes = ['Insanity: doing the same thing expecting different results', '{{7*7}}', '<?php system("whoami"); ?>', '42 is the Answer to the Ultimate Question of Life, the Universe, and Everything']
app.get('/api/public/quote', (req, res) => {
  let quote = quotes[Math.floor(Math.random() * quotes.length)]
  res.send(quote)
})

app.get('/api/public/fake', (req, res) => {
  res.send("HMCSU-CFT{fake_flag}")
})

const flag = process.env.FLAG || "HCMUS-CTF{real_flag}"
app.get('/api/private/flag', (req, res) => {
  res.send(flag)
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
}) 
```
* This code with run through Nginx the through Express, however due to case sensitive in Nginx, we can exploit it by change `/api/private/flag`
to `/API/private/flag` and will print out the flag