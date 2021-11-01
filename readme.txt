1. You must start both Kali and Ubuntu virtual machines.

2. Your Ubuntu virtual machine must have python3 installed.

3. On the Ubuntu virtual machine place client.py in an easy to access folder.

4. On the Ubuntu virtual machine open a terminal and open the directory where
client.py is located using "cd" command.

5. On the Kali virtual machine open a terminal.

6. On the Kali virtual machine type the following command in the terminal:

nc -v -l -p 5555

7. On the Ubuntu virtual machine run client.py by typing the following command in the terminal:

python3 client.py

8. You should now see a connected message on the Kali terminal.
You may now type any non-interactive commands into the Kali terminal.

9. Type exit in the Kali terminal to close the program.
   
