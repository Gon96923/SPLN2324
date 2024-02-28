import jinja2
from glob import glob

mods = glob('*.py')

if len(mods) >= 1:
    name = mods[0].split('.')[0]
else:
    name = input("Modulo?")

pp = jinja2.Template('''

[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "{{name}}"
authors = [
    {name = "{{autor}}", email = "{{email}}"},
]
classifiers = [
    "License :: OSI Approved :: MIT License",
]
requires-python = ">=3.8"
dynamic = ["version", "description"]

dependencies = [
    "jjcli"
]

[project.scripts]
{{name}} = "{{name}}:main"

                     
''')

r = pp.render({"name":name, "autor":"Gonçalo","email":"goncalo@gmail.com"})


with open('pyproject.toml','w') as f:
    f.write(r)
