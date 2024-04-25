from flask import Flask, request
from flask_cors import CORS

import config, prompts, generator

app = Flask(__name__)
CORS(app)


@app.route("/<tmpl_name>/generate", methods=["POST"])
def generate(tmpl_name):
    raw_data = request.get_data()
    requirement = raw_data.decode("utf-8")
    return generator.generate(tmpl_name, requirement), 200


@app.route("/template", methods=["GET"])
def get_templates():
    reload = request.args.get("reload", "false")
    if reload == "true":
        prompts.reload()
    return prompts.get_tmpl_names(), 200


@app.route("/template/<tmpl_name>", methods=["GET"])
def get_template(tmpl_name):
    return prompts.get_template(tmpl_name)


@app.route("/template/<tmpl_name>", methods=["PUT"])
def update_template(tmpl_name):
    raw_data = request.get_data()
    content = raw_data.decode("utf-8")
    prompts.save_template(
        tmpl_name,
        content,
    )
    return "", 204


@app.route("/config", methods=["GET"])
def get_config():
    return config.get_config(), 200


@app.route("/config", methods=["PUT"])
def update_config():
    conf = request.get_json()
    config.update_config(conf)
    return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
