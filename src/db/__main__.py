import os
from alembic.config import CommandLine, Config
from config.pg import DEFAULT_PG_URL


def main():
    alembic = CommandLine()
    options = alembic.parser.parse_args()
     
    config = Config(
        file_=options.config,
        ini_section=options.name,
        cmd_opts=options
    )

    alembic.parser.add_argument(
        "--pg-url", default=os.getenv("ANALYZER_PG_URL", DEFAULT_PG_URL),
        help="Database URL [env var: ANALYZER_PG_URL]"
    )

    exit(alembic.run_cmd(config, options))


if __name__ == "__main__":
    main()

