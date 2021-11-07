DOCKER_TAG = python-json-alternatives-benchmark

# Runs the benchmark in a container
benchmark-docker: docker-build
	docker run --rm -t $(DOCKER_TAG)

# Removes the virtualenv. Required after changes in requirements.txt
clean:
	rm -rf venv

# Builds the benchmark container
docker-build:
	docker build -t $(DOCKER_TAG) -f docker/Dockerfile .

# Runs the benchmark in the local virtualenv. Useful for development and debugging.
benchmark-local:
	python3 -m venv venv
	source venv/bin/activate && pip install --upgrade pip
	source venv/bin/activate && pip install -r requirements.txt
	source venv/bin/activate && python src/benchmark.py

# Runs the benchmark and the lint whenever a key is presed. Useful for development and debugging.
watch_benchmark_local:
	scripts/watch_lint_test.sh

# Lints the code using various tools.
lint: docker-build
	docker run --rm -t $(DOCKER_TAG) "/scripts/lint.sh"
