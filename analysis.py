import pandas as pd 
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

file_path = 'Дядя Стёпа.txt'

with open(file_path, encoding="utf8") as file:
    text = file.read()

text = text.split()

text_series = pd.Series(text)

text_series = text_series.str.strip()
text_series = text_series.str.lower()

text_series = text_series.str.replace(r'[^\w\s]+', '')
text_series = text_series.where(text_series.str.isalnum())
text_series = text_series.dropna()
word_count = text_series.count()

unique_words = pd.Series(text_series.unique())
unique_words = unique_words.sort_values()
unique_word_count = unique_words.count()


def print_newlines():
	counter = 0
	while counter < 4:
		print("\n")
		counter = counter + 1

def calculate_frequency_proportion(frequency):
	#divide the given frequency by the overall number of words, multiply by 100 to get a percentage
	frequency = float(frequency)
	frequency_proportion = frequency/3568.0*100.0
	return frequency_proportion

print_newlines()
print("---------------------- REPORT ----------------------")
print(f"Total word count: {word_count}")
print(f"Total unique word count: {unique_word_count}")
print("How many words occur only once?")
text_series_frequency = text_series.value_counts()
print(text_series_frequency.where(text_series_frequency == 1).count())
print("How many words occur more than once?")
print(text_series_frequency.where(text_series_frequency > 1).count())
print("What frequency values are present in this text?")
unique_frequency_values = pd.Series(text_series_frequency.unique())
print(*unique_frequency_values.astype(str).values.flatten().tolist(), sep=", ")
print("For each frequency, what proportion of the overall text does one word represent?")
freq_prop_df = pd.DataFrame(unique_frequency_values)
freq_prop_df[1] = freq_prop_df[0].apply(calculate_frequency_proportion)
freq_prop_df.columns = ['Frequency', 'Percentage of overall text']
print(freq_prop_df.to_string(index=False))
print("In other words, each time I learn a word that appears once in the text, I learn about 0.03% of the story. On the other hand, if I learn a word that appears 53 times in the text, I can learn almost 1.5% of the story in one shot.") 
print("So now the question is: at what point (percentage) is it worth it to prioritize the more frequent words? The tradeoff is that reading (and learning) in the story order is more pleasant, but learning by descending order of frequency is faster and more efficient. So where is the cutoff?")
print("How many words are associated with each frequency value? (This matters because it's only up to a certain absolute number of words that I'm willing to prioritize for efficiency's sake an out-of-context list over the actual story.")
word_count_with_given_frequency = text_series.value_counts().value_counts(sort=False)
print(word_count_with_given_frequency)
print("So it seems like the choice is pretty clear. Between the word that appears 132 times down to the nine words that appear 6 times, there are really only a few dozen words to learn. That's an easy cutoff, but since I'm enjoying this I'll do a little more analysis.")
frequency_word_count_df = pd.DataFrame()
frequency_word_count_df['Frequency value (FV)'] = word_count_with_given_frequency.index
frequency_word_count_df['Number of unique words at this FV'] = word_count_with_given_frequency.tolist()
frequency_word_count_df['Rolling sum of unique words'] = frequency_word_count_df['Number of unique words at this FV'].cumsum()
frequency_word_count_df['Number of words at this FV incl. duplicates'] = frequency_word_count_df.apply(lambda x : x['Frequency value (FV)'] * x['Number of unique words at this FV'], axis = 1)
frequency_word_count_df['Rolling sum'] = frequency_word_count_df['Number of words at this FV incl. duplicates'].cumsum()
frequency_word_count_df['Cumulative percentage of unique words'] = frequency_word_count_df.apply(lambda x : x['Rolling sum of unique words'] / 1755 * 100, axis=1)
frequency_word_count_df['Cumulative percentage of the story'] = frequency_word_count_df.apply(lambda x : x['Rolling sum'] / word_count * 100, axis=1)
#print(frequency_word_count_df.filter(items=['Frequency value (FV)', 'Number of unique words at this FV', 'Rolling sum of unique words','Cumulative percentage of unique words','Cumulative percentage of the story']).to_csv())
text_series_counts = text_series.value_counts()
mask = text_series_counts > 2
text_series_counts = text_series_counts[mask]
print(f"Here are the {text_series_counts.count()} words that appear in the story three or more times, in descending order of frequency.")
print(text_series_counts.to_markdown())

print_newlines()