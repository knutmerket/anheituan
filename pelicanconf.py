AUTHOR = 'Balthazar'
SITENAME = 'Anheituan'
SITESUBTITLE = "粗种有细"
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Oslo'

DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'

THEME = 'themes/elegant'

DISPLAY_CATEGORIES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 12

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

TYPOGRIFY = True
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'pymdownx.tilde': {},
    },
    'output_format': 'html5',
}

ARTICLE_PATHS = ['teas']
PAGE_PATHS = ['pages']
#DEFAULT_CATEGORY = None  # Optional: avoids fallback 'Uncategorized'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

# Optional: override URL structure just for teas
ARTICLE_URL = 'teas/{slug}.html'
ARTICLE_SAVE_AS = 'teas/{slug}.html'

# Tell Pelican to treat 'featured_image' as a known metadata field
ARTICLE_METADATA_FIELDS = ['title', 'date', 'slug', 'category', 'tags', 'status', 'featured_image', 'price']
