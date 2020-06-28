import typer

from ssg.site import Site

def __main__(source = "content", dest="dist"):
    config = {"source" : "source", "dest" : "dist"}
    site = Site(**config)
    site.build()

typer.run(__main__)
