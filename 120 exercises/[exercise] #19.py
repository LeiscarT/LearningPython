def agregaString(str):
    if len(str) >= 2 and str [:2] == "Is":
        return str
        return "Is" + str

    print(agregaString("Blue"))
    print(agregaString("Isgreen"))