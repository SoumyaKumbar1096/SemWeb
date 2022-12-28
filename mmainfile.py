from icalendar import Calendar
from rdflib import Graph, URIRef, Namespace, Literal, BNode


rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SCHEMA = Namespace("https://schema.org/")


g = Graph()
g.bind("rdf", rdf)
g.bind("rdfs", rdfs)
g.bind("schema", SCHEMA)


schedule = URIRef("https://ci.mines-stetienne.fr/cps2/schedule/")

g.add((schedule, rdf.type, SCHEMA.Thing))
g.add((schedule, rdf.type, SCHEMA.schedule))

with open('ADECal.ics', 'r') as file:
    ecal = Calendar.from_ical(file.read())
    for component in ecal.walk():
     event = BNode()
     if component.name == "VEVENT":
        
        g.add((schedule, SCHEMA.subjectOf, event))
        g.add((event, rdf.type, SCHEMA.Event))
        g.add((event, SCHEMA.description, Literal("first class of sematic web coures")))
        g.add((event, SCHEMA.name, Literal(component.get("summary"))))
        g.add((event, SCHEMA.location, Literal(component.get("location"))))
        g.add((event, SCHEMA.startDate, Literal(component.decoded("dtstart"))))       
        g.add((event, SCHEMA.endDate, Literal(component.decoded("dtend"))))
        g.add((event, SCHEMA.director, Literal(component.decoded("DESCRIPTION"))))
        g.add((event, SCHEMA.duration, Literal("03:30")))
        g.add((event, SCHEMA.Attendee, Literal("23")))
  
        
    file.close()
print(g.serialize(r"D:\Master's subjects\M2_Subjects_SEM_1\Semantic Web\Sample Graph\caloutput.ttl", format="ttl"))
