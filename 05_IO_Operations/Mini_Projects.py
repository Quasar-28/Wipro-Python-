# Mini Project :-
"""
Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the place and time where you have to go and meet him.
He challenges you to find it out without seeing the content of the file. He has
given hints to find it. Let's surprise him by breaking the challenge with our python code.
Hints to find the secret message:
1. The number of lines in the file tells you the meeting time. Note: 1 <= number of lines <= 24.If the number of lines is exceeding 12, you need to convert it to 12 hourformat. For example, If the number of lines is 15, then the meeting time is 3 PM.
If the number of lines is 10, then the meeting time is 10 AM.
2. The word appearing for the maximum number of times tells you the meeting place.
Note: Meeting place will be a street name.
For example,
. If the word Oxford appears for the maximum number of times, then meeting place is Oxford Street.
. If the word Park appears for the maximum number of times, then meeting place is Park Street.
"""
from collections import Counter
filename = "sample.txt"
with open(filename, 'r') as file:
    lines = file.readlines()
    num_lines = len(lines)
    all_words = " ".join(lines).split()
word_counts = Counter(all_words)
most_common_word, _ = word_counts.most_common(1)[0]
if num_lines > 12:
    meeting_hour = num_lines % 12
    meridiem = "PM"
else:
    meeting_hour = num_lines
    meridiem = "AM"
if meeting_hour == 0:
    meeting_hour = 12
print(f"Meeting Time: {meeting_hour} {meridiem}")
print(f"Meeting Place: {most_common_word} Street")
