import asyncio
from functools import wraps, partial

from facerekon.rekon.face_recog import recognize


def async_wrap(func):
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)
    return run 


def _compare_face(filepath: str, known_images_path: str) -> str:
    matches = recognize(known_images_path, filepath)
    if matches:
        return matches[0]
    return None


compare_face = async_wrap(_compare_face)
