import logging
import azure.functions as func
import openai

secret_key = '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'


# {"prompt":"JeffBezos as a terrorist","n":1,"size":"1024x1024"}
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    openai.api_key = secret_key
    req_body = req.get_json()
    logging.info(type(req_body))
    output = openai.Image.create(
        prompt = req_body['prompt'],
        n = req_body['n'],
        size = req_body['size']
    )
    output_text = output['data'][0]['url']
    return func.HttpResponse(output_text,status_code=200)