"""Advanced Task 3: Clean Message Toolkit
- Collect a message that might contain extra spaces or mixed casing.
- Use at least three different string methods (e.g. strip, title, replace, upper) to tidy the message.
- Print the original and cleaned versions so the difference is obvious.
- Extension: show the message length before and after cleaning.
"""

raw_message = input("Type a message to tidy: ")
raw_message = raw_message.lower()
msgList = raw_message.split()

for x in range (0, len(msgList)):
    if x == 0:
        word = msgList[x].title()
        cleaned_message = word
    elif msgList[x] == "i":
        cleaned_message = cleaned_message + " I"
    else:
        word = msgList[x]
        cleaned_message = cleaned_message + " " + word

print(cleaned_message)

# TODO: apply a sequence of string methods to produce a cleaned_message
# Example methods: strip, title, replace, lower, upper
# TODO: display the original and cleaned messages
# Extension: display the character counts for each version
