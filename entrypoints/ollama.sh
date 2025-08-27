#!/bin/bash
set -e

MODEL_NAME="llama3"

# Verifica se o modelo já está instalado
if ! ollama list | grep -q "$MODEL_NAME"; then
  echo "🔄 Baixando modelo $MODEL_NAME..."
  ollama pull "$MODEL_NAME"
else
  echo "✅ Modelo $MODEL_NAME já está instalado."
fi

# Inicia o serviço principal (substitua pelo seu comando real)
exec "$@"

ollama serve