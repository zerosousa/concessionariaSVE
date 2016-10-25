guard-%:
	@ if [ "${${*}}" = "" ]; then \
		echo "Variable '$*' not set"; \
		exit 1; \
	fi

run:
	docker-compose up
exec: guard-args
	docker-compose exec -it $(args)
