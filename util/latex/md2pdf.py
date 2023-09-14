import argparse
from pathlib import Path
import os
import re
import pandoc

def format_meta(meta) -> str:
    # https://boisgera.github.io/pandoc/api/
    match(type(meta)):
        case pandoc.types.Str:
            # Str -> array with one element
            # contains str at first element
            return meta[0]
        case pandoc.types.Space:
            return " "
        case pandoc.types.MetaInlines:
            # MetaInline -> array with two elements e. g. title or MetaList item
            # contains list of Str and Space at first element
            return "".join([format_meta(string) for string in meta[0]])
        case pandoc.types.MetaList:
            # MetaList -> array with two elements e. g. author or tags
            # contains MetaInlines at first element
            return [format_meta(metainline) for metainline in meta[0]]

def md2pdf(path:Path, zettel_dir:Path, figure_dir:Path, util_dir:Path, out_dir:Path):
    module = path / f"""{path.name}.md"""

    assert module.exists()

    references = dict()

    references.update({file.replace(".md", ""): f"""sec:{file.replace(".md", "")}""" for file in os.listdir(path / "sections")})
    references.update({file.replace(".md", ""): f"""ssec:{file.replace(".md", "")}""" for file in os.listdir(path / "subsections")})

    def add_references(content):
        matches = [match.split("|")[0] for match in re.findall("!\[\[(.+?)\]\]", content)]
        references.update({match: f"""zettel:{match}""" for match in matches if match not in references})

    for file in os.listdir(path / "sections"):
        with open(path / "sections" / file) as f:
            add_references(f.read())
    for file in os.listdir(path / "subsections"):
        with open(path / "subsections" / file) as f:
            add_references(f.read())
    
    def md2tex(file:Path, zettel_type=None) -> str:
        with open(file) as f:
            content = f.read()
        
        transcludes = ([match == "!" for match in re.findall("(!?)\[\[.+?\]\]", content)])

        doc = pandoc.read(content, format="markdown")

        match zettel_type:
            case "zettel":
                latex = pandoc.write(doc, format="latex", options=[
                    f"""--resource-path={str(util_dir / "templates")}""",
                    "--template=zettel.tex"
                ])

                return latex
            case default:
                tex = pandoc.write(doc, format="latex", options=[
                    f"""--resource-path={str(util_dir / "templates")}""",
                    f"--template={default}.tex"
                ])
                
                for (i, reference), transclude in zip(enumerate(re.findall("\{\[\}\{\[\}(.+?)\{\]\}\{\]\}", tex)), transcludes):
                    reference = reference.split("\\textbar ")[0]

                    if not transclude:
                        inner = "link/to/zettel"
                    else:
                        match references[reference].split(":"):
                            case ["sec", sec]:
                                inner = md2tex(path / "sections" / f"""{sec}.md""", "sec")
                            case ["ssec", ssec]:
                                inner = md2tex(path / "subsections" / f"""{ssec}.md""", "ssec")
                            case ["zettel", zettel]:
                                inner = md2tex(zettel_dir / f"""{zettel}.md""", "zettel")

                    tex = re.sub("\{\[\}\{\[\}" + reference + ".*?\{\]\}\{\]\}", inner.replace("\\", "\\\\"), tex, 1)

                return tex
        
    tex_file = out_dir / f"""{path.name}.tex"""
    tex = md2tex(module, "module")
    tex = re.sub("\\\\includegraphics\{(.+?)\}", f"\\\\includegraphics{{{str(figure_dir)}/\\1}}", tex)

    with open(tex_file, "w") as f:
        f.write(tex)
    os.system(f"""pdflatex -output-directory {str(out_dir)} {str(tex_file)}""")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--module", "-m", help="module folder name", required=True)
    args = parser.parse_args()

    module = args.module

    root_dir = Path(__file__).absolute().parents[2]
    path = root_dir / "modules" / module
    zettel_dir = root_dir / "zettel"
    figure_dir = root_dir / "figures"
    util_dir = root_dir / "util" / "latex"
    out_dir = root_dir / "bin"


    assert path.exists()

    md2pdf(path, zettel_dir, figure_dir, util_dir, out_dir)