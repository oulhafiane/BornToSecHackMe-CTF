## Reconnaissance and information gathering
When running BornToSecHackMe-v1.1.iso a simple login prompt appeared, no IP address is displayed on the screen, we don't know any user/password in the system.  

![1](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/1.png)

So I created a NAT network in the VirtualBox and connected the BornToSecHackMe virtual machine to it.  
I also have another virtual machine with blackarch linux on it, I attached the same network to it.  

![2](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/2.png)

After I started an intense scan with Nmap in the NAT network  

![3](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/3.png)

Then I got the result

![4](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/4.png)

The information we now know about the machine:  
- IP address: 10.0.2.4
- Open Ports: 21, 22, 80, 143, 443, 993

Here is the detail of the services listening in the open ports:

![5](https://raw.githubusercontent.com/oulhafiane/BornToSecHackMe-CTF/main/ressources/5.png)
