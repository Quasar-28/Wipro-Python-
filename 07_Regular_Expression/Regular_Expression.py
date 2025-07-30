# Regular Expression Assignments : 

# Q1. Write a program to find check if a string has only octal digits. Given string ['789', '123', '004']
# Sol.
import re
pattern = r'^[0-7]+$'
strings = ['789', '123', '004']
for string in strings : 
    result = re.match(pattern , string)
    if result : 
        print(f"{string} has only octal digits")
    else : 
        print(f"{string} has not only octal digits")


"""
Q2.
Extract the user id, domain name and suffix from the following email addresses.
emails = zuck@facebook.com , sunder33@google.com , jeff42@amazon.com
"""
# Sol.
import re
emails = "zuck@facebook.com, sunder33@google.com, jeff42@amazon.com"
pattern = r'(\w+)@(\w+)\.(\w+)'
matches = re.findall(pattern, emails)
for user_id, domain, suffix in matches:
    print(f"User ID: {user_id}, Domain: {domain}, Suffix: {suffix}")


"""
Q3.
Split the following irregular sentence into proper words
sentence : A, very very; irregular_sentence
expected output : A very very irregular sentence
"""
# Sol.
import re
sentence = "A, very very; irregular_sentence"
cleaned = re.sub(r'[^\w\s]', ' ', sentence) 
cleaned = re.sub(r'_', ' ', cleaned)       
cleaned = re.sub(r'\s+', ' ', cleaned).strip()
print(cleaned)


"""
Q4.
Clean up the following tweet so that it contains only the user's message. That is, remove all URLs,hashtags, mentions, punctuations, RTs and CCs.
tweet = Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats
desired_output = Good advice What I would do differently if I was learning to code today
"""
# Sol.
import re
tweet = """Good advice! RT @TheNextWeb: What I would do differently if I was learning "
"to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"""
tweet = re.sub(r'http\S+', '', tweet)
tweet = re.sub(r'\bRT\b', '', tweet)
tweet = re.sub(r'\bcc:?', '', tweet, flags=re.IGNORECASE)
tweet = re.sub(r'[@#]\w+', '', tweet)
tweet = re.sub(r'[^\w\s]', '', tweet)
cleaned_tweet = re.sub(r'\s+', ' ', tweet).strip()
print(cleaned_tweet)


"""
Q5.
Extract all the text portions between the tags from the following HTML page:
https://raw.githubusercontent.com/selva86/datasets/master/sample.html
Code to retrieve the HTML page is given below:
import requests
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
r.text # html text is contained here
desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 'This is a new paragraph! ', 'This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics. ']
"""
# Sol.
import urllib.request
import re
url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
text_list = re.findall(r'>([^<]+)<', html)
cleaned = [text.strip() for text in text_list if text.strip()]
print(cleaned)


"""
Q6.
Given below list of words, identify the words that begin and end with the same character.
civic
trust
widows
maximum
museums
aa
as
"""
# Sol.
import re
words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
pattern = re.compile(r'^(.).*\1$')
matching_words = [word for word in words if pattern.match(word)]
print("Words that begin and end with the same character:")
print(matching_words)

