from flask import Flask, render_template, url_for
from SPARQLWrapper import SPARQLWrapper, JSON, N3

import rdflib
from pprint import pprint

from rdflib import Graph

sparql = SPARQLWrapper('http://localhost:3030/new_dataset')
sparql.setReturnFormat(JSON)
#
sparql.setQuery('''  
        SELECT * 
        WHERE { ?sub ?pred ?obj . } 
        LIMIT 10

    ''')

qres = sparql.query().convert()

########## printing the query result ##################3
pprint(qres)
# for result in qres['results']['bindings']:
#      print(result['obj'])
#     lang, value = result['object']['xml:lang'], result['object']['value']
#     print(f'Lang: {lang}\tValue: {value}')

#################### creating rdf from the result ##############

# g = Graph()
# g.parse(data=qres, format='n3')
# print(g.serialize(format='ttl').decode('u8'))


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


#
# #Convert into RDF
# @app.route('/convertIntoRdf', methods=['GET'])
# def convert_to_rdf():
#     return 'something'
#
# #AddEvent
# @app.route('/addEvent', methods=['POST'])
# def add_event():
#     return 'soemthing'
#
# #ListUpcomingEvents
# @app.route('/upcoming_events', methods=['GET'])
# def upcoming_events():
#     # gets the first 3 geological ages
#     # from a Geological Timescale database,
#     # via a SPARQL endpoint
#
#     return 'ret'
#
# #ListEventsThatAreNotCourses(requires a property to define the type of a event)
# @app.route('/listOtherEvents', methods=['GET'])
# def list_other_events():
#     return 'soemthing'
#
# #AddAnAttendee
# @app.route('/addAttendee', methods=['POST'])
# def add_attendee():
#     return 'something'
#

if __name__ == "__main__":
    app.run(debug=True)
