from whitenoise.storage import CompressedManifestStaticFilesStorage


# For ease of White noise
class WhiteNoiseStaticFilesStorage(CompressedManifestStaticFilesStorage):
    manifest_strict = False