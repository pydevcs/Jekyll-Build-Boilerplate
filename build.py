"""
This script renders HTML templates using Jinja2 and writes the output to the 'dist' directory.
"""

import os
from jinja2 import Environment, FileSystemLoader

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

def render_template(template_name, context, output_file):
    """
    Renders a Jinja2 template with the given context and writes the output to a file.

    Args:
        template_name (str): The name of the template to render.
        context (dict): The context variables to pass to the template.
        output_file (str): The name of the file where the rendered output will be saved.
    """
    template = env.get_template(template_name)
    output = template.render(context)
    os.makedirs('dist', exist_ok=True)
    with open(f'dist/{output_file}', 'w', encoding='utf-8') as f:
        f.write(output)

# Define the pages to be generated
pages = [
    {'template': 'index.html', 'context': {'title': 'Home'}, 'output': 'index.html'}
]

# Render each page into the dist directory
for page in pages:
    render_template(page['template'], page['context'], page['output'])

print("\r\nStatic site generated.\r\n")
