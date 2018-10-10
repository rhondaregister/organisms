'''
An exercise in class inheritance using biological taxonomy.
'''

class Organism():
	def __init__(self, domain, kingdom, phylum, klass, order, family, genus, species, name):
		self.alive = True
		self.domain = domain
		self.kingdom = kingdom
		self.phylum = phylum
		self.klass = klass
		self.order = order
		self.family = family
		self.genus = genus
		self.species = species
		self.common_name = name
	def __str__(self):
		return self.common_name + ' ' + '({} {})'.format(self.genus, self.species.lower())
	def __repr__(self):
		return("<Object: {} ({} {})>").format(self.common_name, self.genus, self.species.lower())
	def determineCellular_UniOrMulti(self):
		if self.domain == 'Bacteria' or self.domain == 'Archaea':
			return('{} is a unicellular organism.'.format(self))
		elif self.domain == 'Eukarya':
			return('{} is a multicellular organism.'.format(self))
		else:
			return('{} is not a unicellular or a multicellular organism. You\'ve discovered an alien o_O'.format(self))


#######################
### Alien Organisms ###
#######################
class Alien(Organism):
	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, **kwargs)
		self.domain = 'Alien'

#############################
### Unicellular Organisms ###
#############################
class Bacteria(Organism):
	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, **kwargs)
		self.domain = 'Bacteria'

class Archaea(Organism):
	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, **kwargs)
		self.domain = 'Archaea'


################################
### Multicellular Organisms ###
################################
class MulticellularOrganism(Organism):
	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, **kwargs)
		self.domain = 'Eukarya'

### Animals ###
class Animal(MulticellularOrganism):
	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, **kwargs)
		self.kingdom = 'Animalia'

### Plants ###
class Plant(MulticellularOrganism):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.kingdom='Plantae'

### Fungi ###
class Fungus(MulticellularOrganism):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.kingdom='Fungi'


#################
### Functions ###
#################
def sortOrganismsByCells(*args):
	unicellular_organisms = []
	multicellular_organisms = []
	aliens = []
	for o in args:
		if o.domain == 'Bacteria' or o.domain == 'Archaea':
			unicellular_organisms.append(o)
		elif o.domain == 'Eukarya':
			multicellular_organisms.append(o)
		else:
			aliens.append(o)
	return unicellular_organisms, multicellular_organisms, aliens 



fox = Animal('Chordata', 'Mammalia', 'Carnivora', 'Canidae', 'Vulpes', 'Vulpes', 'Red Fox')
print(fox)
print(fox.determineCellular_UniOrMulti())

e_coli = Bacteria('Bacteria', 'Proteobacteria', 'Gammaproteobacteria', 'Enterobacteriales', 'Enterobacteriaceae', 'Escherichia', 'Coli', 'E. coli')
print(e_coli)
print(e_coli.determineCellular_UniOrMulti())

c_symbiosum = Archaea('"Proteoarchaeota"', 'Thaumarchaeota', 'incertae sedis', 'Cenarchaeales', 'Cenarchaeaceae', 'Cenarchaeum', 'Symbiosum', 'C. symbiosum')
print(c_symbiosum)
print(c_symbiosum.determineCellular_UniOrMulti())

ET = Alien('Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'ET')
print(ET)
print(ET.determineCellular_UniOrMulti())

print(sortOrganismsByCells(fox, e_coli, c_symbiosum, ET))