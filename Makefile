##Commands
.PHONY: run_api
run_api:
	. venv/bin/activate \
	&& python3 manage.py run

.PHONY: run_ui
run_ui:
	cd ui \
	&& npm start
