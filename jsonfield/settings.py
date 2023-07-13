from django.conf import settings

JSONFIELD_INDENT = getattr(settings, 'JSONFIELD_INDENT', None)
JSONFIELD_ENCODER_CLASS = getattr(settings, 'JSONFIELD_ENCODER_CLASS', None)
JSONFIELD_DECODER_KWARGS = getattr(settings, 'JSONFIELD_DECODER_KWARGS', {})
