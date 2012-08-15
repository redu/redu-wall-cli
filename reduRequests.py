from HyperText import findLink

getmeUrl = "http://www.redu.com.br/api/me"
getSpacesUrl = "{0}/spaces"
getStatusesUrl = "http://www.redu.com.br/api/spaces/{0}/statuses/timeline"


def getMe(requestClient):
    return requestClient.getLink(getmeUrl)


def getEnrollmentData(requestClient):
    data = getMe(requestClient)
    link = findLink("enrollments", data["links"])
    data = requestClient.getLink(link)
    return data


def getCourseLinks(requestClient):
    data = getEnrollmentData(requestClient)
    links = []
    for enrollments in data:
        link = findLink("course", enrollments["links"])
        links.append(link)
    return links


def getSpaceData(requestClient):
    courseList = getCourseLinks(requestClient)
    spaces = []
    for course in courseList:
        tempList = requestClient.getLink(getSpacesUrl.format(course))
        for space in tempList:
            spaces.append(space)
    return spaces


def getTimeline(requestClient, spaceId):
    r = requestClient.getLink(getStatusesUrl.format(spaceId))
    return r
