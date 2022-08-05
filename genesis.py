from flask import Flask
from flask import jsonify
from flask_cors import CORS

application = Flask(__name__)
CORS(application,supports_credentials=True)


def template(id):
    tpl = {
        "attributes":[
            {
                "trait_type":"Level",
                "value":"bronze"
            },
        ],
        "description":"Elon Musk Says Das Baby would be a hit!",
        "external_url":"http://dasbabyinu.com",
        "id":1,
        "image":"http://dasbabyinu.com/genesis/",
        "name":"DasBabyGenesis - #"
    }

    if int(id) > 788:
        tpl["attributes"][0]["value"] = "sliver"

    tpl["id"] = int(id)
    tpl["image"] = tpl["image"] + id + ".jpg"

    tpl["name"] = tpl["name"] + id
    return tpl


@application.route("/nft/<id>",methods=["GET"])
def nft(id):
    tpl = template(id)
    return jsonify(tpl)

@application.route("/nft/",methods=["GET"])
def nfts():
    tpls = []
    for id in range(1,1001):
        tpl = template(str(id))
        tpls.append(tpl)
    return jsonify(tpls)

if __name__ == "__main__":
    application.run(host='0.0.0.0',port=8888,debug=True)