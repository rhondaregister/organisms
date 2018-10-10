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
	def checkIfMultiCellular(self):
		if self.domain == 'Eukarya':
			return('{} is a multicellular organism.'.format(self))
		else:
			return('{} is not a multicellular organism.'.format(self))
	def checkIfUnicellular(self):
		if self.domain == 'Bacteria':
			return('{} is a unicellular organism.'.format(self))
		elif self.domain == 'Archaea':
			return('{} is a unicellular organism.'.format(self))
		elif self.domain == 'Eukarya':
			return('{} is not a unicellular organism.'.format(self))
		else:
			return('{} is not a unicellular organism.'.format(self))


###############################
### Unicellular Organisms ###
###############################
class Bacteria(Organism):
	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, **kwargs)
		self.domain = 'Bacteria'

class Archaea(Organism):
	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, **kwargs)
		self.domain = 'Archaea'


################################
### Multi-Cellular Organisms ###
################################
class MultiCellularOrganism(Organism):
	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, **kwargs)
		self.domain = 'Eukarya'

### Animals ###
class Animal(MultiCellularOrganism):
	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, **kwargs)
		self.kingdom = 'Animalia'

### Plants ###
class Plant(MultiCellularOrganism):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.kingdom='Plantae'

### Fungi ###
class Fungus(MultiCellularOrganism):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.kingdom='Fungi'


#################
### Functions ###
#################
def sortOrganismsByCells(organism, *args):
	all_organisms_list = []
	unicellular_organisms = []
	multicellular_organisms = []
	all_organisms_list.append(organism)
	for arg in args:
		all_organisms_list.append(arg)
	for o in all_organisms_list:
		if o.domain == 'Bacteria':
			unicellular_organisms.append(o)
		elif o.domain == 'Archaea':
			unicellular_organisms.append(o)
		elif o.domain == 'Eukarya':
			multicellular_organisms.append(o)
	return unicellular_organisms, multicellular_organisms



fox = Animal('Chordata', 'Mammalia', 'Carnivora', 'Canidae', 'Vulpes', 'Vulpes', 'Red Fox')
print(fox)
print(fox.checkIfUnicellular())
print(fox.checkIfMultiCellular())

e_coli = Bacteria('Bacteria', 'Proteobacteria', 'Gammaproteobacteria', 'Enterobacteriales', 'Enterobacteriaceae', 'Escherichia', 'Coli', 'E. coli')
print(e_coli)
print(e_coli.checkIfUnicellular())
print(e_coli.checkIfMultiCellular())


c_symbiosum = Archaea('"Proteoarchaeota"', 'Thaumarchaeota', 'incertae sedis', 'Cenarchaeales', 'Cenarchaeaceae', 'Cenarchaeum', 'Symbiosum', 'C. symbiosum')
print(c_symbiosum)
print(c_symbiosum.checkIfUnicellular())
print(c_symbiosum.checkIfMultiCellular())


print(sortOrganismsByCells(fox, e_coli, c_symbiosum))