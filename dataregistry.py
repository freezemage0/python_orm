import tools

@tools.Singleton
class DataRegistry:
	def __init__(self):
		self.__registry = {}
	
	def registerEntity(self, entity):
		try:
			entityName = entity.getName()
		except NotImplementedError:
			raise NotImplementedError('Entity does not implement \'getName()\' method')
		
		if entityName in self.__registry:
			raise AttributeError('Entity "{}" already registered'.format(entityName))
		self.__registry[entityName] = entity

	def unRegisterEntity(self, entityName):
		if entityName in self.__registry:
			self.__registry[entityName] = None
	
	def getEntityInstance(self, entityName):
		entity = self.getEntity(entityName)
		instance = entity.initialize()
		return instance

	def getEntity(self, entityName):
		if entityName not in self.__registry:
			raise AttributeError('Entity "{}" not registered'.format(entityName))
		return self.__registry[entityName]

