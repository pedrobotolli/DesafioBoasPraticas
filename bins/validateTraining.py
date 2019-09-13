import requests

def get_model_id():
    '''
    Gets the id of the model to be validated
    :return:
    a json containing the id of the model
    '''
    st_request = requests.get('http://dtt-boas-praticas.geekvault.org:5000/api/0.1/predictions/titanic/train')
    return st_request.json()["model_id"]
def validate_id(model_id):
    '''
    Recieves an id to be verified at the server
    :param model_id:
    the id that will be validated
    :return:
    Return true if the id is found and false if isn't, as a json
    '''
    st_post = requests.post('http://dtt-boas-praticas.geekvault.org:5000/api/0.1/predictions/titanic/predicted', json={"model": f"{model_id}"})
    return st_post.json()["success"]

def main():
    '''
    Main procedure
    :return:
    '''
    result_request = "False"
    while result_request == "False":
        id_request = get_model_id()
        result_request = validate_id(id_request)
    return id_request

if __name__=='__main__':
   print(main())