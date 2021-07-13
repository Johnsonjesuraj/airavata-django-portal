import logging

from django.shortcuts import redirect
from wagtail.core import hooks

logger = logging.getLogger(__name__)


@hooks.register('register_rich_text_features')
def register_custom_style_feature(features):

    features.default_features.insert(5, 'h1')
    features.default_features.insert(9, 'h5')
    features.default_features.insert(10, 'h6')
    features.default_features.append('superscript')
    features.default_features.append('subscript')
    features.default_features.append('code')
    features.default_features.append('blockquote')
    # logger.debug(f"default_features={features.default_features}")


DIRECT_SERVE_FILE_EXTENSIONS = ["pdf"]


@hooks.register('before_serve_document')
def direct_serve_document(document, request):
    try:
        file_extension = document.file.name.split(".")[-1]
        if (file_extension in DIRECT_SERVE_FILE_EXTENSIONS and
                'download' not in request.GET):
            return redirect(document.file.url)
    except Exception as e:
        logger.warning("direct_serve_document error: ", exc_info=e)
        return None
