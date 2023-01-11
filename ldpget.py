import os
from flask import Flask, render_template, url_for, request, flash, redirect
from SPARQLWrapper import SPARQLWrapper, JSON, N3
import rdflib
from pprint import pprint
from rdflib import Graph
from werkzeug.utils import secure_filename
from calender_to_RDF import convertto_RDF

sparql = SPARQLWrapper('https://territoire.emse.fr/ldp/maximeaurelien/')
sparql.setReturnFormat(JSON)
sparql.setCredentials("ldpuser", "LinkedDataIsGreat")


sparql.setQuery("""
            SELECT * 
            WHERE { ?sub ?startDate "2022-09-27"^^xsd:date.
                    }
            LIMIT 10           
            """  
)
try:
    qres = sparql.queryAndConvert()
    
    for r in qres["results"]["bindings"]:
        print(r)
except Exception as e :
    print(e)
