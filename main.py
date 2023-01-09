import os
from flask import Flask, render_template, url_for, request, flash, redirect
from SPARQLWrapper import SPARQLWrapper, JSON, N3
import rdflib
from pprint import pprint
from rdflib import Graph
from werkzeug.utils import secure_filename

from calender_to_RDF import convertto_RDF



sparql = SPARQLWrapper('http://localhost:3030/new_dataset')
sparql.setReturnFormat(JSON)
#


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




# #Convert into RDF
# @app.route('/convertIntoRdf', methods=['GET'])
# def convert_to_rdf():
#     return 'something'

#AddEvent
@app.route('/addEvent', methods=['POST'])
def add_event():
    sparql.setQuery('''  
            Create * 
            WHERE { ?sub ?pred ?obj . } 
            LIMIT 10
        ''')
    return 'soemthing'

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
@app.route('/listOtherEvents', methods=['GET'])
def list_other_events():
    sparql.setQuery('''  
                    SELECT * 
                    WHERE { ?sub ?pred ?obj . } 
                    LIMIT 10
                ''')
    return 'soemthing'

#R5 - AddAnAttendee
@app.route('/addAttendee', methods=['POST'])
def add_attendee():
    sparql.setQuery('''  
                    UPDATE * 
                    WHERE { ?sub ?pred ?obj . } 
                    LIMIT 10
                ''')
    return 'something'


if __name__ == "__main__":
    app.run(debug=True)
