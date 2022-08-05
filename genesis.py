from flask import Flask
from flask import jsonify
application = Flask(__name__)


@application.route("/nft/<id>",methods=["GET"])
def nft(id):
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
        "image":"http://dasbabyinu.com/nft/image/",
        "name":"DasBabyGenesis - #"
    }

    if int(id) > 788:
        tpl["attributes"][0]["value"] = "sliver"

    tpl["id"] = int(id)
    tpl["image"] = tpl["image"] + id + ".jpg"

    tpl["name"] = tpl["name"] + id
    return jsonify(tpl)

if __name__ == "__main__":
    application.run(host='0.0.0.0',port=8888,debug=True)
