from rdflib import Graph

g = Graph()
g.parse("rdfDATA.nt")

print(len(g))
# prints: 2

import pprint
for stmt in g:
    pprint.pprint(stmt)

# reads a simple rdf data file
