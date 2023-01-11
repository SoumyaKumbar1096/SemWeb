import requests
from  rdflib import Graph,RDF,Namespace, Literal

url = 'https://territoire.emse.fr/ldp/sivasoumya/'
file_path = "C:\\Users\\Siva Ratnam Pachava\\OneDrive\Desktop\\SemW P\\SemWeb\\rdf_cal.ttl"
graph_name = 'rdf_cal.ttl'
username = "ldpuser"
password = "LinkedDataIsGreat"

rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SCHEMA = Namespace("https://schema.org/")

g = Graph().parse("C:\\Users\\Siva Ratnam Pachava\\OneDrive\Desktop\\SemW P\\SemWeb\\rdf_cal.ttl")
g.bind("rdf", rdf)
g.bind("rdfs", rdfs)
g.bind("schema", SCHEMA)

for event in g.subjects(rdf.type,SCHEMA.Event):
    print(event)
    
    startDate  = g.value(event,SCHEMA.startDate)
    endDate = g.value(event,SCHEMA.endDate)
    location = g.value(event,SCHEMA.location)
    director  = g.value(event,SCHEMA.director)
    uid = g.value(event,SCHEMA.uid)
    name  = g.value(event,SCHEMA.name)
    
    graph = Graph()
    
    graph.add((event, rdf.type, SCHEMA.Event))
    graph.add((event, SCHEMA.uid, Literal(uid)))
    graph.add((event, SCHEMA.startDate, Literal(startDate)))   
    graph.add((event, SCHEMA.endDate, Literal(endDate)))
    graph.add((event, SCHEMA.location, Literal(location)))   
    graph.add((event, SCHEMA.director, Literal(director)))     
    graph.add((event, SCHEMA.name, Literal(name)))     
    
    headers = {
        'Content-type': 'text/turtle',
    }
    
    event  = graph.serialize()

    params = {'graph': graph_name}  # optional
    response = requests.post(url, headers=headers,  auth=(username, password), params=params, data=event)
    # #print(response.text)