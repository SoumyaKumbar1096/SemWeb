
import requests
from rdflib import Graph, Namespace, URIRef, BNode, Literal

URL = "https://territoire.emse.fr/ldp/sivasoumya/"
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SCHEMA = Namespace("https://schema.org/")
schedule = URIRef("https://territoire.emse.fr/ldp/sivasoumya/")

def create_container(slug):
    #api endpoint
    headers = {'Content-Type': 'text/turtle', 'Slug': slug}
    xml_body = """<> a <http://example.org>."""
    r = requests.post(url=URL, headers=headers, auth=('ldpuser','LinkedDataIsGreat'), data=xml_body)
    pass

def uploadfile_to_ldp(rdffile):
    # Get the file
    #with open(rdffile, 'r') as f:
        #rf =


# Loop through each triple set
# upload each triple set to the ldp.
    pass

def add_event_to_ldp():
    # Create a BNode of these events
    g = Graph()
    g. bind("rdf", rdf)
    g.bind("rdfs", rdfs)
    g.bind("schema", SCHEMA)


    g.add((schedule, rdf.type, SCHEMA.Thing))
    g.add((schedule, rdf.type, SCHEMA.schedule))

    event = BNode()
    #associate Literals coming from Frontend to Literals here
    g.add((schedule, SCHEMA.subjectOf, event))
    g.add((event, rdf.type, SCHEMA.Event))
    g.add((event, SCHEMA.description, Literal("first class of semantic web coures")))
    g.add((event, SCHEMA.name, Literal("summary")))
    g.add((event, SCHEMA.location, Literal("location")))
    g.add((event, SCHEMA.startDate, Literal("dtstart")))
    g.add((event, SCHEMA.endDate, Literal("dtend")))
    g.add((event, SCHEMA.director, Literal("DESCRIPTION")))


    URL = "https://territoire.emse.fr/ldp/sivasoumya/"
    headers = {'Content-Type': 'text/turtle'}
    xml_body = """<> a <http://example.org>."""
    r = requests.post(url=URL, headers=headers, auth=('ldpuser', 'LinkedDataIsGreat'), data=xml_body)

    pass

def list_upcoming_events_ldp():
# SPARQLWrapper query to the ldp
    pass

def list_other_events_ldp():
# SPARQLWrapper query to the ldp
    pass

def add_attendee_to_ldp():
    # create an Attendee Node.
    # Associate information provided in the frontend to the Literals in this node
    URL = "https://territoire.emse.fr/ldp/sivasoumya/"
    headers = {'Content-Type': 'text/turtle'}
    xml_body = """<> a <http://example.org>."""
    r = requests.post(url=URL, headers=headers, auth=('ldpuser', 'LinkedDataIsGreat'), data=xml_body)

# POST attendee in the event
    pass









