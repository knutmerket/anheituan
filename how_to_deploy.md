# Because I'm going to forget...

1. Do changes on development branch. Commit.
2. `poetry run make publish` OR `pelican content -s publishconf.py`
3. `ghp-import output -b gh-pages -p -m "my descriptive commit message"`

That should be it.