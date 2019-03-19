import tools, db
from dataregistry import DataRegistry

class Entity:
	def __init__(self, name):
		self.dbInstance = db.DB.getInstance()
		self.entityInstance = None
		self.name = name

	def getName(self):
		if self.name == None:
			raise AttributeError('Entity does not have "name" property')
		return self.name
	
	def initialize(self):
		if self.entityInstance == None:
			dbInstance = self.dbInstance
			try:
				if dbInstance.exist(self.getName()) == False:
					dbInstance.start().parseMap(self.getMap()).execute()
				else:
					dbInstance.start().getTable(self.getName()).execute()
				self.entityInstance = dbInstance.getResult()
			except NotImplementedError as NIError:
				raise Exception(NIError)
		return self.entityInstance
			
	def getMap(self):
		map = {}
		return map

class User(Entity):
	def getMap(self):
		map = {
			'id': {
				'datatype': 'integer',
				'autoincrement': 'true',
				'primary': 'true'
			},
			'test_column': {
				'datatype': 'text',
				'null': 'true',
				'default': 'null'
			}
		}
		return map
	
registry = DataRegistry.getInstance()
registry.registerEntity(User('test_user'))
userTableObject = registry.getEntity('test_user')
print(userTableObject.getName())
