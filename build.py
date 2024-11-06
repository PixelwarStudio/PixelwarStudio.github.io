from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("template"))
env.trim_blocks = True
env.lstrip_blocks = True

IMAGE_FOLDER = Path("img")

def write(temp, out, **kwargs):
    template = env.get_template(temp)
    with open(out, "w") as out_file:
        out_file.write(template.render(kwargs))

if __name__ == "__main__":
    with open("data/projects.yml", "r") as f:
        projects = yaml.safe_load(f)
    projects.sort(key=lambda p: p["year"], reverse=True)
    for project in projects:
        if "id" in project:
            project_image_folder = IMAGE_FOLDER / project["id"]
            project["images"] = list(project_image_folder.iterdir())
    write("index.j2", "index.html", projects=projects)
    write("imprint.j2", "imprint.html")
    write("disclaimer.j2", "disclaimer.html")
    write("tree.j2", "tree.html")
