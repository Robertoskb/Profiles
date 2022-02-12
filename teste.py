import Profiles 

a = Profiles.ModifyProfile('exemplo01.csv')

a.CreateProfile('Roberto')
a.UpdateItems(0,{'Cubos':['Skewb', '3x3x3', 'Megaminx']})

