# json-path-traversal
This Python program loads data from a JSON file specified by the user and allows them to traverse it based on a given path. The program prompts the user to enter the path to the desired value, which is a sequence of keys separated by spaces.
The program uses the json module to load the data from the JSON file into a dictionary. It then traverses the dictionary based on the provided path, treating numeric keys as integers.
Finally, the program displays the retrieved value to the user using colored output.

## Usage: 
1. Run main file.
2. You will be prompted to enter the path to the desired value and you can enter "done" to finish the program.
3. After entering the path, the program will display the retrieved value in cyan color.

### Example: 
Here's an example usage of the program with a data.json file containing the following data:

data.json file:
{
  "name": "Ali",
  "lastname": "Adl Yar"
  "friends": [
     {
       "name": "Matin",
       "lastname": "Moradi"
     },
     {
       "name": "Arman",
       "lastname": "Moqimi"
     },
     {
       "name": "Mohammad Hossein",
           "lastname": "Nahi"
     }
  ]
}

Running the program and entering the path "name" and "friends 0 name" would produce the following output:

Enter The Path Of Value You Want (or "done" to finish): name

==> Ali 

Enter The Path Of Value You Want (or "done" to finish): friends 0 name

==> Matin 

Enter The Path Of Value You Want (or "done" to finish): done

Thank You For Choosing Us :)
>>> Developed By Maryam Fakhraei & Amirhossein Naseri <<<