FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir cryptography
COPY simulation_main.py public_key.pem policy.json policy.json.sig ./
USER 1000
CMD ["python", "simulation_main.py"]
