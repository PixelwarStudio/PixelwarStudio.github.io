import yaml
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("template"))

def write(temp, out, **kwargs):
    template = env.get_template(temp)
    out_file = open(out, "w")
    out_file.write(template.render(kwargs))
    out_file.close()

if __name__ == "__main__":
    projects = yaml.load(open("data/projects.yml", "r"))
    print(projects)
    write("index.j2", "index.html", projects=projects)
    write("imprint.j2", "imprint.html")
    write("disclaimer.j2", "disclaimer.html")
