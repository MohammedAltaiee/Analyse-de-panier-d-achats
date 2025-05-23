# Analyse-de-panier-d-achats
Mini-Système de e-commerce

source /home/nissinassime/Analyse-de-panier-d-achats/.venv/bin/activate

pour tester uvicorn main:app --reload

ouvrir les ports 80 et 443 sur GCP (Google Cloud Platform)
puis:
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

uvicorn <your_app_file>:<your_app_object> --host <your_ip_address> --port <your_port>

sudo uvicorn main:app --reload --host 0.0.0.0 --port 80

