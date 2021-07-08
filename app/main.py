from fastapi import FastAPI, Request, HTTPException, status
from .redis import limiter

app = FastAPI()


@app.get("/")
def test(request: Request):
    clientIp = request.client.host
    res = limiter(clientIp, 5)
    if res["call"]:
        return {
            "message": "Hello world",
            "ttl": res["ttl"]
        }
    else:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail={
            "message": "call limit reached",
            "ttl": res["ttl"]
        })
