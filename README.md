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


