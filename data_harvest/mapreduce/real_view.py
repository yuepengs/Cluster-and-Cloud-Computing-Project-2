import couchdb
import couchdb.design
import time

def view_create(db, design_name, view_name):
	map = 'function(doc) { emit([doc.label, doc.sentimental],1); }'
	reduce = 'function(keys, values) { return sum(values); }'
	view = couchdb.design.ViewDefinition(design_name, view_name, map_fun=map, reduce_fun=reduce)
	view.sync(db)
	view_set = f"{design_name}/{view_name}"
	return view_set


def view_reduce(db, view_set_name):
	out_keys = []
	for out in db.view(view_set_name, group=True):
		if out.key[0] not in out_keys:
			out_keys.append(out.key[0])

	out_dict = {}
	for key_i in out_keys:
		in_dict = {}
		for out in db.view(view_set_name, group=True):
			if out.key[0] == key_i:
				in_dict[out.key[1]] = out.value

		out_dict[key_i] = in_dict
	return out_dict


if __name__ == "__main__":
	while True:
		server = "http://admin:password@172.26.130.194:5984/"
		couch = couchdb.Server(server)
		db = couch['realtime_sent_new']
		view_set = view_create(db, "test", "senti_count")

		dict = view_reduce(db, view_set)
		# try:
		# 	new_db = couch['realtime_mapreduce']
		# 	couch.delete('realtime_mapreduce')
		#
		# except:
		# 	new_db = couch.create('realtime_mapreduce')

		if 'realtime_mapreduce' in couch:
			couch.delete('realtime_mapreduce')
		new_db = couch.create('realtime_mapreduce')

		for key, value in dict.items():
			new_db[key] = value


	# new_db.save(dict)

		print(dict)
		time.sleep(60)



