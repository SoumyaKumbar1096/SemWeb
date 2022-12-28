# Calender

### Main Objectives
* Design a Calender  
  - It should be available online
  - It should be represented in a standard vocabulary
* Develop an Application to :
  * Create calender events
  * Query calender events
  * Validate calender events

[Note]: Write a report explaining your choices, functionalities etc

### Territoire LDP
* Create a LDP container at https://www.w3.org/TR/ldp/#ldpc

### Technical Requirements 
* R1 - Application must download any ICS file and turn it into RDF
  * [Note]: Use identifiers from Plateforme Territoire's LDP to denote rooms
* R2 - Add events to personal calender hosted on Platforme Territoire's LDP
  * [Note]: Events can generated from ICS file, extracted from Web pages or manually written
* R3 - List of upcoming events on a given date
  * [Node]: This feature should include at least one SPARQL query
* R4 - List events taking place in Saint-Etienne that are not courses
  * [Note]: use SPARQL
* R5 - Modify an existing event to indicate that someone has attended it
* R6 - Validate the information defined for a given event.
  * [Note]: use SHACL
* R7 - Validate the information defined for CPS2 course
  * [Note]: it should either be organized by UJM or EMSE and be held in one of the university locations of Saint-Étienne
* R8 - Discover other resources and link a resource describing an event to another resource describing the same event
  * [Note]: The property used for linking should be owl:sameAs
* R9 - Take owl:sameAs statements into account when answering SPARQL queries: if two resources are declared to be the same, they must both be part of an answer.


