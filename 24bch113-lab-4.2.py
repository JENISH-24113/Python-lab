def lowercase(input_str):
    result = ""
    for char in input_str:
        if 'A' <= char <= 'Z':  
            result += chr(ord(char) + 32)  
        else:
            result += char
    return result


def uppercase(input_str):
    result = ""
    for char in input_str:
        if 'a' <= char <= 'z': 
            result += chr(ord(char) - 32) 
        else:
            result += char
    return result


def togglecase(input_str):
    result = ""
    for char in input_str:
        if 'a' <= char <= 'z':  
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z': 
            result += chr(ord(char) + 32)
        else:
            result += char  
    return result