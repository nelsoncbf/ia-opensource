#!/bin/bash
set -e

echo "🚀 Iniciando Ollama com modelo $MODEL_NAME..."

# Inicia o servidor Ollama em segundo plano
ollama serve &

# Aguarda o servidor subir
sleep 5

# Verifica se o modelo já está instalado, senão baixa
if ! ollama list | grep -q "$MODEL_NAME"; then
  echo "📦 Baixando modelo $MODEL_NAME..."
  ollama pull "$MODEL_NAME"
else
  echo "✅ Modelo $MODEL_NAME já está disponível."
fi

# Mantém o processo ativo
wait