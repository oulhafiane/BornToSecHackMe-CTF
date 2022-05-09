## Reconnaissance and information gathering
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
Once we checked all the comments we completed te source code:**

```C
char getme1() { return 'I'; }
char getme2() { return 'h'; }
char getme3() { return 'e'; }
char getme4() { return 'a'; }
char getme5() { return 'r'; }
char getme6() { return 't'; }
char getme7() { return 'p'; }
char getme8() { return 'w'; }
char getme9() { return 'n'; }
char getme10() { return 'a'; }
char getme11() { return 'g'; }
char getme12() { return 'e'; }
int main() {
	printf("M");
	printf("Y");
	printf(" ");
	printf("P");
	printf("A");
	printf("S");
	printf("S");
	printf("W");
	printf("O");
	printf("R");
	printf("D");
	printf(" ");
	printf("I");
	printf("S");
	printf(":");
	printf(" ");
	printf("%c",getme1());
	printf("%c",getme2());
	printf("%c",getme3());
	printf("%c",getme4());
	printf("%c",getme5());
	printf("%c",getme6());
	printf("%c",getme7());
	printf("%c",getme8());
	printf("%c",getme9());
	printf("%c",getme10());
	printf("%c",getme11());
	printf("%c",getme12());
	printf("\n");
	printf("Now SHA-256 it and submit");
}
```

> **So the password for the user 'laurie' is `SHA256("Iheartpwnage")` which is `330b845f32185747e4f8ca15d40ca59796035c89ea809fb5d30f4da83ecf45a4`.**

> **When we connected to the user laurie via ssh we found another README wich says:**
![29](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/29.png)
