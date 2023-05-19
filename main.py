# BEGIN CODE HERE
import json
from difflib import SequenceMatcher
import math
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    "color":int,
    "size":int
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
    # if new_product["color"] == "red":
    #     new_product["color"] = 1
    # elif new_product["color"] == "yellow":
    #     new_product["color"] = 2
    # else:
    #     new_product["color"] = 3
    #
    # if new_product["size"] == "small":
    #     new_product["size"] = 1
    # elif new_product["size"] == "medium":
    #     new_product["size"] = 2
    # elif new_product["size"] == "large":
    #     new_product["size"] = 3
    # else:
    #     new_product["size"] = 4

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
    new_product = request.json
    thistuple = (new_product["productionYear"], new_product["price"], new_product["color"], new_product["size"])
   # print(thistuple)
    list1 = []
    thisdistance = math.sqrt(thistuple[0]*thistuple[0] + thistuple[1]*thistuple[1] + thistuple[2]*thistuple[2] + thistuple[3]*thistuple[3])

    for x in mongo.db.products.find():
        tuple2 = (x["productionYear"], x["price"], x["color"], x["size"])
        multi2 = sum(p*q for p, q in zip(thistuple, tuple2))
        distance2 = math.sqrt(tuple2[0]*tuple2[0] + tuple2[1]*tuple2[1] + tuple2[2]*tuple2[2] + tuple2[3]*tuple2[3])
        if multi2/(thisdistance*distance2) >= 0.7:
            list1.append(x["name"])

    return list1
    # END CODE HERE


@app.route("/crawler", methods=["GET"])
def crawler():
    # BEGIN CODE HERE

    semester = request.args.get("semester1")
    print(semester)
    try:
        url = "https://qa.auth.gr/el/x/studyguide/600000438/current"
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        #
        # if semester == "1":
        #     html = str((driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div[2]/table[1]/tbody")).text)
        # elif semester == "2":
        #     html = str((driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div[2]/table[2]/tbody")).text)
        # elif semester == "3":
        #     html = str(
        #         (driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div[2]/table[3]/tbody")).text)
        # elif semester == "4":
        #     html = str(
        #         (driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div[2]/table[4]/tbody")).text)
        # elif semester == "5":
        #     html = str(
        #         (driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div[2]/table[5]/tbody")).text)
        # elif semester == "6":
        #     html = str(
        #         (driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div[2]/table[6]/tbody")).text)
        # elif semester == "7":
        #     html = str(
        #         (driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div[2]/table[7]/tbody")).text)
        # elif semester == "8":
        #     html = str(
        #         (driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div[2]/table[8]/tbody")).text)
        str2 = "/html/body/div[2]/div[1]/div/div/div/div/div[2]/table["+semester+"]/tbody"
        print(str2)
        html = str((driver.find_element(By.XPATH, str2)).text)
        html1 = html.split()
        string1 = ""
        subjects = []
        for x in html1:
            if len(x) > 1 and not("-" in x) and x != "ΥΚΕ":
                if string1 == "":
                    string1 = x
                else:
                    string1 = string1 + " " + x
            else:
                if string1 != "":
                    subjects.append(string1)
                string1 = ""
        print(subjects)

    except Exception as e:
        print("bad request")

    return subjects
    # END CODE HERE
