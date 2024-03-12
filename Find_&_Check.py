from googletrans import Translator
def Find(path)->None:
    '''Function docstring'''
    translator = Translator()
    with open(path,'r') as file:
        result = [note for note in file.readlines() if translator.detect(note).lang=='en']
        with open('export.txt','w') as dest_file:
            dest_file.writelines(result)
Find("inputs.txt")
