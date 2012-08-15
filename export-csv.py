from reduRequests import getSpaceData, getTimeline
from HttpClient import HttpClient
from writer import exportTimeline

if __name__ == '__main__':
    #add your consumer keys here
    client = HttpClient("consumer_key",
        "consumer_secret")

    print ("Follow this url: {0}".format(client.getAuthorizeUrl()))
    pin = raw_input("Enter pin:")
    client.initClient(pin)
    print ("fetching spaces data...")
    ids = []
    names = []
    spaceData = getSpaceData(client)
    print ("You own the following spaces:")

    for count, space in enumerate(spaceData):
        name = space["name"].encode("UTF-8")
        print ("{0}){1}".format(count, name))
        ids.append(space['id'])
        names.append(name)

    choice = raw_input("Please choose the desired space:")
    print ("ok, now getting timeline data...")
    timelineData = getTimeline(client, ids[int(choice)])
    print ("done!")
    f = open("{0}.csv".format(names[int(choice)]), "w")
    print ("writing file")
    exportTimeline(f, timelineData)
    f.close()
    print ("yay! we fineshed exporting your file")
