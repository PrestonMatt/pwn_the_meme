"""
    Generate a password that is hard to guess.
    THIS IS NOT MY OWN CODE
    Source:
    https://www.reddit.com/r/ProgrammerHumor/comments/13ahhou/ah_yes_tough_to_break_for_hackers/
    https://i.imgur.com/lefs1lW.png
"""
import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*\/?"

Use_for = lower_case + upper_case + number + symbols

length_for_pass = 8

password = "".join(random.sample(Use_for, length_for_pass))

print("Your generated password is: %s" % password)
