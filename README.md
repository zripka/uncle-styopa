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
2. Identify: total word count, total unique word count
3. Identify counts by individual word 
4. Display histogram
5. Based on frequency, identify a priority cutoff: if a repeated word makes up more than 0.X% of the text, include it in the priority list (ranked word frequency, most to least)
6. All other words: include them after the priority list, in the order they appear in the story

### file output
Anki can bulk import "notes" (flashcards) from a .csv. My end result is a folder of .csv files, one for each day: I can just drag and drop.
1. Take the first word from the above list and add it to a .csv file in a folder
2. Name the folder YYYY-MM-DD.csv for today's date
3. Create another .csv file with 1 word in it until the end of the current month
4. Do the same for each day in the next month, but add 2 words to each file
5. In the third month, continue, but add 3 words to each file and continue in the Fibonacci sequence (5 words per day the next month, 8, 13, etc.)

## results
This doesn't belong in the readme but here we are.

| Frequency value (FV) | Number of unique words at this FV | Rolling sum of unique words | Cumulative percentage of unique words | Cumulative percentage of the story |
|----------------------|-----------------------------------|-----------------------------|---------------------------------------|------------------------------------|
| 132                  | 1                                 | 1                           | 0.06%                                 | 3.70%                              |
| 97                   | 1                                 | 2                           | 0.11%                                 | 6.42%                              |
| 81                   | 1                                 | 3                           | 0.17%                                 | 8.69%                              |
| 67                   | 1                                 | 4                           | 0.23%                                 | 10.57%                             |
| 65                   | 1                                 | 5                           | 0.28%                                 | 12.39%                             |
| 64                   | 1                                 | 6                           | 0.34%                                 | 14.18%                             |
| 53                   | 2                                 | 8                           | 0.46%                                 | 17.15%                             |
| 49                   | 1                                 | 9                           | 0.51%                                 | 18.53%                             |
| 29                   | 2                                 | 11                          | 0.63%                                 | 20.15%                             |
| 28                   | 1                                 | 12                          | 0.68%                                 | 20.94%                             |
| 26                   | 3                                 | 15                          | 0.85%                                 | 23.12%                             |
| 25                   | 1                                 | 16                          | 0.91%                                 | 23.82%                             |
| 22                   | 1                                 | 17                          | 0.97%                                 | 24.44%                             |
| 17                   | 3                                 | 20                          | 1.14%                                 | 25.87%                             |
| 15                   | 1                                 | 21                          | 1.20%                                 | 26.29%                             |
| 14                   | 3                                 | 24                          | 1.37%                                 | 27.47%                             |
| 13                   | 1                                 | 25                          | 1.42%                                 | 27.83%                             |
| 12                   | 1                                 | 26                          | 1.48%                                 | 28.17%                             |
| 11                   | 3                                 | 29                          | 1.65%                                 | 29.09%                             |
| 10                   | 6                                 | 35                          | 1.99%                                 | 30.77%                             |
| 9                    | 3                                 | 38                          | 2.17%                                 | 31.53%                             |
| 8                    | 4                                 | 42                          | 2.39%                                 | 32.43%                             |
| 7                    | 9                                 | 51                          | 2.91%                                 | 34.19%                             |
| 6                    | 9                                 | 60                          | 3.42%                                 | 35.71%                             |
| 5                    | 22                                | 82                          | 4.67%                                 | 38.79%                             |
| 4                    | 29                                | 111                         | 6.32%                                 | 42.04%                             |
| 3                    | 88                                | 199                         | 11.34%                                | 49.44%                             |
| 2                    | 248                               | 447                         | 25.47%                                | 63.34%                             |
| 1                    | 1308                              | 1755                        | 100.00%                               | 100.00%                            |
