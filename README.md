**URL** Shortener

A lightweight, in-memory **URL** shortener implemented in Python. This project demonstrates core system design concepts for **URL** shortening, including deterministic hash generation using UUIDv5 and compact encoding using Base62.

Features

Deterministic Generation: Uses uuid.uuid5 with a **URL** namespace so that identical long URLs always generate the same unique short code without duplicate entries.

Base62 Encoding: Converts numeric IDs into compact, alphanumeric short strings (0-9, a-z, A-Z).

In-Memory Mapping: Keeps track of mappings using Python dictionaries for fast lookups during shortening and redirection.

Interactive **CLI**: A simple command-line interface to test shortening URLs and resolving them back to their original destinations.

### Project Structure

**URL**-Shortener/ ├── urlshortener.py    # Contains the URLShortener core logic class └── main.py            # Interactive **CLI** application script

### How It Works

Shorten **URL** (shorten_url):

Generates a **128**-bit integer **UID** from the input **URL** using UUIDv5.

Checks if the **UID** already exists in memory to avoid duplicate generation.

Converts the **UID** into a compact alphanumeric string using Base62 encoding (_generate_url).

Appends the string to a base domain ([https://mytinyurl.com/](https://mytinyurl.com/)) and stores the mapping.

Redirect / Resolve (redirect):

Takes a short **URL** and looks it up in the internal mapping to return the original long **URL**.

### Getting Started

Prerequisites

Python 3.10 or higher (required for match-case syntax in the **CLI**).

Running the Application

Clone the repository:

git clone [https://github.com/gkrvkoushik/**URL**-Shortener.git](https://github.com/gkrvkoushik/**URL**-Shortener.git) cd **URL**-Shortener

Run the interactive script:

python main.py

Follow the on-screen menu prompts:

Option 1: Enter a long **URL** to generate its shortened version.

Option 2: Enter the shortened **URL** to retrieve the original long **URL**.

Option 3: Exit the program.
