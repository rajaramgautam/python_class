def Greeting(strName):
    print("Welcome " + strName + "!")
def Add(n1, n2):
    try:
        answer = n1 + n2
        return answer
    except Exception:
        print("The adding function did not work.")
def Average3(n1, n2, n3):
    answer = (n1 + n2 + n3) / 3
    return answer