# FUTURE_CS_02
Password Strength Analyzer
A simple Python tool to analyze the strength of passwords based on length and character types. This script provides a score, strength rating, and feedback to help users create more secure passwords. Part of the FUTURE_CS_02 repository.
Features
Evaluates password strength based on:
Length (minimum 8 characters)

Use of uppercase letters

Use of lowercase letters

Use of numbers

Use of special characters

Returns a score out of 100

Provides a strength rating (Very Weak, Weak, Moderate, Strong, Very Strong)

Offers constructive feedback for improvement

Installation
Clone the Repository  
bash

git clone https://github.com/flair19/FUTURE_CS_02.git
cd FUTURE_CS_02

Requirements
This project uses only Python's standard libraries (re and string), so no additional dependencies are required. Ensure you have Python 3.x installed.

Run the Script
You can run the script directly:
bash

python password_analyzer.py

Usage
The script includes a passwordAnalyzer class and a test_password function to evaluate passwords. You can use it in two ways:
1. Run the Example
The script includes a set of test passwords. Simply execute the file to see the analysis:
bash

python password_analyzer.py

Example output:

password: Password123!
Score: 80/100
Strength: Strong
Feedback:

password: Ab1!
Score: 50/100
Strength: Weak
Feedback:
- Password should be at least 8 characters long

2. Use in Your Code
Import and use the passwordAnalyzer class in your own project:
python

from password_analyzer import passwordAnalyzer

analyzer = passwordAnalyzer()
result = analyzer.analyze_password("MyPass123!")
print(result["score"])       # e.g., 80
print(result["strength"])    # e.g., "Strong"
print(result["feedback"])    # e.g., []

How It Works
Length Check: Adds points based on password length (10 for 8-9, 20 for 10-11, 30 for 12+).

Character Types: Adds points for including:
Uppercase letters (+15)

Lowercase letters (+15)

Numbers (+15)

Special characters (+20)

Strength Rating: Calculated based on the total score:
90+: Very Strong

80-89: Strong

60-79: Moderate

40-59: Weak

Below 40: Very Weak

Feedback: Suggestions are provided if criteria are not met.

Contributing
Feel free to fork this repository and submit pull requests with improvements, such as:
Additional scoring criteria

Customizable minimum length

More detailed feedback

Fork the repo

Create a new branch (git checkout -b feature-branch)

Commit your changes (git commit -m "Add new feature")

Push to the branch (git push origin feature-branch)

Open a pull request

License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments
Built with Python’s re module for regular expression matching.




