def getresponseconvert(responses, key):
    jsonresponse = []
    for response in responses:
        jsonresponse.append(response[key])

    return jsonresponse
