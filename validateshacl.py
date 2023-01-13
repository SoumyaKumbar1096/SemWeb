from pyshacl import validate


shape_graph = "EVENT.ttl"
data_graph = "rdf_calender.ttl"


r = validate(data_graph,
      shacl_graph=shape_graph,
      inference='rdfs',
      data_graph_format="ttl",
      shape_graph_format="ttl",
      debug=False,
      report_graph="ttl"
      )
conforms, report_graph, results_text = r

print("Conforms: ",conforms)
print("Report Graph: ", report_graph)
print("Results text: ", results_text)