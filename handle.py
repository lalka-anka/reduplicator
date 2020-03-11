from aiohttp import web
import os


def wrap(name):
    async def f(arg):
        return web.FileResponse(name)
    return f


def main(name):
    app = web.Application()
    file_opener = wrap(name)
    app.router.add_get('/', file_opener)
    web.run_app(app)


def create_server():
    path = os.path.dirname(os.path.realpath(__file__))
    new_html_page = path + '/page_code.html'
    main(new_html_page)
