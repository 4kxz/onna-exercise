.PHONY: build test run

build:
	docker build -t onna-exercise .

test: build
	docker run --name onna --rm onna-exercise /usr/local/bin/python -m pytest /app/tests

run:
	docker-compose up
