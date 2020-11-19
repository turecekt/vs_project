from lxml import html
from lxml.html.clean import Cleaner
from lxml.html.clean import clean_html


class Htmlhelper:
    def stripTags(self, data):
        cleaner = Cleaner(page_structure=True,
                          meta=True,
                          embedded=True,
                          links=True,
                          style=True,
                          processing_instructions=True,
                          inline_style=True,
                          scripts=True,
                          javascript=True,
                          comments=True,
                          frames=True,
                          forms=True,
                          annoying_tags=True,
                          remove_unknown_tags=True,
                          safe_attrs_only=True,
                          safe_attrs=frozenset(['src', 'color', 'href', 'title', 'class', 'name', 'id']),
                          remove_tags=('span', 'font')
                          )

        tree = html.fromstring(data)
        clean_tree = cleaner.clean_html(tree)
        return clean_tree.text_content()  # .strip()
        # return clean_tree

    def remove_html_markup(self, s):

        tag = False
        quote = False
        out = ""
        links = ""

        for c in s:
            if c == '<' and not quote:
                tag = True
            elif c == '>' and not quote:
                tag = False
            elif (c == '"' or c == "'") and tag:
                quote = not quote
            elif not tag:
                out = out + c

        return out
