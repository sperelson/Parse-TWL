#Parse TWL Word List
Into a format for a Qt based Symbian game I am developing so it can look up words in real-time without impacting performance and memory usage.

##Reasons Why
Mainly due to limited power and memory on Symbian phones. I need to use an approach that guarantees extremely fast lookup times while restricting memory usage to a minimum.

I took the initial approach of compressing the words based on a simple 'how many letters in the preceeding word does the new word start with?' This didn't work well enough so I then broke up the list into multiple files. The first version broke it into files named after the first two letters and the word lookup would open the the file and read through line by line until the word was matched or not found. 

At this point you are probably thinking that this isn't good for checking the spelling of words. Since the game allows the user to enter letters to make up what could become a valid word this method actually works very well. But, when certain words are encountered, such as 'COX', the system lags a bit due to the file size and having to loop through it line by line. A few seconds lag is unnacceptable when the majority of word lookups happen without the user even realising.

Thus this version was born that breaks up the word list into thousands of files and generates a small lookup list for valid 2-letter words and for the existing folders.

##Will It Work
Sure, maybe. Turns out that Qt programs deal with packaged resources very quickly. Making the lookup for the first 2 letters comes from a small lookup table that is loaded into memory and then the 3 letter word comes from a file check that should result in practically real-time lookups of larger words as they get typed.