CryptoSafe Manager

Secure password vault architecture (8-sprint roadmap).

Architecture (MVC)

- core → business logic / crypto / state
- database → schema & persistence
- gui → UI layer
- tests → unit + integration

Setup

python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  
pytest

Sprint Roadmap

1. Foundation (current)
2. Real KDF + key storage
3. AES-256-GCM
4. Clipboard manager
5. Audit signing
6. Import/export
7. Auto-lock + inactivity
8. Packaging + release
