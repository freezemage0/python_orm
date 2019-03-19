def Singleton(classInstance):
	class Wrapper:
		__classInstance = classInstance
		__instance = None
		def __init__():
			raise NotImplementedError('Cannot instantiate, use getInstance() instead')

		def getInstance():
			if Wrapper.__instance == None:
				Wrapper.__instance = Wrapper.__classInstance()
			return Wrapper.__instance
	return Wrapper

