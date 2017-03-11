# Single category feed maker for Blox
===========

This is simple Python script to extract posts belonging to single category on
Blox.pl RSS feed. Created, because Blox.pl does not support feeds for a single
category right now, at least not for new templates.

It fetches original RSS feed, and tries to preserve as much as possible.

Usage
---------
* clone this repository
* pip install -r requirements.txt
* python rss_from_category_blox.py --url FEED_URL --category CATEGORY  > /output.xml
