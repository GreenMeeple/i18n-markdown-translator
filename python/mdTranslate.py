import os
import re
import json
import requests
from lxml import html, etree
from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.deflist import deflist_plugin
from mdit_py_plugins.tasklists import tasklists_plugin
from mdit_py_plugins.field_list import fieldlist_plugin
from markdownify import markdownify
from dotenv import load_dotenv

# Translator API setup
load_dotenv()
API_KEY = os.getenv("TRANSLATOR_KEY")
REGION = os.getenv("TRANSLATOR_REGION")
ENDPOINT = "https://api.cognitive.microsofttranslator.com"
HEADERS = {
    "Ocp-Apim-Subscription-Key": API_KEY,
    "Ocp-Apim-Subscription-Region": REGION,
    "Content-Type": "application/json"
}

def extract_code_blocks(markdown):
    code_blocks = []

    def replacer(match):
        code_blocks.append(match.group(0))
        return f"[[[CODEBLOCK{len(code_blocks) - 1}]]]"

    pattern = r"```[\w+-]*\n[\s\S]*?\n```"
    modified_md = re.sub(pattern, replacer, markdown)
    return modified_md, code_blocks

def restore_code_blocks(text, code_blocks):
    for i, block in enumerate(code_blocks):
        text = text.replace(f"[[[CODEBLOCK{i}]]]", block)
    return text

def mdToHtml(input):
    # Initialize MarkdownIt with desired plugins
    md = (
        MarkdownIt('commonmark', {'html': False, 'linkify': True, 'typographer': False})
        .use(front_matter_plugin)
        .use(footnote_plugin)
        .use(tasklists_plugin)
        .use(deflist_plugin)
        .use(fieldlist_plugin)
        .enable('table')
        .enable('strikethrough')
    )

    # Read input Markdown
    with open(input, "r", encoding="utf-8") as f:
        content = f.read()

    # Convert Markdown → HTML
    html_output = md.render(content)

    # Parse HTML to modify code blocks for language preservation
    tree = html.fromstring(html_output)
    for code in tree.xpath('//pre/code'):
        class_attr = code.get('class', '')
        if 'language-' in class_attr:
            lang = class_attr.split('language-')[-1]
            code_text = code.text or ''
            fenced = f"```{lang}\n{code_text.rstrip()}\n```"
            new_node = html.fromstring(f"<p>{fenced}</p>")
            code.getparent().getparent().replace(code.getparent(), new_node)

    # Serialize modified HTML back to string
    rawHtml = etree.tostring(tree, encoding='unicode', method='html')
    return rawHtml

def translate_text(text: str, source_lang = 'en', target_lang = 'yue') -> str:
    body = [{"Text": text}]
    try:
        response = requests.post(
            f"{ENDPOINT}/translate?api-version=3.0&from={source_lang}&to={target_lang}",
            headers=HEADERS,
            params={"textType": "html"},
            data=json.dumps(body)
        )
        response.raise_for_status()
        return response.json()[0]["translations"][0]["text"]
    except requests.RequestException as e:
        print("Translation failed:", e)
        return text  # Fallback to original

def mdTranslate(input = "./testcases/example.md", source_lang = 'en', target_lang = 'yue'):
    # Read input
    with open(input, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract and protect code blocks
    safe_markdown, code_blocks = extract_code_blocks(content)

    # Convert to HTML
    md = (
        MarkdownIt('commonmark', {'html': False, 'linkify': True, 'typographer': False})
        .use(front_matter_plugin)
        .use(footnote_plugin)
        .use(tasklists_plugin)
        .use(deflist_plugin)
        .use(fieldlist_plugin)
        .enable('table')
        .enable('strikethrough')
    )
    raw_html = md.render(safe_markdown)
    wrapped_html = f"<html><body>{raw_html}</body></html>"

    # Translate content
    if target_lang == 'yue':
        wrapped_html = translate_text(wrapped_html, source_lang, 'zh-Hant')
        source_lang = 'zh-Hant'

    translated_html = translate_text(wrapped_html, source_lang, target_lang)

    # Convert back to markdown
    markdown_back = markdownify(translated_html)

    # Restore code blocks
    markdown_back = restore_code_blocks(markdown_back, code_blocks)

    # Clean-up
    markdown_back = (
        markdown_back
        .replace('“', '"')
        .replace('”', '"')
        .replace("'''", '```')
        .replace('（', '(')
        .replace('）', ')')
        .replace('<表', '<table ')
        .replace('&lt;表','<table ')
    )

    # Write result
    output_path = f"./{target_lang}/{input}"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_back)
