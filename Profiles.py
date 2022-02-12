import csv
    
class File:
    #faz tratamento do arquivo csv onde ficará salvo os perfis

    def __init__(self, file_csv = 'file.csv', items = dict()):
        self._CreateFile(file_csv)

        self.saves = self._ReadFile(file_csv)
        self.file = file_csv
        self.items = items
        

    def _CreateFile(self, filename):       
        try:
            a = open(filename, 'r')
            
        except FileNotFoundError:
            a = open(filename, 'wt+')

        finally:
            a.close()


    def _ReadFile(self, filename):
        a = open(filename,'r')

        reader = csv.reader(a)
        saves = list()
    
        for line in reader: saves.append(line)

        a.close()

        return saves


    def _SaveProfile(self):
        self.list = [self.name, self.items]

        a = open(self.file, 'a', newline='')

        recorder = csv.writer(a)
        recorder.writerow(self.list)

        a.close()

        self.__init__(self.file, self.items)

        return self.LoadProfile(-1)


    def _SaveProgress(self):
        a = open(self.file, 'w', newline='')

        recorder = csv.writer(a)

        for i in self.saves: recorder.writerow(i)

        a.close()



class NewProfile(File):
    #cria, carrega e deleta perfis salvos

    def __init__(self, file_csv = 'file.csv', items = dict()):
        File.__init__(self, file_csv, items)
    

    def CreateProfile(self, name):
        name = name.strip()

        if name == '': name = 'Profile'
        
        self.name = name
        
        return self._SaveProfile()


    def LoadProfile(self, id):        
        name = self.saves[id][0]
        items = self.saves[id][1]

        return name, items
    
           
    def DeleteProfile(self, id, msg = 'Profile not found'):
        try:
            self.saves.pop(id)
            self._SaveProgress()
               
        except:
            print(msg)

    def DelAllProfiles(self):
        self.saves.clear()
        self._SaveProgress()


class LayoutProfile(NewProfile):
    #Retorna uma string que com os perfis salvos

    def __init__(self, file_csv = 'file.csv', items = dict()):
        NewProfile.__init__(self, file_csv, items)


    def ListProfiles(self, msg = 'No profiles'):
        self.__init__(self.file, self.items)

        text = ''

        for c, i in enumerate(self.saves): 
            text += f'{c+1} - {self.saves[c][0]}\n'

        if text == '': return msg

        else: return text


    def ListProfilesCompletely(self, msg = 'No profiles'):
        self.__init__(self.file, self.items)

        text = ''

        for c, i in enumerate(self.saves): 
            text += f'{c+1} - {self.saves[c][0]} id: {c}\n{self.saves[c][1]} \n'

        if text == '': return msg

        else: return text


class ModifyProfile(LayoutProfile):
    '''Edita nomes e items de um perfil específico'''

    def __init__(self, file_csv = 'file.csv', items = dict()):
        LayoutProfile.__init__(self, file_csv, items)

      
    def EditName(self, id, name, msg = 'Profile not found'):
        try:
            self.saves[id][0] = name
            self._SaveProgress()
        
        except:
            print(msg)

    def UpdateItems(self, id, items, msg = 'Profile not found'):
        try:
            self.saves[id][1] = eval(self.saves[id][1])
            self.saves[id][1] = items
            self._SaveProgress()
        
        except:
            print(msg)
    
