#ex:3.10
def noVowel(sent):
    for i in sent:
        if i in 'aeiouAEIOU':
            return False
        return True

sent=str(input('enter text:'))
noVowel(sent)