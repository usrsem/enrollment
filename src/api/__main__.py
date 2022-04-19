from aiohttp.web import Application, run_app
from api.controller import routes


def main() -> None:
    app = Application()
    app.add_routes(routes)
    run_app(app)


if __name__ == "__main__":
    main()

