# viikko3/login

- This is a `uv` project. Run project commands with `uv run ...` from `viikko3/login`.
- Start the Flask app with `uv run python src/index.py`. It listens on port `5001`.
- Run the Robot Framework browser tests with `uv run robot src/tests`. Keep the app running during tests.
- User registration validation (username/password length, confirmation, and duplicate username) is in `src/services/user_service.py` (`UserService.validate`). Login credential checks are in `UserService.check_credentials`.
- Flask routes and form handling are defined in `src/app.py`; `src/index.py` starts the app.
- Keep business logic in `src/services/user_service.py`, separate from the in-memory user storage in `src/repositories/user_repository.py`.
- The repository stores users in memory; `POST /tests/reset` clears that state for test setup.
- HTML pages are Jinja templates in `src/templates/`; Robot browser suites and shared browser setup are in `src/tests/`.
