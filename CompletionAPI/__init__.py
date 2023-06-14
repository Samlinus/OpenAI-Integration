import logging
import azure.functions as func
import openai

secret_key = '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'


# {"model":"text-davinci-003","prompt":"Give me jingles for tea","max_tokens":200,"temperature":0}
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    openai.api_key = secret_key
    req_body = req.get_json()
    logging.info(type(req_body))
    output = openai.Completion.create(
        model = req_body['model'],
        prompt = req_body['prompt'],
        max_tokens = req_body['max_tokens'],
        temperature = req_body['temperature']
    )
    output_text = output['choices'][0]['text']
    return func.HttpResponse(output_text,status_code=200)

