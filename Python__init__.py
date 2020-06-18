

# Parent Class
class Organism:
    def __init__(self, name, species, legs, arms, dna, origin, carbon_based):
        self.name = name
        self.species = species
        self.legs = legs
        self.arms = legs
        self.dna = dna
        self.origin = origin
        self.carbon_based = carbon_based


O1 = Organism('McGuyver', 'Homosapien', 2, 2,'23 Chromosomal pairs', 'Earth', 'Yes')

print(O1.name)
print(O1.species)
print(O1.legs)
print(O1.arms)
print(O1.dna)
print(O1.origin)
print(O1.carbon_based)
    
