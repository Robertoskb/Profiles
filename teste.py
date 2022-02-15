import Profiles 

a = Profiles.ModifyProfile('exemplo01.csv')

a.CreateProfile('Roberto',{})
a.UpdateItems(0, {'cubos': ['Skewb', '3x3x3', 'Megaminx']})
