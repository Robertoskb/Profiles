import csv
    
class File:
    #faz tratamento do arquivo csv onde ficará salvo os perfis

    def __init__(self, file_csv = 'file.csv'):
        self._CreateFile(file_csv)

        self.saves = self._ReadFile(file_csv)
        self.file = file_csv
        

    def _CreateFile(self, filename):       
        try:
            a = open(filename, 'r')
            
        except FileNotFoundError:
            a = open(filename, 'wt+')

        finally:
            a.close()


    def _ReadFile(self, filename):
        a = open(filename,'r')
        b = csv.reader(a)

        saves = list()
    
        for line in b: saves.append(line)

        a.close()

        return saves


    def _SaveProfile(self, name, items):
        self.list = [name, items]

        a = open(self.file, 'a', newline='')
        b = csv.writer(a)

        b.writerow(self.list)

        a.close()

        self.__init__(self.file)


    def _SaveProgress(self):
        a = open(self.file, 'w', newline='')
        b = csv.writer(a)

        for i in self.saves: b.writerow(i)

        a.close()


class NewProfile(File):
    #cria, carrega e deleta perfis salvos

    def __init__(self, file_csv = 'file.csv'):
        File.__init__(self, file_csv)
    

    def CreateProfile(self, name: str, items: dict):
        name = name.strip()

        if name == '': name = 'Profile'
        
        self._SaveProfile(name, items)


    def LoadProfile(self, id):        
        name = self.saves[id][0]
        items = self.saves[id][1]

        return name, items
    
           
    def DeleteProfile(self, id: int, msg = 'Profile not found'):
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

    def __init__(self, file_csv = 'file.csv'):
        NewProfile.__init__(self, file_csv)


    def ListProfiles(self, msg = 'No profiles'):
        self.__init__(self.file)

        text = ''

        for c, i in enumerate(self.saves): 
            text += f'{c+1} - {self.saves[c][0]}\n'

        if text == '': return msg

        else: return text


    def ListProfilesCompletely(self, msg = 'No profiles'):
        self.__init__(self.file)

        text = ''

        for c, i in enumerate(self.saves): 
            text += f'{c+1} - {self.saves[c][0]} id: {c}\n{self.saves[c][1]}\n'

        if text == '': return msg

        else: return text


class ModifyProfile(LayoutProfile):
    #Edita nomes e items de um perfil específico

    def __init__(self, file_csv = 'file.csv'):
        LayoutProfile.__init__(self, file_csv)

      
    def EditName(self, id: int, name: str, msg = 'Profile not found'):
        try:
            self.saves[id][0] = name

            self._SaveProgress()
        
        except:
            print(msg)
            

    def UpdateItems(self, id: int, items: dict, msg = 'Profile not found'):
        try:
            self.saves[id][1] = eval(self.saves[id][1])
            self.saves[id][1] = items

            self._SaveProgress()
        
        except:
            print(msg)