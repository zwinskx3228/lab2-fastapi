
import os

from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient


load_dotenv()


class AzureConfig:
    """Configuration for Azure Blob Storage."""

    def __init__(self):
        self.connection_string = os.getenv(
            "AZURE_STORAGE_CONNECTION_STRING"
        )

        self.container_name = os.getenv(
            "AZURE_CONTAINER_NAME"
        )

        if not self.connection_string:
            raise ValueError(
                "AZURE_STORAGE_CONNECTION_STRING is not configured"
            )

        if not self.container_name:
            raise ValueError(
                "AZURE_CONTAINER_NAME is not configured"
            )

        self._blob_service_client = None
        self._container_client = None

    @property
    def blob_service_client(self):
        if self._blob_service_client is None:
            self._blob_service_client = (
                BlobServiceClient.from_connection_string(
                    self.connection_string
                )
            )

        return self._blob_service_client

    @property
    def container_client(self):
        if self._container_client is None:
            self._container_client = (
                self.blob_service_client.get_container_client(
                    self.container_name
                )
            )

        return self._container_client


azure_config = AzureConfig()