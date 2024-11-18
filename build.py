import os
import json
from jinja2 import Environment, FileSystemLoader

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# Define a function to render a template with given context and write to a file
def render_template(template_name, context, output_file):
    template = env.get_template(template_name)
    output = template.render(context)
    os.makedirs('dist', exist_ok=True)
    with open(f'dist/{output_file}', 'w') as f:
        f.write(output)

# Define the pages to be generated
pages = [
    {'template': 'index.html', 'context': {'title': 'Home'}, 'output': 'index.html'}
]

# Render each page into the dist directory
for page in pages:
    render_template(page['template'], page['context'], page['output'])

print("\r\nStatic site generated.\r\n")
