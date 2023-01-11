from pyshacl import validate


pyshacl = "${pyshacl}"
shape_graph = "C:\\Users\\Siva Ratnam Pachava\\OneDrive\\Desktop\\SemW P\\SemWeb\\EVENT.ttl"
data_graph = "C:\\Users\\Siva Ratnam Pachava\\OneDrive\\Desktop\\SemW P\\SemWeb\\rdf_cal.ttl"
results = validate(
    data_graph,
    shacl_graph=shape_graph,
    data_graph_format="ttl",
    shacl_graph_format="ttl",
    inference="rdfs",
    debug=True,
    serialize_report_graph="ttl",
    )

conforms, report_graph, report_text = results

"conforms", conforms, results, dir(report_graph), repr(report_graph)