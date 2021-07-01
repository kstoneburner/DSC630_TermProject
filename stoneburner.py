#//***************************************
#//*** Apply Common Cleanup operations
#//***************************************
#//*** In anticpation that I'll be re-using text cleanup code. I'm adding some robustness to the function.
#//*** Adding kwargs to disable features that default to true.
#//*** Whether an action is skipped or executed is based on a boolean value stored in action_dict.
#//*** Key values will default to true. If code needs to be defaulted to False, a default_false list can be added later
#//*** All Boolean kwarg keya are stored in kwarg list. This speeds up the coding of the action_dict.
#//*** As Kwargs are added 
def mr_clean_text(input_series, input_options={}):
    
    #//*** import time library
    try:
        type(time)
    except:
        import time
    
    #//*** Start Timing the process
    start_time = time.time()
    
    #//*** Add some data validation. I'm preparing this function for additional use. I'm checking if future users (ie future me)
    #//*** may throw some garbage at this function. Experience has taught me to fail safely wherever possible.

    #//*** All kwargs are listed here. These initialize TRUE by default.
    key_list = [ "lower", "newline", "html", "remove_empty", "punctuation" ]
    
    #//*** Build Action Dictionary
    action_dict = { } 
    
    #//*** Build the keys from kwarg_list and default them to TRUE
    for key in key_list:
        action_dict[key] = True
        
    #//*** Loop through the input kwargs (if any). Assign the action_dict values based on the kwargs:
    for key,value in input_options.items():
        print(key,value)
        action_dict[key] = value
    
    
    #//*************************************************************************
    #//*** The Cleanup/Processing code is a straight lift from DSC550 - Week02
    #//*************************************************************************
    #//*** Convert to Lower Case, Default to True
    if action_dict["lower"]:
        input_series = input_series.str.lower()
    
   
    #//*** Remove New Lines
    if action_dict["newline"]:
        #//*** Rmove \r\n
        input_series = input_series.str.replace(r'\r?\n',"")

        #//*** Remove \n new lines
        input_series = input_series.str.replace(r'\n',"")

    #//*** Remove html entities, observed entities are &gt; and &lt;. All HTML entities begin with & and end with ;.
    #//*** Let's use regex to remove html entities
    if action_dict["html"]:
        input_series = input_series.str.replace(r'&.*;',"")

    #//*** Remove the empty lines
    if action_dict["remove_empty"]:
        input_series = input_series[ input_series.str.len() > 0]

    #//*** Remove punctuation
    if action_dict["punctuation"]:
        #//*** Load libraries for punctuation if not already loaded.
        #//*** Wrapping these in a try, no sense in importing libraries that already exist.
        #//*** Unsure of the cost of reimporting libraries (if any). But testing if library is already loaded feels
        #//*** like a good practice
        try:
            type(sys)
        except:
            import sys

        try:
            type(unicodedata)
        except:
            import unicodedata
        
        #//*** replace Comma and Period with a space.
        for punct in [",",".","$"]:
            input_series = input_series.str.replace(punct," ")

        #//*** Remove punctuation using the example from the book
        punctuation = dict.fromkeys(i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith('P') )
        input_series = input_series.str.translate(punctuation)

    print(f"Text Cleaning Time: {time.time() - start_time}")

    return input_series
#//*** Remove Stop words from the input list
def remove_stop_words(input_series):
    
    #//*** This function removes stop_words from a series.
    #//*** Works with series.apply()
    def apply_stop_words(input_list):

        #//*** Load Stopwords   
        for word in input_list:
            if word in stop_words:
                input_list.remove(word)
        return input_list

    #//*** import nltk if needed
    try:
        type(nltk)
    except:
        import nltk
        
    stopwords = nltk.corpus.stopwords

    #//*** Stopwords requires an additional download
    try:
        type(stopwords)
    except:
        nltk.download('stopwords')


    #//*** import time library
    try:
        type(time)
    except:
        import time

    #//*** Start Timing the process
    start_time = time.time()


    #//*** The stop_words include punctuation. Stop Word Contractions will not be filtered out.
    stop_words = []

    #//*** Remove apostrophies from the stop_words
    for stop in stopwords.words('english'):
        stop_words.append(stop.replace("'",""))

    
    #//*** Remove Stop words from the tokenized strings in the 'process' column
    #input_series = input_series.apply(remove_stop_words,stop_words)
    
    input_series = input_series.apply(apply_stop_words)

    print(f"Stop Words Time: {time.time() - start_time}")
    
    return input_series
#//*** Tokenize a Series containing Strings.
#//*** Breaking this out into it's own function for later reuse.
#//*** Not a lot of code here, but it helps to keep the libraries localized. This creates standarization for future
#//*** Stoneburner projects. Also has the ability to add functionality as needed.

def tokenize_series(input_series):
    
    try:
        type(nltk)
    except:
        import nltk
    
    word_tokenize = nltk.tokenize.word_tokenize 
    
    #//*** import time library
    try:
        type(time)
    except:
        import time
    
    #//*** Start Timing the process
    start_time = time.time()
    try:
        input_series = input_series.apply(word_tokenize)
    except:
        #//*** Try again is punkt not downloaded
        nltk.download('punkt')
        input_series = input_series.apply(word_tokenize)
        
    
    print(f"Tokenize Time: {time.time() - start_time}")
    
    return input_series