# uncle-styopa
I'm learning Russian using Anki. It's possible to import a lot of text at once into Anki, but if I do a lot on the same day, say a few thousand words and their translations, it would be months before any of the other material I study shows up again. This project will take in a text file ([Дядя Стёпа](https://en.wikipedia.org/wiki/Uncle_Styopa)) and separate it into multiple .csv files, each for a specific date. That way, I can learn at a good pace without a firehose of new words hitting me all at once.

## approach
I'll "ship" the smallest possible working pieces, Agile-style.

## non-programmatic workflow
1. Open the text file containing the Дядя Стёпа poem
2. Pick a word
3. Open a browser
4. Navigate to a translation app
5. Translate the word
6. Write a note in Anki according to the formula "In Russian, _слово_ means _word_."

## structure
The program should identify which words are important to learn first and prioritize them, after which it should follow the order they appear in the story.

### analysis
1. Read text file
2. Identify total word count
3. Identify counts by individual word (display histogram)
4. Based on frequency, identify a priority cutoff: if a repeated word makes up more than 0.X% of the text, include it in the priority list (ranked word frequency, most to least)
5. All other words: include them after the priority list, in the order they appear in the story

### file output
Anki can bulk import "notes" (flashcards) from a .csv. My end result is a folder of .csv files, one for each day: I can just drag and drop.
1. Take the first word from the above list and add it to a .csv file in a folder
2. Name the folder YYYY-MM-DD.csv for today's date
3. Create another .csv file with 1 word in it until the end of the current month
4. Do the same for each day in the next month, but add 2 words to each file
5. In the third month, continue, but add 3 words to each file and continue in the Fibonacci sequence (5 words per day the next month, 8, 13, etc.)
