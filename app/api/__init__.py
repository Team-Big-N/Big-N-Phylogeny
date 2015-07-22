import imp

def add(version, *args, **kwargs):
	return load(version).add.delay(*args, **kwargs)

def get(version, *args, **kwargs):
	return load(version).get.delay(*args, **kwargs)

def edit(version, *args, **kwargs):
	return load(version).edit.delay(*args, **kwargs)

def delete(version, *args, **kwargs):
	return load(version).delete.delay(*args, **kwargs)
	
	
def load(version):
	return imp.load_module(str(version))