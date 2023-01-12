from icalendar import Calendar
from rdflib import Graph, URIRef, Namespace, Literal, BNode

def convertto_RDF(fileName):
        file = "static\\uploads\\" + fileName
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
        rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
        SCHEMA = Namespace("https://schema.org/")
        ldp = Namespace("http://www.w3.org/ns/ldp#")

        g = Graph()
        g.bind("rdf", rdf)
        g.bind("rdfs", rdfs)
        g.bind("schema", SCHEMA)
        g.bind("ldp", ldp)


        #schedule = URIRef("https://ci.mines-stetienne.fr/cps2/schedule/")
        schedule = URIRef("https://territoire.emse.fr/ldp/sivasoumya/")

        g.add((schedule, rdf.type, SCHEMA.Thing))
        g.add((schedule, rdf.type, SCHEMA.schedule))
        g.add((schedule, SCHEMA.description, Literal("The graph contains the rdf representation of our university Calender events")))
        #with open('ADECal.ics', 'r') as f:
        with open(file, 'r') as f:
            ecal = Calendar.from_ical(f.read())
            for component in ecal.walk():
             event = BNode()
             if component.name == "VEVENT":

                g.add((schedule, ldp.containes, event))
                g.add((event, rdf.type, SCHEMA.Event))
                g.add((event, SCHEMA.description, Literal("first class of sematic web coures")))
                g.add((event, SCHEMA.name, Literal(component.get("summary"))))
                g.add((event, SCHEMA.location, Literal(component.get("location"))))
                g.add((event, SCHEMA.startDate, Literal(component.decoded("dtstart"))))
                g.add((event, SCHEMA.endDate, Literal(component.decoded("dtend"))))
                g.add((event, SCHEMA.director, Literal(component.decoded("DESCRIPTION"))))
                #g.add((event, SCHEMA.duration, Literal("03:30")))
                #g.add((event, SCHEMA.Attendee, Literal("23")))

            f.close()
        rdfFilePath = "static\\rdfFiles\\" + fileName + "_rdf"
        print(g.serialize(rdfFilePath, format="ttl"))
        return rdfFilePath






