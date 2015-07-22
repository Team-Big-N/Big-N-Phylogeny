import os
from flask import Flask, jsonify, request
import tempfile
import uuid
import hashlib
from functools import partial
from os.path import join as j
import shutil

#app = Flask(os.getenv('APP_NAME', 'big-n-phylogeny'))
app = Flask(__name__)

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)

UPLOAD_BLOCK_SIZE = 4194304

import viz
import api

def init():
	pass
	
#Tree Visualizer
@app.route('/viz/<path:segment>')
def visualize(segment=None):
	pass
	
@app.route('/viz/newick/<path:segment>')
def newick(segment=None):
	pass
	
#Sample api
@app.route('/api/<float:version>/samples/', methods=('POST',))
def add(version):
	tempdir = tempfile.mkdtemp()
	files = dict()
	
	metadata = dict()
	metadata['id'] = new_id = uuid.uuid4()
	#read in files
	h = hashlib.md5()
	for f in request.files.getlist('file'):
		with open(j(tempdir, f.filename), 'wb') as savefile:
			bytes = f.stream.read(UPLOAD_BLOCK_SIZE)
			h.update(bytes)
			savefile.write(bytes)
		files[f.filename] = h.hexdigest()
	
	#make celery job
	paths = [j(tempdir, fname) for fname in files.keys()]
	cleanup = partial(shutil.rmtree, tempdir)
	api.add(version=version, paths=paths, metadata=metadata, cleanup=cleanup)
	#return id
	return jsonify({'id':new_id, 'files_received':files})
	
	
# @app.route('/api/samples/', methods=('GET',))
# def getall():
# 	pass

@app.route('/api/<float:version>/samples/', methods=('GET',))
def get(version, id=None):
	pass
	
@app.route('/api/<float:version>/samples/<id>', methods=('PUT',))
def edit(version, id):
	pass
	
@app.route('/api/<float:version>/samples/<id>', methods=('DELETE',))
def delete(version, id):
	pass

	
