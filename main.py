import os
import uuid

import requests
from flask import Flask, render_template, url_for, request, flash, redirect
from SPARQLWrapper import SPARQLWrapper, JSON, N3
import rdflib
from pprint import pprint
from rdflib import Graph, Namespace, BNode, Literal
from werkzeug.utils import secure_filename

from calender_to_RDF import convertto_RDF



sparql = SPARQLWrapper('http://localhost:3030/new_dataset')
sparql.setReturnFormat(JSON)
#

sparql.setCredentials("ldp", "LinkedDataIsGreat")
qres = sparql.query().convert()
UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'ttl', 'ics'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello():
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_file', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
       if 'file' not in request.files:
           flash('No file part')
           return redirect(request.url)

       file = request.files['file']

       if file.filename == '':
           flash('No selected file')
           return redirect(request.url)

       if file and allowed_file(file.filename):
           filename = secure_filename(file.filename)
           file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           return redirect(url_for('download_file', name=filename))

       rdf_calender = convertto_RDF(file.filename)


   return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
        '''

#AddEvent
@app.route('/add_event', methods=['POST'])
def add_event():
        # form data has a dictionary structure
        form_data = request.form
        #loop through the dictionary and create a Blank node for the event and upload it to the ldp
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
        rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
        SCHEMA = Namespace("https://schema.org/")
        ldp = Namespace("http://www.w3.org/ns/ldp#")
        g = Graph()
        g.bind("rdf", rdf)
        g.bind("rdfs", rdfs)
        g.bind("schema", SCHEMA)
        g.bind("ldp", ldp)

        for key in form_data.keys():
            eventName = key['eventName']
            startDate = key['startDate']
            endDate = key['endDate']
            location = key['locationName']
            attendeeName = key['attendeeName']
            comment = key['comment']
            organizer = key['organizerName']

        graph = Graph()
        event = BNode()
        uid = uuid.UUID
        graph.add((event, rdf.type, SCHEMA.Event))
        graph.add((event, SCHEMA.uid, Literal(uid)))
        graph.add((event, SCHEMA.startDate, Literal(startDate)))
        graph.add((event, SCHEMA.endDate, Literal(endDate)))
        graph.add((event, SCHEMA.location, Literal(location)))
        graph.add((event, SCHEMA.director, Literal(organizer)))
        graph.add((event, SCHEMA.name, Literal(eventName)))
        graph.add((event, SCHEMA.attendee, Literal(attendeeName)))
        headers = {
            'Content-type': 'text/turtle',
        }

        event = graph.serialize()
        url = 'https://territoire.emse.fr/ldp/sivasoumya/'
        username = "ldpuser"
        password = "LinkedDataIsGreat"
        # params = {'graph': graph_name}  # optional
        response = requests.post(url, headers=headers, auth=(username, password), data=event)
    #return 'something'

#R3 - ListUpcomingEvents
@app.route('/upcoming_events', methods=['GET'])
def upcoming_events():
    sparql.setQuery('''  
                SELECT * 
                WHERE { ?sub ?pred ?obj . } 
                LIMIT 10
            ''')

    return 'ret'

#R4 - ListEventsThatAreNotCourses(requires a property to define the type of a event)
@app.route('/list_other_events', methods=['GET'])
def list_other_events():
    sparql.setQuery('''  
                    SELECT * 
                    WHERE { ?sub ?pred ?obj . } 
                    LIMIT 10
                ''')
    return 'soemthing'

#R5 - AddAnAttendee
@app.route('/add_attendee', methods=['POST'])
def add_attendee():
    # form data has a dictionary structure
    form_data = request.form
    # loop through the dictionary and create a Blank node for the event and upload it to the ldp
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
    SCHEMA = Namespace("https://schema.org/")
    ldp = Namespace("http://www.w3.org/ns/ldp#")
    g = Graph()
    g.bind("rdf", rdf)
    g.bind("rdfs", rdfs)
    g.bind("schema", SCHEMA)
    g.bind("ldp", ldp)

    for key in form_data.keys():
        eventName = key['attendeeName']
        startDate = key['attendeeComment']


    graph = Graph()
    event = BNode()
    uid = uuid.UUID
    graph.add((event, rdf.type, SCHEMA.Event))
    graph.add((event, SCHEMA.uid, Literal(uid)))
    graph.add((event, SCHEMA.startDate, Literal(startDate)))
    graph.add((event, SCHEMA.endDate, Literal(endDate)))
    graph.add((event, SCHEMA.location, Literal(location)))
    graph.add((event, SCHEMA.director, Literal(organizer)))
    graph.add((event, SCHEMA.name, Literal(eventName)))
    graph.add((event, SCHEMA.attendee, Literal(attendeeName)))
    headers = {
        'Content-type': 'text/turtle',
    }

    event = graph.serialize()
    url = 'https://territoire.emse.fr/ldp/sivasoumya/'
    username = "ldpuser"
    password = "LinkedDataIsGreat"
    # params = {'graph': graph_name}  # optional
    response = requests.post(url, headers=headers, auth=(username, password), data=event)
    #return 'something'

def validate():
    #Write code to validate
    print("Validating the graphs")

if __name__ == "__main__":
    app.run(debug=True)
