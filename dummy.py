from entity import *

class Dummy(Entity):
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
registry.registerEntity(Dummy('dummy_table'))

dummyObject = registry.getEntity('dummy_table')
print(dummyObject.getMap())
