import argparse
from pathlib import Path
import os
import pandoc

def md2pdf(path:Path):
    def md2tex(file:Path) -> str:
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

        with open(file) as f:
            content = f.read()
        
        markdown = pandoc.read(content, format="markdown")
        
        # meta = markdown[0][0]
        # title = format_meta(meta["title"])
        # author = ", ".join(format_meta(meta["author"]))
        # tags = format_meta(meta["tags"])

        # if "module" in tags:
        return markdown

    module = str(path / f"""{path.name}.md""")
    latex = md2tex(module)

    templates_path = Path(__file__).absolute().parent / "templates"

    # latex[0][0]["template"] = pandoc.types.MetaInlines([pandoc.types.Str(str(templates_path / "module.tex"))])
    latex[0][0]["documentclass"] = pandoc.types.MetaInlines([pandoc.types.Str("zettel")])
    print(latex)
    pandoc.write(latex, file="./a.pdf")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--module", "-m", help="module folder name", required=True)
    args = parser.parse_args()

    path = Path(__file__).absolute().parents[2] / "modules" / args.module
    assert path.exists()

    md2pdf(path)