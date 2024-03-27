def list_all(mongo_collection):
    """
    List all documents in a collection.

    :param mongo_collection: PyMongo collection object
    :return: List of documents in the collection
    """
    all_documents = []
    cursor = mongo_collection.find({})
    for document in cursor:
        all_documents.append(document)
    return all_documents

