import requests

def create_container(slug):
    #api endpoint
    URL = "https://territoire.emse.fr/ldp/sivasoumya/"
    headers = {'Content-Type': 'text/turtle', 'Slug': slug}
    xml_body = """<> a <http://example.org>."""
    r = requests.post(url = URL, headers= headers, auth=('ldpuser','LinkedDataIsGreat'), data= xml_body)
    pass

def uploadfile_to_ldp():

    pass

def add_event_to_ldp():
    pass

def list_upcoming_events_ldp():
    pass

def list_other_events_ldp():
    pass

def add_attendee_to_ldp():
    pass










