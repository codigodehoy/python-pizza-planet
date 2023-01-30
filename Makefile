##Commands
.PHONY: run_api
run_api:
	. venv/bin/activate \
	&& python3 manage.py run

.PHONY: run_ui
run_ui:
	cd ui \
	&& npm start

.PHONY: run_test_api
run_test_api:
	. venv/bin/activate \
	&& python3 manage.py test

.PHONY: generate_report
generate_report:
	. venv/bin/activate \
	&& coverage run manage.py test \
	&& coverage xml \
