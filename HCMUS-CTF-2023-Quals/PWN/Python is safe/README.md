# Python is safe

## Description  
![image](https://github.com/KenTranR3/HCMUS-CTF-2023-Quals/blob/main/PWN/Python%20is%20safe/Description.png)

## Write Up
* There are some note in the source code:
    -  ``` libc = CDLL('/lib/x86_64-linux-gnu/libc.so.6') buf1 = c_buffer(512) buf2 = c_buffer(512) ``` this code using gnu compiler and acting like the C code, ```c_buffer``` is create a buffer just like an array and var  `buf1` and `buf2` connect to each other.
    - ```libc.gets(buf1) ``` when user input, it will be added to `buf1` not `buf2`.
* However because `buf1` and `buf2` connect to each other so we can try to buffer overflow it. We will input an 512 letter + `HCMUS-CTF` to print the flag
* ```ncat --ssl python-is-safe.chall.ctf.blackpinker.com 443 A*512+HCMUS-CTF```
* ```HCMUS-CTF{pYt40n_4rE_s|U|Perrrrrrr_5ecureeeeeeeeeeee}```


