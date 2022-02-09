from typing import Optional

import tornado.web


class Entry(tornado.web.UIModule):
    def embedded_css(self) -> Optional[str]:
        return ".entry {margin-bottom: 1em;}"

    def render(self, entry, show_comments=False) -> str:
        return self.render_string('module-entry.html', entry=entry, show_comments=show_comments)