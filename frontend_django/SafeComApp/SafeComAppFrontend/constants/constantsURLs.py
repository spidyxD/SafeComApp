##################################
# BASE
BASEURL = "http://localhost:8000/api"
##################################
# PERSON
PERSON_CREATE = "{}/{}".format(BASEURL, "person/create")
PERSON_LIST = "{}/{}".format(BASEURL, "persons")
PERSON_GET = "{}/{}".format(BASEURL, "person/")
PERSON_UPDATE = "{}/{}".format(BASEURL, "person/update/")
PERSON_DELETE = "{}/{}".format(BASEURL, "person/delete/")
PERSON_VISITS = "{}/{}".format(BASEURL, "person/visits/")
# ##################################
# VEHICLE
VEHICLE_CREATE = "{}/{}".format(BASEURL, "vehicle/create")
VEHICLE_LIST = "{}/{}".format(BASEURL, "vehicles")
VEHICLE_GET = "{}/{}".format(BASEURL, "vehicle/")
VEHICLE_UPDATE = "{}/{}".format(BASEURL, "vehicle/update/")
VEHICLE_DELETE = "{}/{}".format(BASEURL, "vehicle/delete/")
VEHICLE_VISITS = "{}/{}".format(BASEURL, "vehicle/visits/")
# ##################################
# VISIT
VISIT_CREATE = "{}/{}".format(BASEURL, "recordVisit/create")
VISIT_LIST = "{}/{}".format(BASEURL, "recordVisits")
VISIT_GET = "{}/{}".format(BASEURL, "recordVisit/update/")
VISIT_UPDATE = "{}/{}".format(BASEURL, "recordVisit/update/")
VISIT_DELETE = "{}/{}".format(BASEURL, "recordVisit/delete/")
VISIT_VISITS = "{}/{}".format(BASEURL, "recordVisit/visits/")
VISIT_EXIT = "{}/{}".format(BASEURL, "recordVisit/exit/")
# ##################################
# BLACK LIST
BLACKLIST_CREATE = "{}/{}".format(BASEURL, "blacklist/create")
BLACKLIST_LIST = "{}/{}".format(BASEURL, "blacklist/")
BLACKLIST_GET = "{}/{}".format(BASEURL, "blacklist/")
BLACKLIST_UPDATE = "{}/{}".format(BASEURL, "blacklist/update/")
BLACKLIST_DELETE = "{}/{}".format(BASEURL, "blacklist/delete/")
BLACKLIST_VISITS = "{}/{}".format(BASEURL, "blacklist/visits/")