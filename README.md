# Paddle webhook signature verifier for Python
A Python package for verifying Paddle webhook signatures. Official Paddle SDKs are only available for PHP and Node.js. This packagage helps server side verification of Paddle webhook signatures if you are using a Python based backend framework like Django, Flask, FastAPI, etc.

## Installation
```bash
pip install paddle-webhook-signature-verifier
```

## Usage
### FastAPI example
```Python
from fastapi import FastAPI, Request, Header, HTTPException
from paddle_webhook_signature_verifier import WebhookHandler

app = FastAPI()
handler = WebhookHandler(secret_key=b'your_secret_key')

@app.post("/webhook")
async def webhook(request: Request, paddle_signature: str = Header(None)):
    try:
        body_bytes = await request.body()
        handler.verify_paddle_signature(paddle_signature, body_bytes)
        return {"status": "ok"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
```
### Flask example
```Python
from flask import Flask, request, abort
from paddle_webhook_signature_verifier import WebhookHandler

app = Flask(__name__)
handler = WebhookHandler(secret_key=b'your_secret_key')

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        paddle_signature = request.headers.get("Paddle-Signature")
        body_bytes = request.get_data()
        handler.verify_paddle_signature(paddle_signature, body_bytes)
        return {"status": "ok"}, 200
    except ValueError as e:
        abort(400, description=str(e))
```
### Django example
```Python
from django.http import JsonResponse
from paddle_webhook_signature_verifier import WebhookHandler

handler = WebhookHandler(secret_key=b'your_secret_key')

def webhook(request):
    try:
        paddle_signature = request.headers.get("Paddle-Signature")
        body_bytes = request.body
        handler.verify_paddle_signature(paddle_signature, body_bytes)
        return JsonResponse({"status": "ok"})
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details

## Contact
For any questions or suggestions, feel free to open an issue or contact the maintainer at aneesh.arora.aa@gmail.com

