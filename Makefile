# Runs the benchmark in a container
benchmark:
	docker-compose up --build benchmark
	docker-compose down

# Removes the virtualenv. Required after changes in requirements.txt
clean:
	rm -rf venv
	docker-compose rm --force --stop -v

# Runs the benchmark in the local virtualenv. Useful for development and debugging.
benchmark-local:
	python3 -m venv venv
	source venv/bin/activate && \
		pip install --upgrade pip && \
		pip install -r requirements.txt && \
		python src/benchmark.py

# Runs the benchmark and the lint whenever a key is presed. Useful for development and debugging.
watch_benchmark_local:
	scripts/watch_lint_test.sh

# Lints the code
lint:
	docker-compose up --build lint
	docker-compose down
