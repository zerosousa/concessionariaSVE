guard-%:
	@ if [ "${${*}}" = "" ]; then \
		echo "Variable '$*' not set"; \
		exit 1; \
	fi

run:
	docker-compose up

exec: guard-args
	docker-compose exec web $(args)

stop:
	docker-compose kill

kill:
	docker-compose rm -fv
