# journal-topic-organiser
A little bit of python that sorts journal entries into topics

## how it works 
The general idea is that you write journal entries and keep them all in a folder. Inside the entries, you can have topic headings to organise your thoughts, study, make shopping lists, whatever you want really. Then, when you want to create files that sort these topics, you run the script and choose the folder where the journal entries are stored. having folders in the main folder is fine. 

## things to keep in mind
the scripts looks for "---" on either side of your topic heading to sift out topics into topic text files so make sure to name you topics like that each time. for example, "---hunting for decent pubs---".
adding DDMMYY at the end of your entries - the current script looks for the date at the end of your journal entries and sorts them accordingly. make sure to include this format at the end of your txt files e.g. myjournalentry130924.txt. 
the date range - before you run the script, make sure to change the start and end date so the script will only sort entries within this range.

##thanks 
Big inspo for this came from Derek Sivers. Here's an article on the [Benefits of a daily diary and topic journals](https://sive.rs/dj)

## collabs
If anyone is keen to jam on the code have a go! I've been using this for a while and it really works for me but any ideas are always welcome. Happy Journalling :)

## license

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License - see the [LICENSE](LICENSE) file for details.

You are free to use, share, and adapt this work for non-commercial purposes, as long as you give appropriate credit and indicate if changes were made.
