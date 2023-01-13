from pyshacl import validate


shape_graph = "C:\\Users\\Siva Ratnam Pachava\\OneDrive\\Desktop\\SemW P\\SemWeb\\EVENT_F.ttl"
data_graph = "C:\\Users\\Siva Ratnam Pachava\\OneDrive\\Desktop\\SemW P\\SemWeb\\rdf_cal_F.ttl"

r = validate(data_graph,
      shacl_graph=shape_graph,
      inference='rdfs',
      data_graph_format="ttl",
      shape_graph_format="ttl",
      debug=False,
      report_graph_format="ttl"
      )
conforms, report_graph, results_text = r

print("Conforms: ",conforms)
print("Report Graph: ", report_graph)
print("Results text: ", results_text)