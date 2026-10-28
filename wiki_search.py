import re

import requests

from wiki_search_info import USER_AGENT

API_URL = "https://en.wikipedia.org/w/api.php"

# User Agent header is required by Wikipedia to prevent misuse
# You can create a constant USER_AGENT below and delete the import above

def search_wikipedia(search_term):
    """Return a list of search matches from Wikipedia."""
    params = {
        "action": "query",
        "list": "search",
        "srsearch": search_term,
        "srlimit": 5,
        "srinfo": "totalhits|suggestion",
        "format": "json",
        "formatversion": 2,
    }
    headers = {"User-Agent": USER_AGENT}

    response = requests.get(API_URL, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()

    results = data.get("query", {}).get("search", [])
    if not results:
        raise ValueError(f"No results found for {search_term}")
    return results


def choose_page(search_term):
    matches = search_wikipedia(search_term)
    if len(matches) == 1:
        return matches[0]

    print(f"Found {len(matches)} matches for '{search_term}':")
    for i, match in enumerate(matches, start=1):
        print(f"{i}. {match['title']}")

    while True:
        choice = input("Choose result (#): ")
        if choice.isdigit() and 1 <= int(choice) <= len(matches):
            return matches[int(choice) - 1]
        print(f"Please enter a number from 1 to {len(matches)}.")



def clean_snippet(snippet):
    """Remove HTML tags like <span class="searchmatch"> from a snippet."""
    return re.sub(r"<.*?>", "", snippet)


def get_page_details(pageid):
    """Return description, intro text, categories, image, and URL for one page."""
    params = {
        "action": "query",
        "pageids": pageid,
        "prop": "description|extracts|categories|pageimages|info",
        "exintro": 1,          # only the intro section, not the whole article
        "explaintext": 1,      # plain text instead of HTML
        "clshow": "!hidden",   # skip hidden maintenance categories
        "cllimit": 10,         # up to 10 categories
        "inprop": "url",       # adds the page's full URL
        "format": "json",
        "formatversion": 2,
    }
    headers = {"User-Agent": USER_AGENT}

    response = requests.get(API_URL, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()

    return data["query"]["pages"][0]

# ==================================================================================
# ==================== I got the data, now time to format it =======================
# ==================================================================================



import textwrap


def format_paragraphs(text, width=80):
    """Wrap each paragraph to a fixed width and put a blank line between them."""
    paragraphs = text.split("\n")
    wrapped = []
    for paragraph in paragraphs:
        if paragraph.strip():  # skip empty lines
            wrapped.append(textwrap.fill(paragraph, width))
    return "\n\n".join(wrapped)


def add_bars(text, width=76):
    """Wrap each line in '| ... |' with the right side lined up."""
    border = "+" + "-" * (width + 2) + "+"
    bar_lines = [border]
    for line in text.split("\n"):
        bar_lines.append(f"| {line.ljust(width)} |")
    bar_lines.append(border)
    return "\n".join(bar_lines)


search_input = input("Please enter search term: ")
try:
    page = choose_page(search_input)
    details = get_page_details(page["pageid"])
except ValueError as e:
    print(e)
else:
    title = details["title"]
    lines = [
        title,
        "=" * len(title),
        details.get("description", "No description"),
        details["fullurl"],
        "",
        "_" * 80,
        add_bars(format_paragraphs(details.get("extract", "No intro text"), width=76), width=76),
        "_" * 80,
        "",
        "Categories",
        "----------",
    ]

    for category in details.get("categories", []):
        name = category["title"].removeprefix("Category:")
        url = "https://en.wikipedia.org/wiki/" + category["title"].replace(" ", "_")
        lines.append(f"- {name}")
        lines.append(f"  {url}")

    with open("wikipedia.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Saved '{title}' to wikipedia.txt")