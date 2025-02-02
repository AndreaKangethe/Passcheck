from zxcvbn import zxcvbn
import pprint
import getpass
import sys
import logging
from datetime import datetime


def get_password_strength(password):
    """
    Evaluate the strength of a password using zxcvbn.
    """
    result = zxcvbn(password)
    return result


def print_password_result(result):
    """
    Print the password evaluation result in a readable format.
    """
    print("\n[+] ######################")
    print(f"Value: {result['password']}")
    print(f"Password Score: {result['score']}/4")
    print(f"Crack Time: {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}")
    print("Feedback:")
    for suggestion in result['feedback']['suggestions']:
        print(f"  - {suggestion}")
    print_custom_feedback(result['score'])


def print_custom_feedback(score):
    """
    Provide custom feedback based on the password score.
    """
    if score == 0:
        print("  - This password is extremely weak. Avoid using common words or patterns.")
    elif score == 1:
        print("  - This password is weak. Consider adding more complexity.")
    elif score == 2:
        print("  - This password is moderate. It could be stronger with additional characters or words.")
    elif score == 3:
        print("  - This password is strong. Good job!")
    elif score == 4:
        print("  - This password is very strong. Excellent!")


def log_password_result(result, log_file):
    """
    Log the password evaluation result to a file.
    """
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')
    logging.info(f"Password: {result['password']}, Score: {result['score']}/4, Crack Time: {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}")


def test_single_password(log_file=None):
    """
    Test the strength of a single password entered by the user.
    """
    password = getpass.getpass("[?] Enter your password: ")
    result = get_password_strength(password)
    print_password_result(result)
    if log_file:
        log_password_result(result, log_file)


def test_multiple_passwords(password_file, log_file=None):
    """
    Test the strength of multiple passwords from a file.
    """
    try:
        with open(password_file, 'r') as passwords:
            for password in passwords:
                password = password.strip('\n')
                if password:  # Skip empty lines
                    result = get_password_strength(password)
                    print_password_result(result)
                    if log_file:
                        log_password_result(result, log_file)
    except FileNotFoundError:
        print(f"[!] Error: The file '{password_file}' was not found.")
    except PermissionError:
        print(f"[!] Error: You do not have permission to read the file '{password_file}'.")
    except Exception as e:
        print(f"[!] An unexpected error occurred: {e}")


def main():
    """
    Main function to handle command-line arguments and execute the script.
    """
    if len(sys.argv) == 2:
        # Test passwords from a file
        password_file = sys.argv[1]
        log_file = "password_strength_log.txt"  # Default log file
        print(f"[*] Testing passwords from file: {password_file}")
        print(f"[*] Logging results to: {log_file}")
        test_multiple_passwords(password_file, log_file)
    elif len(sys.argv) == 1:
        # Test a single password
        log_file = "password_strength_log.txt"  # Default log file
        print(f"[*] Logging results to: {log_file}")
        test_single_password(log_file)
    else:
        print("Usage: python test_password_strength.py <file> (for a file containing passwords) or \n"
              "python test_password_strength.py (for a single password.)")


if __name__ == "__main__":
    main()
