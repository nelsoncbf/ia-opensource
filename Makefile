run:
	docker compose up ollama -d
	docker exec -it rag-opensource-ollama-1 ollama pull llama3
