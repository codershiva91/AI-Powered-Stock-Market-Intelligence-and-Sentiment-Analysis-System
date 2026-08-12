"""
=========================================================
Qdrant Vector Database Client
=========================================================

Author  : Shivam Sahu
Project : AI Stock Market Intelligence System
=========================================================
"""

from qdrant_client import QdrantClient
from qdrant_client.http.models import (
    Distance,
    VectorParams,
    PointStruct,
    Filter,
)

from .config import (
    QDRANT_HOST,
    QDRANT_PORT,
    COLLECTION_NAME,
    EMBEDDING_DIMENSION,
)

from .logger import get_logger

logger = get_logger(__name__)


class QdrantManager:
    """
    Qdrant Database Manager
    """

    ##################################################################

    def __init__(self):

        self.client = QdrantClient(
            host=QDRANT_HOST,
            port=QDRANT_PORT,
        )

        logger.info("Connected to Qdrant.")

    ##################################################################

    def create_collection(self):
        """
        Create collection if it does not already exist.
        """

        collections = self.client.get_collections().collections

        names = [c.name for c in collections]

        if COLLECTION_NAME in names:

            logger.info(
                f"Collection '{COLLECTION_NAME}' already exists."
            )

            return

        self.client.create_collection(

            collection_name=COLLECTION_NAME,

            vectors_config=VectorParams(
                size=EMBEDDING_DIMENSION,
                distance=Distance.COSINE,
            ),
        )

        logger.info(
            f"Collection '{COLLECTION_NAME}' created successfully."
        )

    ##################################################################

    def insert_embedding(
        self,
        news_id,
        embedding,
        payload,
    ):
        """
        Insert a single vector.
        """

        self.client.upsert(

            collection_name=COLLECTION_NAME,

            wait=True,

            points=[
                PointStruct(
                    id=int(news_id),
                    vector=embedding,
                    payload=payload,
                )
            ],
        )

    ##################################################################

    def insert_batch(self, points):
        """
        Insert multiple vectors.
        """

        self.client.upsert(

            collection_name=COLLECTION_NAME,

            wait=True,

            points=points,

        )

        logger.info(f"{len(points)} vectors inserted.")

    ##################################################################

    def search(
        self,
        query_vector,
        limit=5,
        query_filter=None,
    ):
        """
        Semantic vector search.

        Parameters
        ----------
        query_vector : list[float]
            Query embedding.

        limit : int
            Number of results.

        query_filter : Filter, optional
            Metadata filter.

        Returns
        -------
        list
            List of ScoredPoint objects.
        """

        response = self.client.query_points(

            collection_name=COLLECTION_NAME,

            query=query_vector,

            limit=limit,

            query_filter=query_filter,

            with_payload=True,

            with_vectors=False,

        )

        return response.points

    ##################################################################

    def get_all_points(
        self,
        batch_size=1000,
    ):
        """
        Fetch all vectors from the collection.
        """

        all_points = []

        offset = None

        while True:

            points, offset = self.client.scroll(

                collection_name=COLLECTION_NAME,

                limit=batch_size,

                offset=offset,

                with_payload=True,

                with_vectors=False,

            )

            all_points.extend(points)

            if offset is None:
                break

        logger.info(
            f"Fetched {len(all_points)} vectors from '{COLLECTION_NAME}'."
        )

        return all_points

    ##################################################################

    def delete_point(
        self,
        point_id,
    ):
        """
        Delete one vector.
        """

        self.client.delete(

            collection_name=COLLECTION_NAME,

            points_selector=Filter(must=[]),

            points=[point_id],

        )

        logger.info(
            f"Deleted Point : {point_id}"
        )

    ##################################################################

    def collection_info(self):
        """
        Return collection metadata.
        """

        return self.client.get_collection(
            COLLECTION_NAME
        )

    ##################################################################

    def count_vectors(self):
        """
        Return total vectors.
        """

        info = self.client.get_collection(
            COLLECTION_NAME
        )

        return info.points_count

    ##################################################################

    def test_connection(self):
        """
        Test Qdrant connection.
        """

        self.client.get_collections()

        logger.info(
            "Qdrant Connection Successful"
        )

        return True