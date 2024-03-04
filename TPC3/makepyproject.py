import jinja2
from glob import glob

mods = glob('*.py')

if len(mods) > 1 and mods[0] != 'makepyproject.py':
    name = mods[0]
else:
    name = input("Modulo?\n")

name = name.replace('.py','')
autor = input("Autor?\n")
email = input("E-mail?\n")

dep = []
nD = input("Numero de dependencias?\n")
for i in range(int(nD)):
    dep.append(input("Dependencia?\n"))



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
    {% for i in dep %}
    "{{i}}",
    {% endfor %}
]

[project.scripts]
{{name}} = "{{name}}:main"

                     
''')

r = pp.render({"name":name, "autor":autor,"email":email,"dep":dep})



with open('pyproject.toml','w') as f:
    f.write(r)
