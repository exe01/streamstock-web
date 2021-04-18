from django.db.models.signals import post_save
from django.dispatch import receiver
from streamstock_backend.admin_panel.models import Compilation
from django.conf import settings
from streamstock_common.mq import MQPublisherSingleton
from streamstock_common import const as mq_const


@receiver(post_save, sender=Compilation)
def post_save_handler(sender, instance: Compilation, **kwargs):
    if instance.status == 'AC':
        publisher = MQPublisherSingleton.get_instance(
            settings.MQ_HOST,
            settings.MQ_PORT,
            mq_const.MQ_TASK_PUBLISHER
        )

        instance.status = 'QU'
        instance.save()
        publisher.publish(mq_const.COMPILATION_QUEUE, {'id': instance.id})
