FROM python:3.12-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# ensure deep3_mod doesn't raise on import (we check version in module)
CMD ["python", "gtrans3.py"]

