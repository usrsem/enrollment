from aiohttp.web import RouteTableDef, Request, Response
from loguru import logger as log


routes: RouteTableDef = RouteTableDef()


@routes.post("/imports")
async def post_imports(request: Request) -> Response:
    log.debug("post_imports")
    return Response(text="post_imports")


@routes.get(r"/imports/{import_id:\d+}/citizens")
async def get_citizens(request: Request) -> Response:
    log.debug("get_citizens")
    return Response(text="get_citizens")


@routes.patch(r"/imports/{import_id:\d+}/citizens/{citizen_id:\d+}")
async def update_citizen(request: Request) -> Response:
    log.debug("update_citizen")
    return Response(text="update_citizen")


@routes.get(r"/imports/{import_id:\d+}/citizend/birthdays")
async def get_citizens_birthdays(request: Request) -> Response:
    log.debug("get_citizens_birthdays")
    return Response(text="get_citizens_birthdays")


@routes.get(r"/imports/{import_id:\d+}/towns/stat/percentile/age")
async def get_age_percentiles(request: Request) -> Response:
    log.debug("get_age_percentiles")
    return Response(text="get_age_percentiles")

