Passcheck
Passcheck is a Python-based password strength testing tool that evaluates the strength of passwords using the zxcvbn library. It provides a detailed analysis of passwords, including a strength score, estimated crack time, and suggestions for improvement. The tool can test a single password or multiple passwords from a file, making it ideal for both individual use and batch processing.

Features
Password Strength Evaluation:

Scores passwords on a scale of 0 (weak) to 4 (very strong).

Estimates the time required to crack the password using offline attacks.

Provides actionable feedback to improve password strength.

Flexible Input Options:

Test a single password entered interactively.

Test multiple passwords from a file (one password per line).

Logging:

Logs password evaluation results to a file for further analysis.

User-Friendly Output:

Displays results in a clear and readable format.

Provides custom feedback based on the password score.

Installation
Clone the Repository:

bash
Copy
git clone https://github.com/AndreaKangethe/Passcheck.git
cd Passcheck
Install Dependencies:

Ensure you have Python 3 installed.

Install the zxcvbn library:

bash
Copy
pip install zxcvbn
Usage
Test a Single Password
Run the script without any arguments to test a single password:

bash
Copy
python passcheck.py
You will be prompted to enter a password securely.

Test Multiple Passwords from a File
Provide the path to a text file containing passwords (one password per line):

bash
Copy
python passcheck.py passwords.txt
Replace passwords.txt with the path to your file.

Example Password File (passwords.txt)
Copy
password123
SecurePass!2023
123456
qwerty
MyStrongPassword!2023
Output
The script will display the following for each password:

Password Value: The password being tested.

Password Score: A score from 0 (weak) to 4 (very strong).

Crack Time: Estimated time to crack the password.

Feedback: Suggestions for improving the password.

Example output:

Copy
[+] ######################
Value: password123
Password Score: 1/4
Crack Time: 1 minute
Feedback:
  - Add another word or two. Uncommon words are better.
  - This password is weak. Consider adding more complexity.
Logging
Results are logged to password_strength_log.txt by default. Each entry includes:

Timestamp

Password

Score

Crack time

Example log entry:

Copy
2023-10-10 12:34:56 - Password: password123, Score: 1/4, Crack Time: 1 minute
Command-Line Arguments
Argument	Description
<file>	Path to a file containing passwords (one per line).
(No arguments)	Test a single password entered by the user.
Example Commands
Test a single password:

bash
Copy
python passcheck.py
Test passwords from a file:

bash
Copy
python passcheck.py passwords.txt
Test passwords from a file in a different directory:

bash
Copy
python passcheck.py /path/to/passwords.txt
Contributing
Contributions are welcome! If you'd like to contribute to Passcheck, please follow these steps:

Fork the repository.

Create a new branch for your feature or bug fix.

Commit your changes.

Submit a pull request.

Please ensure your code follows the project's style and includes appropriate tests.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
zxcvbn: Password strength estimation library by Dropbox.

Support
If you encounter any issues or have questions, please open an issue on the GitHub repository.

Enjoy using Passcheck to evaluate and improve your passwords! If you find this tool useful, consider giving it a ⭐ on GitHub.
