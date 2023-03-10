# HackerNews Sentiment Analysis

[![PyPI](https://img.shields.io/pypi/v/hn-sentiment?style=flat-square)](https://pypi.python.org/pypi/hn-sentiment/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hn-sentiment?style=flat-square)](https://pypi.python.org/pypi/hn-sentiment/)
[![PyPI - License](https://img.shields.io/pypi/l/hn-sentiment?style=flat-square)](https://pypi.python.org/pypi/hn-sentiment/)

Use VaderSentiment to analyze the sentiment of a post on HackerNews.

---

**Documentation**: [https://namuan.github.io/hn-sentiment](https://namuan.github.io/hn-sentiment)

**Source Code**: [https://github.com/namuan/hn-sentiment](https://github.com/namuan/hn-sentiment)

**PyPI**: [https://pypi.org/project/hn-sentiment/](https://pypi.org/project/hn-sentiment/)

---

## Installation

```sh
pip install hn-sentiment
```

## Usage

To run it against a single HackerNews post, copy the post id from the URL and run the following command:

```shell
hn-sentiment -s 34846476 -o target/34846476-sentiment.md
```

## Acknowledgements

- [VaderSentiment](https://pypi.org/project/vaderSentiment/)

## Development

* Clone this repository
* Requirements:
  * Python 3.7+
  * [Poetry](https://python-poetry.org/)

* Create a virtual environment and install the dependencies
```sh
poetry install
```

* Activate the virtual environment
```sh
poetry shell
```

### Validating build
```sh
make build
```

### Release process
A release is automatically published when a new version is bumped using `make bump`.
See `.github/workflows/build.yml` for more details.
Once the release is published, `.github/workflows/publish.yml` will automatically publish it to PyPI.

### License

[MIT License](LICENCE)
