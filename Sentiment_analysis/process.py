

from Sentiment_analysis import preprocessing

def get_wordcounts(x):
	return preprocessing._get_wordcounts(x)

def get_charcounts(x):
	return preprocessing._get_charcounts(x)

def get_avg_wordlength(x):
	return preprocessing._get_avg_wordlength(x)

def get_stopwords_counts(x):
	return preprocessing._get_stopwords_counts(x)

def get_hashtag_counts(x):
	return preprocessing._get_hashtag_counts(x)

def get_mentions_counts(x):
	return preprocessing._get_mentions_counts(x)

def get_digit_counts(x):
	return preprocessing._get_digit_counts(x)

def get_uppercase_counts(x):
	return preprocessing._get_uppercase_counts(x)

def cont_exp(x):
	return preprocessing._cont_exp(x)

def get_emails(x):
	return preprocessing._get_emails(x)

def remove_emails(x):
	return preprocessing._remove_emails(x)

def get_urls():
	return preprocessing._get_urls(x)

def remove_urls(x):
	return preprocessing._remove_urls(x)

def remove_rt(x):
	return preprocessing._remove_rt(x)

def remove_special_chars(x):
	return preprocessing._remove_special_chars(x)

def remove_html_tags(x):
	return preprocessing._remove_html_tags(x)

def remove_accented_chars(x):
	return preprocessing._remove_accented_chars(x)

def remove_stopwords(x):
	return preprocessing._remove_stopwords(x)

def make_base(x):
	return preprocessing._make_base(x)

def get_value_counts(df, col):
	return preprocessing._get_value_counts(df, col)

def get_word_freqs(df, col):
	return preprocessing._get_value_counts(df, col)

def remove_common_words(x, freq, n=20):
	return preprocessing._remove_common_words(x, freq, n)

def remove_rarewords(x, freq, n=20):
	return preprocessing._remove_rarewords(x, freq, n)

def spelling_correction(x):
	return preprocessing._spelling_correction(x)

def remove_dups_char(x):
	return preprocessing._remove_dups_char(x)

def get_basic_features(df):
	return preprocessing._get_basic_features(df)

def get_ngram(df, col, ngram_range):
	return preprocessing._get_ngram(df, col, ngram_range)