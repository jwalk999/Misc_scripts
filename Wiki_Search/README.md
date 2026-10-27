Readme · MD
# Wikipedia Search
 
A small Python script that searches Wikipedia and saves an article's summary to a text file.
 
## Setup
 
Install the `requests` library:
 
```
pip install requests
```
 
Wikipedia requires a User-Agent. Create a file named `wiki_search_info.py` next to the script:
 
```python
USER_AGENT = "MyWikiSearch/1.0 (your_email@example.com)"
```
 
## Usage
 
```
python wiki_search.py
```
 
Enter a search term, pick a result from the list, and the article's title, description, link, intro, and categories will be saved to `wikipedia.txt`.
 
