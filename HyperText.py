

def findLink(rel, links):
    returnLink = ""
    for link in links:
        if link["rel"] == rel:
            returnLink = link["href"]
    return returnLink
