# Skills-Lab-6
The code begins with setting the variable count equal to zero. Once count is assigned its starting variable, the program then proceeds to prompt the user to enter a name. The input the user chooses to enter for the name is then entered into another variable called name. The variable name is then changed to all lowercase using the .lower() method and then inserted into a variable called lowercaseName. 

The program then prompts the user to input a letter. The user input is then placed into the variable letterInput. letterInput is then also changed into being lowercase by using the .lower() method, and the output is stored in a variable called lowercaseLetter. 

The program makes the name input and letter input both lowercase so that it won't matter if the user capitalized any letters.

The code then performs a for and an if statement. The for statement loops through each letter in lowercaseName. The if statement then goes on to read if lowercaseLetter==letter: then count+=1 so that the count increases each time that letter is found in the name. It then says print("Number of ", letterInput, "'s in ", name,": ",count,sep=""). The print line is used to tell the user how many of the input letter are in the input name. 

To summarize, the code takes a name input and a letter input and then compares the two to see how many time the letter appears in the name.
