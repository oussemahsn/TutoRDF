from rdflib import Graph

g = Graph()
g.parse("http://www.w3.org/People/Berners-Lee/card")
g.serialize(destination="tbl.ttl")

# ce script parse les donnée de l'url et l'enregistre dans tbl.ttl