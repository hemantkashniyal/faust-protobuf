VENV_NAME := venv-faust-protobuf

.PHONY: proto

install:
	conda env update -n $(VENV_NAME) -f environment.yaml

proto:
	python -m grpc_tools.protoc -I . --python_out=app proto/greetings.proto

run: proto
	python -m app.app worker
