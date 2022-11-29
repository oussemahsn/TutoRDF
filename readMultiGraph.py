from rdflib import Dataset
from rdflib.namespace import RDF

g = Dataset()
g.parse("multiGraph.trig")

for s, p, o, g in g.quads((None, RDF.type, None, None)):
    print(s, g)


# reads multigraph RDF data file 