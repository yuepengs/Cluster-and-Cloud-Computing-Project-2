"""
COMP90024 Cluster and Cloud Computing Assignment 2
Team 22

Zizhao Li (1267416) zizhaol2@student.unimelb.edu.au (Suzhou, China)
Fu Zhu (1166186) fuzhu@student.unimelb.edu.au (Melbourne, Australia)
Chuting Wang (1074511) chutingw@student.unimelb.edu.au (Xi’an, China)
Xuezhu Wu (938808) xuezhuw@student.unimelb.edu.au (Hangzhou, China)
Yuepeng Sheng (1048382) yuepengs@student.unimelb.edu.au (Shanghai, China)
"""


import couchdb
import couchdb.design
import json
import os
import numpy as np
import pandas as pd


def view_create(db, design_name, view_name):
	map = 'function(doc) { emit([doc.location, doc.sentimental],1); }'
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
	server = "http://admin:password@172.26.130.194:5984/"
	couch = couchdb.Server(server)
	db = couch['historytime_sent_new']
	view_set = view_create(db, "test", "senti_count")
	dict = view_reduce(db, view_set)


	rent_median_excel = pd.read_excel(io = "Data/rent.xlsx", sheet_name = "All Properties")
	payment_csv = pd.read_csv("Data/payment.csv")


	# Merge Data
	with open("Data/map.json", "r", encoding="utf-8") as f:
		json_data = json.load(f)
		for i in range(len(json_data["features"])):
			try:
				del json_data["features"][i]["id"]
			except:
				pass

			location_name = json_data["features"][i]["properties"]["vic_lga__3"]
			rent_median = int(rent_median_excel[rent_median_excel["LGA_name_l"] == location_name.lower()]["Median"].values[0])

			low_income_card = int(payment_csv[payment_csv["lga_name"] == location_name.lower()][" low_income_card"].values[0])

			total = dict[location_name][-1] + dict[location_name][0] + dict[location_name][1]
			json_data["features"][i]["properties"]["total_tweets"] = total
			json_data["features"][i]["properties"]["senti_neg_count"] = dict[location_name][-1]
			json_data["features"][i]["properties"]["senti_neu_count"] = dict[location_name][0]
			json_data["features"][i]["properties"]["senti_pos_count"] = dict[location_name][1]
			json_data["features"][i]["properties"]["senti_neg_dens"] = round(dict[location_name][-1] / total, 3)
			json_data["features"][i]["properties"]["senti_neu_dens"] = round(dict[location_name][0] / total, 3)
			json_data["features"][i]["properties"]["senti_pos_dens"] = round(dict[location_name][1] / total, 3)
			json_data["features"][i]["properties"]["rent_median"] = rent_median
			json_data["features"][i]["properties"]["low_income_card"] = low_income_card


	with open("Data/map.json", "w", encoding="utf-8") as f:
		json.dump(json_data, f, ensure_ascii=False)
