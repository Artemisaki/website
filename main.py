# BEGIN CODE HERE
import json
from difflib import SequenceMatcher
import math
import re
from collections import Counter


from operator import itemgetter
from urllib import request
from flask import Flask, jsonify, request

from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import TEXT


schema = {
    "ID": str,
    "name":str,
    "productionYear":int,
    "price":float,
    "color":str,
    "size":str
}
# END CODE HERE

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/pspi"
CORS(app)
mongo = PyMongo(app)
mongo.db.products.create_index([("name", TEXT)])


# TESTING BEGINS!
#  this is the URL: http://127.0.0.1:5000/
# flask --app main  --debug run
# API call 1
# # get request
@app.route("/")
def api_call_1():
    # return jsonify({"res": "This is our first API Call"})
    return "This is our first API call"
# TESTING ENDS!


@app.route("/search", methods=["GET"])
def search():
    # BEGIN CODE HERE
    name = request.args.get("name")
    list1 = []
    for x in mongo.db.products.find({"$text": {"$search": f"\"{name}\""}}):
        list1.append(x)
    newlist = sorted(list1,key=itemgetter('price'),reverse=True)
    final_list=[]
    for x in newlist:
        final_list.append(str(x))

    return final_list
    # END CODE HERE


@app.route("/add-product", methods=["POST"])
def add_product():


    # BEGIN CODE HERE
    new_product = request.json
    print(new_product)
    if new_product["color"] == "red":
        new_product["color"] = 1
    elif new_product["color"] == "yellow":
        new_product["color"] = 2
    else:
        new_product["color"] = 3

    if new_product["size"] == "small":
        new_product["size"] = 1
    elif new_product["size"] == "medium":
        new_product["size"] = 2
    elif new_product["size"] == "large":
        new_product["size"] = 3
    else:
        new_product["size"] = 4

    exists = mongo.db.products.find_one({"name": new_product["name"]})
    if exists is None:
        mongo.db.products.insert_one(new_product)
        return "not exists, Addition made"
    else:
        mongo.db.products.update_one({"name": new_product["name"]}, {"$set": {"ID": new_product["ID"], "productionYear": new_product["productionYear"], "price": new_product["price"], "size": new_product["size"], "color": new_product["color"]}})
        return "exists, Updated"

    # END CODE HERE


@app.route("/content-based-filtering", methods=["POST"])
def content_based_filtering():
    # BEGIN CODE HERE
    WORD = re.compile(r"\w+")
    vector1 = request.args.get("name")
    list1 = []

    for x in mongo.db.products.find():

        #words = WORD.findall(str(x['name']))#παιρνουμε το value του name
        #print("word from dict: ", str(x['name']))
        sim1 = -1
        words = WORD.findall(str(x['name']))
        for y in words:

            sim2 = SequenceMatcher(None, vector1, y).ratio()
            if sim2 > sim1:
                sim1 = sim2

        if sim1 >= 0.7:
            list1.append(x)
        print("..................................................")
        print("Similarity between ", vector1, "and", str(x['name']), "two strings is: " + str(sim1))

    print(*list1, sep="\n")
        #sim = SequenceMatcher(None, vector1, str(x['name'])).ratio()

        #print("Similarity between ",vector1, "and",str(x['name']),"two strings is: " + str(sim))
        #print("words: ", words)
        #vector2 = Counter(words)#και το κανουμε text_to_vector2
        #print("value2 to value: ", vector2,"/n")

        #words = WORD.findall(str(vector1))#παιρνουμε το name
        #vector1 = Counter(words)#και το κανουμε text_to_vector1
        #print("words: ", words)
        #print("value 1: ", vector1)
        #print("vector 1: ", vector1)
        #intersection = set(vector1.keys()) & set(vector2.keys())
        #numerator = sum([vector1[x] * vector2[x] for x in intersection])

        #sum1 = sum([vector1[x] ** 2 for x in list(vector1.keys())])
        #sum2 = sum([vector2[x] ** 2 for x in list(vector2.keys())])
        #denominator = math.sqrt(sum1) * math.sqrt(sum2)

        #if not denominator:
           # cosine = 0.0
        #else:
        #cosine = float(numerator) / denominator

        #print(cosine)

    return ""
    # END CODE HERE


@app.route("/crawler", methods=["GET"])
def crawler():
    # BEGIN CODE HERE
    return ""
    # END CODE HERE