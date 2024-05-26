# your code goes here!
class Anagram:
    def __init__(self,anagram):
        self.anagram = anagram
        pass

    def match(self,list):
        anagram = [letter for letter in self.anagram]
        returnList = []
        for element in list:
            element = [letter for letter in element]
            if sorted(element) == sorted(anagram):
                element = "".join(element)
                returnList.append(element)
        return returnList    

listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana','stelni']) )       