#variables
COMPOSE_FILE = docker-compose.yml

install-packages:
	pip install -r requirements.txt

setup-db:
	docker-compose -f $(COMPOSE_FILE) up -d

stop-db:
	docker-compose -f $(COMPOSE_FILE) down

# to check postgres logs
logs-db:
	docker-compose -f $(COMPOSE_FILE) logs -f postgres

# Application start
start:
	cd backend && uvicorn main:app --port 8080 --reload