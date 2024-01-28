def solution(myString):
    return "".join([s.upper() if s=='a' or s=='A' else s.lower()  for s in myString])