# from http import client
# import logging

# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from apps.clients.models import Client
# from apps.next_of_kins.models import NextOfKin

# logger = logging.getLogger(__name__)


# @receiver(post_save, sender=Client)
# def create_client_next_of_kin(sender, instance, created, **kwargs):
#     if created:
#         NextOfKin.objects.create(client=instance)
#         logger.info(f"{instance}'s next of kin has been created.")