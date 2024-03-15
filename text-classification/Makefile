IMAGE_TAG = visable-service:latest
EXPOSED_PORT = 8000

docker-build-serve:
	docker build -f Dockerfile -t $(IMAGE_TAG) .

docker-run-serve:
	docker run -p $(EXPOSED_PORT):$(EXPOSED_PORT) $(IMAGE_TAG)