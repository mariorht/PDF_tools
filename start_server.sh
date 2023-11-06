#!/bin/bash

# Inicia el servidor FastAPI
uvicorn src.main:app --reload --host 0.0.0.0 --port 8080
