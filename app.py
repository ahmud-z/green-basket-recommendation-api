from flask import Flask, request, jsonify
import pickle
import json

app = Flask(__name__)

products_file = open("products.pkl", "rb")
similarity_file = open("similarity.pkl", "rb")

products_data = pickle.load(products_file)
similarity_data = pickle.load(similarity_file)


@app.route("/")
def adasdasd():
    product_index = products_data[
        products_data["product_name"] == request.args.get("product_name")
    ].index[0]

    recommended_products = sorted(
        list(enumerate(similarity_data[product_index])),
        reverse=True,
        key=lambda x: x[1],
    )[1:5]

    recommended_product_ids = []

    for index in recommended_products:
        recommended_product_ids.append(int(products_data.iloc[index[0]].product_id))

    print(recommended_product_ids)

    return jsonify({"products": recommended_product_ids})
