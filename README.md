# Impledge_Recruitment

## Compound Word Finder

### Overview
This Python program is designed to find the longest and second-longest compound words in a list of words provided in a text file. A compound word is a word made up of two or more smaller words. The program uses a recursive approach to determine if a word is compound by breaking it down into smaller words.

### Design Decisions
- The program uses a function `is_compound_word` that recursively checks if a word can be divided into smaller words found in the input word list.
- To make the search efficient, it first sorts the words in the input file by length in descending order, allowing it to check the longest words first.
- It utilizes a set to store the words for faster lookups during the recursive checks.
- The code measures the processing time to provide performance information.

### Instructions
1. Place your list of words in a text file. Each word should be on a separate line.

2. Save the text file and make a note of the file path.

3. Ensure you have Python installed on your system.

4. Download the Python script from the provided source.

5. Open the Python script in a code editor or IDE.

6. Locate the `file_path` variable in the script and set it to the file path of your text file.

7. Save the script.

8. Open your command prompt or terminal.

9. Navigate to the directory where the Python script is located.

10. Run the script by executing the command: `python main.py` 

11. The program will process the file, find the longest and second-longest compound words, and display them, along with the processing time.

12. The results will be shown on the console.

### Ouput
```
Longest compound word: ethylenediaminetetraacetates
Second longest compound word: electroencephalographically
Processing time: 0.05171656608581543 seconds


---

