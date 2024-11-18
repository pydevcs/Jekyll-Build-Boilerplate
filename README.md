# Jinja2 Static Site Generator

This repository contains a simple Python script to generate a static site using Jinja2 templates. The `build.py` script renders HTML pages from Jinja2 templates and saves the output to a `dist` directory.

## Requirements

- Python 3.x
- Jinja2

## Installation

To get started, you'll need to install the required dependencies. You can install them using `pip`:

```bash
pip install Jinja2

python build.py
```


You can test locally on at localhost:8080

```bash
cd dist

python -m http.server 8080
```