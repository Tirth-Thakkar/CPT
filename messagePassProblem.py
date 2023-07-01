def messagepass(message, array):
    # Defining length of message and array
    messageLength = len(message)
    arrayLength = len(array)
    response = ""
    
    for value in array:
        # If value is greater than or equal to message length, return "invalid"
        if value >= messageLength:
            return "invalid"
        
        # Recipient finder, based on array value
        response += message[value]
    
    return response

print(messagepass("cdeo", [3, 2, 0, 1]))
print(messagepass("cdeenetpi", [5, 2, 0, 1, 6, 4, 8, 3, 7]))

