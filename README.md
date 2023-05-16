# Resume-Parser
Find best suited candidate for a job using AI

# Features:

Utilizes the edit distance metric to calculate the similarity between words
Uses a comprehensive English dictionary to find the closest match
Provides a simple and user-friendly command-line interface for testing
Code Overview:

# Installation:
The code begins with the installation of the necessary dependencies, including the NLTK library.

Loading the English Dictionary: The code downloads and loads the English dictionary from the NLTK corpus, ensuring a wide range of words for comparison.

Finding the Closest Word: The find_closest_word() function implements the core logic of the auto-correct tool. It iterates over the English dictionary, calculating the edit distance between the misspelled word and each word in the dictionary. It updates the closest word if a smaller distance is found.

Testing the Tool: The code prompts the user to enter a word and then calls the find_closest_word() function to obtain the autocorrected word. The result is printed on the console.

# Usage:
To use this auto-correct tool, simply run the script and follow the instructions on the command line. Enter a word, and the tool will provide the closest corrected word based on the English dictionary.

# Contributing:
Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, feel free to submit a pull request. Let's collaborate and enhance the functionality and performance of this auto-correct tool together.

# License:
This project is released under the [insert license name] license. Please refer to the LICENSE file for more details.

We hope you find this project insightful and informative. Don't hesitate to explore the code and experiment with different functionalities. If you have any questions or feedback, feel free to reach out. Happy coding!
