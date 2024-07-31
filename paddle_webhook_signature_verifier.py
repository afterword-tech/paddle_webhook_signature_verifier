import hmac
import hashlib
import time

class WebhookHandler:
    def __init__(self, secret_key: bytes):
        self.secret_key = secret_key

    def verify_hmac_signature(self, signed_payload: bytes, received_signature: str) -> bool:
        hmac_hash = hmac.new(self.secret_key, signed_payload, hashlib.sha256).hexdigest()
        return hmac_hash == received_signature

    def validate_timestamp(self, timestamp: str) -> bool:
        try:
            event_time = int(timestamp)
            current_time = int(time.time())
            return abs(current_time - event_time) <= 5
        except ValueError:
            return False

    def verify_paddle_signature(self, paddle_signature: str, body: bytes):
        if not paddle_signature:
            raise ValueError("Paddle-Signature header missing")
        
        signature_parts = dict(part.split('=') for part in paddle_signature.split(';'))
        timestamp = signature_parts.get('ts')
        hash_signature = signature_parts.get('h1')

        if not self.validate_timestamp(timestamp):
            raise ValueError("Invalid timestamp")

        signed_payload = f"{timestamp}:{body.decode('utf-8')}".encode('utf-8')
        if not self.verify_hmac_signature(signed_payload, hash_signature):
            raise ValueError("Invalid signature")
        
        return True