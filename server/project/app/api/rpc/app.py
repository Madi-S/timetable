import fastapi_jsonrpc as jsonrpc


app = jsonrpc.API()
api_v1 = jsonrpc.Entrypoint('/json')


@api_v1.method()
def echo(data: str) -> str:
    return data


app.bind_entrypoint(api_v1)
