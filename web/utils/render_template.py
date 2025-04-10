import jinja2
from info import *
from web.server import Webmslandersbot
from utils import get_size
from web.utils.file_properties import get_file_ids
from web.server.exceptions import InvalidHash
import urllib.parse
import logging
import aiohttp

#Dont Remove My Credit @MSLANDERS 
# For Any Kind Of Error Ask Us In Support Group @MSLANDERS_HELP

async def render_page(id, secure_hash, src=None):
    file = await Webmslandersbot.get_messages(int(BIN_CHANNEL), int(id))
    file_data = await get_file_ids(Webmslandersbot, int(BIN_CHANNEL), int(id))
    if file_data.unique_id[:6] != secure_hash:
        logging.debug(f"link hash: {secure_hash} - {file_data.unique_id[:6]}")
        logging.debug(f"Invalid hash for message with - ID {id}")
        raise InvalidHash

    src = urllib.parse.urljoin(
        URL,
        f"{id}?hash={secure_hash}",
    )

    tag = file_data.mime_type.split("/")[0].strip()
    file_size = get_size(file_data.file_size)
    if tag in ["video", "audio"]:
        template_file = "web/template/webav.html"
    else:
        template_file = "web/template/dl.html"
        async with aiohttp.ClientSession() as s:
            async with s.get(src) as u:
                file_size = get_size(int(u.headers.get("Content-Length")))

    with open(template_file) as f:
        template = jinja2.Template(f.read())

    file_name = file_data.file_name.replace("_", " ")

    return template.render(
        file_name=file_name,
        file_url=src,
        file_size=file_size,
        file_unique_id=file_data.unique_id,
    )
