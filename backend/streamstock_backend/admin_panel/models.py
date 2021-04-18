from django.db import models
from datetime import datetime


class PipelineSettings(models.Model):
    CHAT_CHOICES = [
        ('TW', 'twitch'),
    ]
    HIGHLIGHTS_CHOICES = [
        ('AVG', 'avg'),
    ]
    DOWNLOADER_CHOICES = [
        ('TWV', 'twitch_vod'),
    ]
    SPEECH_DETECTOR_CHOICES = [
        ('VOS', 'vosk'),
    ]
    UPLOADER_CHOICES = [
        ('YOU', 'youtube'),
        ('YSE', 'youtube_selenium')
    ]
    TRANSITIONS_CHOICES = [
        ('CFI', 'crossfadein'),
    ]

    twitch_client_id = models.CharField(max_length=64, null=True)
    twitch_client_secret = models.CharField(max_length=64, null=True)

    # Chat
    chat_type = models.CharField(
        max_length=3,
        choices=CHAT_CHOICES,
        null=True,
    )

    twitch_chat_skip = models.DurationField(null=True)

    # Highlights
    highlights_type = models.CharField(
        max_length=3,
        choices=HIGHLIGHTS_CHOICES,
        null=True,
    )

    avg_highlights_tic = models.DurationField(null=True)
    avg_highlights_percent = models.FloatField(null=True)
    avg_highlights_skip_calc = models.DurationField(null=True)

    # Downloader
    downloader_type = models.CharField(
        max_length=3,
        choices=DOWNLOADER_CHOICES,
        null=True
    )

    twitch_vod_downloader_quality = models.CharField(max_length=16, null=True)

    # Speech detector
    speech_detector_type = models.CharField(
        max_length=3,
        choices=SPEECH_DETECTOR_CHOICES,
        null=True
    )

    speech_detector_max_of_silence = models.DurationField(null=True)
    speech_detector_additional_begin = models.DurationField(null=True)
    speech_detector_additional_end = models.DurationField(null=True)

    vosk_speech_detector_model = models.CharField(max_length=64, null=True)

    # Videoeditor
    videoeditor_transition_type = models.CharField(
        max_length=3,
        choices=TRANSITIONS_CHOICES,
        null=True
    )

    # Uploader
    uploader_type = models.CharField(
        max_length=3,
        choices=UPLOADER_CHOICES,
        null=True
    )

    youtube_uploader_client_secrets = models.TextField(null=True)
    youtube_uploader_credentials = models.TextField(null=True)
    youtube_uploader_title = models.CharField(max_length=75, null=True)
    youtube_uploader_description = models.TextField(null=True)
    youtube_uploader_tags = models.CharField(max_length=500, null=True)
    youtube_uploader_category = models.CharField(max_length=256, null=True)
    youtube_uploader_default_language = models.CharField(max_length=16, null=True)
    youtube_uploader_privacy = models.CharField(max_length=32, null=True)
    youtube_uploader_playlist = models.CharField(max_length=256, null=True)

    youtube_selenium_uploader_cookie = models.TextField(null=True)

    # Pipeline
    pipeline_name_of_compilations = models.CharField(max_length=256, null=True)
    pipeline_compilation_length = models.IntegerField(null=True)
    pipeline_max_of_compilations = models.IntegerField(null=True)
    pipeline_to_check_music_license = models.BooleanField(null=True)
    pipeline_to_cut_speech = models.BooleanField(null=True)


class Project(models.Model):
    name = models.CharField(max_length=256)
    pipeline_settings = models.ForeignKey(PipelineSettings, null=True, on_delete=models.SET_NULL)


class Source(models.Model):
    TYPE_CHOICES = [
        ('TW', 'twitch'),
    ]

    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
    )

    title_pattern = models.CharField(max_length=80)
    auto_compile = models.BooleanField(default=False)
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    credentials = models.TextField(null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Compilation(models.Model):
    STATUS_CHOICES = [
        ('AC', 'active'),
        ('PA', 'pause'),
        ('QU', 'queue'),
        ('PR', 'progress'),
        ('RE', 'ready'),
    ]

    source = models.ForeignKey(Source, null=True, on_delete=models.SET_NULL)
    source_location = models.CharField(max_length=256)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    pipeline_settings = models.ForeignKey(PipelineSettings, null=True, on_delete=models.SET_NULL)
    last_part = models.IntegerField(default=0)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='AC'
    )


class CompilationVideo(models.Model):
    STATUS_CHOICES = [
        ('AC', 'active'),
        ('PA', 'pause'),
        ('QU', 'queue'),
        ('PR', 'progress'),
        ('RE', 'ready'),
    ]

    compilation = models.ForeignKey(Compilation, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=256)
    published = models.DateTimeField(default=datetime.now)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='AC'
    )
