import os
import uuid

from flask import current_app, Request
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename


def upload_files(request: Request) -> list[FileStorage] | None:
    """Сохраняем файл из request на диск"""
    if request.files:
        upload_folder = current_app.config.get('UPLOAD_FOLDER')
        images = []
        for file in request.files.values():
            images.append(file)

            images[-1].filename = secure_filename(images[-1].filename)
            if os.path.isfile(
                    os.path.join(upload_folder, images[-1].filename)
            ):
                file_name, file_extension = os.path.splitext(
                    images[-1].filename
                )
                images[-1].filename = (
                        file_name
                        + '_'
                        + str(uuid.uuid4())[:8]
                        + file_extension
                )
            images[-1].save(os.path.join(upload_folder, images[-1].filename))
        return images
