#!/usr/bin/env python3

import connexion

#from swagger_server import encoder


app = connexion.App(__name__, specification_dir='./swagger/')
#    app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'Yc'})
#app.run(port=7000)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=7000)
