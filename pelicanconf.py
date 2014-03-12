#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lita Cho'
SITENAME = u'Lita Cho'
SITEURL = 'http://litacho.github.io'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None #'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
FEED_DOMAIN = SITEURL

# Blogroll
BLOG_LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'))

LINKS = False

# Social widget
#SOCIAL = (('Facebook', 'http://facebook.com/litacho'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = "pelican-themes/subtle_lwcho"

DEFAULT_CATEGORY = 'Blog'
DISPLAY_CATEGORIES_ON_MENU = True

DELETE_OUTPUT_DIRECTORY = True

PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PAGINATED_DIRECT_TEMPLATES = (('index',))
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives',))

DISQUS_SITENAME = "litacho"

DISPLAY_PAGES_ON_MENU = False
MENU_PAGES = ['Projects', 'About']

#GITHUB_URL="http://www.github.com/litacho"
#TWITTER_USERNAME="litacho"

