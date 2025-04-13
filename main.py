import mistune
import os
import json
import datetime
import hashlib

from jinja2 import Template
from pygments import highlight
from pygments.lexers import get_lexer_by_name 
from pygments.formatters import HtmlFormatter

ARTICLE_DATA = []
TEMPLATES = {}

def load_templates():
    """
        Load the templates defined in templates dir in .tpl format
    """
    global TEMPLATES
    
    # Corrected path with capital T
    template_dir = "./Templates/" 
    
    for filename in os.listdir(template_dir):
        with open(template_dir + filename, 'r') as f:
            TEMPLATES.update({ filename.rstrip(".tpl"): Template(f.read()) })


def render_template(template, data):
    """ 
        Render the template 
    """
    return TEMPLATES[template].render(**data)
    
    
# list out contents and convert from markdown to html
class BlogContentRenderer(mistune.Renderer):
    
    def block_code(self, code, lang):
        global ARTICLE_DATA

        if not lang:
            return '\n<pre><code id="block_code">%s</code></pre>' % mistune.escape(code)

        if lang == "blogcfg":
            article_info = json.loads(code)
            print(article_info)
            ARTICLE_DATA.append(article_info)
            return "" 

        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter(linenos=False, cssclass="source")
        return highlight(code, lexer, formatter)


def render_articles():
    """ 
        Renders the markdown content to raw html by mistune, then applied on a
        jinja template and exported to out/
    """
    os.makedirs('./out/article', exist_ok=True)

    # Corrected path with capital C
    content_dir = './Content/'
    
    for md_filename in os.listdir(content_dir):
        
        # skip draft files from processing
        # draft files are named as <hexcode>_draft.md
        if "draft" in md_filename:
            continue

        with open(content_dir + md_filename, 'r') as f:
            
            # articles are named by their hex code or filename without extension
            article_name = md_filename.rstrip('.md')
            
            content = f.read()
            print('[+] Rendering Article ', article_name)

            # render the markdown to raw html
            renderer = BlogContentRenderer(escape=True)
            markdown = mistune.Markdown(renderer=renderer)
            raw_html = markdown(content)
            
            # Generate a hex code for the article if not present
            # Using the first 6 characters of the MD5 hash of the title
            if 'hex_code' not in ARTICLE_DATA[-1]:
                title_hash = hashlib.md5(ARTICLE_DATA[-1]['title'].encode()).hexdigest()[:6]
                ARTICLE_DATA[-1]['hex_code'] = title_hash

        # apply the article jinja template to it
        with open("./out/article/" + ARTICLE_DATA[-1]['hex_code'] + '.html', 'w') as html_f:
            html_f.write(render_template('article', {
                'meta': ARTICLE_DATA[-1],
                'content': raw_html 
            }))


def render_main_page():
    """
        Render the main page by updating with article list
    """
    # Create the output directory if it doesn't exist
    os.makedirs('./out', exist_ok=True)
    
    # Update the main page template with your information
    with open('./out/index.html', 'w') as f:
        f.write(render_template('mainpage', {'articles': ARTICLE_DATA}))


def main():
    load_templates()
    render_articles()
    render_main_page()

if __name__ == "__main__":
    main()