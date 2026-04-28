# 3200-group-project

## AI acknowledgement
Database entries 2-7 were genrated based on prompt "Using entry 1 make more Users" 

GitHub Copilot was primarily used for debugging, error correction, and providing 
recommendations related to improving the security of the implementation. This was particularly 
helpful when working with Python libraries such as hashlib. 
All final code, analysis, and written content were developed and produced by the authors of this 
report. AI tools were used solely as supplementary aids to support learning, troubleshooting, and 
refinement of the work. 

## Instructions

- How to set up the Environment:
* Download all of the files.
* Place them in a folder in VScode.
* Open the Terminal (Ctr + J).
* Ensure Python is installed on your device.
* Type pip install cryptography (If error occurs type: python -m pip install cryptography)
* Run python authentication.py
- How to run the broken system simulation:
* Choose option 1 and enter your credentials.
* Once you enter a login and password, choose option 2, which will provide you with the broken database. As you can see, all the passwords are visible and are in plaintext.
* Next, click on option 3 to see what will happen to your database when there is no encryption implemented. You should see the word 'Compromised' next to each set of user credentials.
- How to run the secure system simulation:
* In the list provided, choose option 4, which will create a new file with a secure database.
* Once the creation is completed, click on option 5 and look at the way your passwords have changed. They are no longer in plaintext, instead, they were encrypted using the salted SHA-256 algorithm.
* Click on option 6 and simulate a dictionary attack. You should be able to see the word 'Safe' next to each user entry. This is exactly what will happen to your system when encryption is implemented.
* Option 7 is optional. When clicking it, you will witness that the system hashes the input and compares it to the stored hash, allowing secure authentication.
- Looking Ahead:
* Option 8 prompts you to type in a message with is then converted into unreadable ciphertext. Even if an attacker gains access, RSA ensures the message is unreadable without the private key.
* Option 9 allows you to exit the simulation. Please delete all the files and database entries you created to get the simulation into it's original state.

## Brief explanation of how the mechanism and attack are implemented:
- The database was designed with JSON, whereas all the security mechanisms were written in Python using the hashlib and os libraries. 
- Password protection was achieved through the use of the SHA-256 algorithm with a randomly generated salt produced by the PRNG.
- When the secure system is ran, the passwords are hashed for the purpose of authentication and confidentiality.
- The RSA encryption was implemented using the cryptography libraries.
- The broken system showcases how easy it is for insider threats to obtain user information when encryption is not implemented. This is because the password which was created by the user is visible when the broken database is shown.
- The secure system showcases how important it is to encrypt user data. This was seen in step 5, when all the previously created passwords were no longer readable. 
