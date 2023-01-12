import requests
from  rdflib import Graph,Namespace, Literal, URIRef, XSD
import uuid

container = 'https://territoire.emse.fr/ldp/spsk/'
username = "ldpuser"
password = "LinkedDataIsGreat"
schedule_url = "https://territoire.emse.fr/ldp/spsk/ade60323032322d3230323353542d455449454e4e452d383032372d332d30/"



rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SCHEMA = Namespace("https://schema.org/")
SCHEMAComments = Namespace("https://schema.org/UserComments")
SCHEMAPerson = Namespace("https://schema.org/Person")

graph= Graph()

graph.bind("rdf", rdf)
graph.bind("rdfs", rdfs)
graph.bind("schema", SCHEMA)

#schedule = URIRef("https://territoire.emse.fr/ldp/spsk/sample")

schedule = URIRef( schedule_url )


person = "ss"
comment = "I am attending"

person_graph = Graph()

graph.add((schedule, SCHEMA.attendee, person_graph))  
graph.add((person_graph, SCHEMAPerson.givenName, Literal(person, datatype = XSD.string)))  
graph.add((person_graph, SCHEMAComments.commentText, Literal(comment, datatype = XSD.string)))
headers = {
        'Content-type': 'text/turtle',
    }
    
event  = graph.serialize()
#print(event)

response = requests.get(schedule_url, headers=headers,  auth=(username, password))
#eventList = response.content.decode('UTF-8').split(";")
eventList = response.text
# for triple in eventList:
#     print(triple)
print(eventList)

# response = requests.delete(schedule_url, headers=headers,  auth=(username, password))

# response = requests.get(schedule_url, headers=headers,  auth=(username, password))
# print("Event after deleting",response.content.decode('UTF-8'))