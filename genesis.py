from flask import Flask, jsonify, request
from flask_cors import CORS
from web3 import Web3, HTTPProvider
import json
import requests

application = Flask(__name__)
CORS(application, supports_credentials=True)


Contract = '0x74155e8E00D19083033d3f58C0BA25eAE1856f84'
Rpc = 'https://bsc-dataseed1.binance.org:443'

BscUrl = "https://api.bscscan.com/api?apikey=X4G8XDAWSXKVGBSYVKFGX8FSEHS6Y57ZSZ&module=account&action=txlist&page=1&offset=10&sort=desc&address="


with open('abi.json', 'r') as contract_abi:
    ABI = json.load(contract_abi)

web3 = Web3(HTTPProvider(Rpc))
token_contract = web3.eth.contract(
    address=Web3.toChecksumAddress(Contract), abi=ABI)


def OwnerOf(id):
    try:
        return token_contract.functions.ownerOf(id).call()
    except:
        return "0"


def template(id):
    tpl = {
        "attributes": [
            {
                "trait_type": "Level",
                "value": "sliver"
            },
        ],
        "description": "Elon Musk Says Das Baby would be a hit!",
        "external_url": "http://dasbabyinu.com",
        "id": 1,
        "image": "http://dasbabyinu.com/genesis/",
        "name": " - #",
        "owner": "0"
    }

    if int(id) > 212:
        tpl["attributes"][0]["value"] = "bronze"

    tpl["id"] = int(id)
    tpl["image"] = tpl["image"] + id + ".jpg"

    tpl["name"] = tpl["attributes"][0]["value"] + tpl["name"] + id
    return tpl

@application.route("/trade/tx_list/<address>", methods=["GET"])
def tx_list(address):
    url = BscUrl + address
    ret = []
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        if data["result"]:
            for item in data["result"]:
                if item["hash"]:
                    print("data is:",item["hash"])
                    ret.append(item["hash"])
    return  jsonify(ret)

@application.route("/nft/<id>", methods=["GET"])
def nft(id):
    tpl = template(id)
    return jsonify(tpl)


@application.route("/nft/owner/<id>", methods=["GET"])
def owner(id):
    addr = OwnerOf(int(id))
    return jsonify(addr)


@application.route("/nft/", methods=["GET"])
def nfts():
    start = int(request.args.get("start"))
    page = int(request.args.get("page"))

    end = start+page
    if end > 1001:
        end = 1000
    if start > 1001:
        start = 1000
    tpls = []
    for id in range(start, end):
        tpl = template(str(id))
        tpls.append(tpl)
    return jsonify(tpls)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8888, debug=True)
