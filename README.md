# Basic OSINT Domain Scanner

A lightweight Python script that verifies if an email domain is disposable, temporary, or potentially malicious using the open Kickbox API.

## Features
- Extracts the domain directly from any given email address.
- Integrates with the open.kickbox.com API.
- Parses JSON responses to determine domain status.

## Prerequisites
- Python 3.x
- `requests` library

## Usage
Run the script and provide the target email when prompted:
`python osint.py`