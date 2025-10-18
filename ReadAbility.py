import math
import string

Sentence = input("Text: ")
LetterCounter = 0
WordCounter = 0
ReadingLevel = 0
SentenceCount = 0
l = 0
s = 0

for i in range (len(Sentence)):
    if Sentence[i] == ' ':
        WordCounter += 1
    elif Sentence[i] == '.' or Sentence[i] == '!' or Sentence[i] == '?':
        SentenceCount += 1
    elif Sentence[i].isalpha():
        LetterCounter += 1

if SentenceCount == 0:
    SentenceCount = 1

WordCounter = WordCounter + 1
l = (LetterCounter / WordCounter) * 100
s = (SentenceCount / WordCounter) * 100


ReadingLevel = 0.0588 * l - 0.296 * s - 15.8

if ReadingLevel <= 0:
    print("Before Grade 1\n")
elif ReadingLevel >= 16:
    print("Grade 16+\n")

print(f"Grade {round(ReadingLevel)}")
