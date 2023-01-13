from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper('https://territoire.emse.fr/ldp/')
sparql.setReturnFormat(JSON)
sparql.setCredentials("ldpuser", "LinkedDataIsGreat")

eventdate = "2023-01-13"
sparql.setQuery(f"""
    PREFIX ldp: <http://www.w3.org/ns/ldp#>
    PREFIX ns0: <https://carbonldp.com/ns/v1/platform#> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
    PREFIX ns1: <https://schema.org/>
    
    SELECT ?id
    WHERE{{
        <https://territoire.emse.fr/ldp/spsk/> ldp:hasMemberRelation ldp:member ;
        ldp:member ?id.
        ?id ns1:startDate "{eventdate}"^^xsd:date.
        
    }}
    LIMIT 10
    """ 
                )

try:
    qres = sparql.queryAndConvert()
    
    for r in qres["results"]["bindings"]:
        print(r)
except Exception as e :
    print(e)
