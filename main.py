import logging

from yaml import load, Loader

from notion_database_pull.notion_handler import NotionDatabaseRead

log = logging.getLogger(__name__)


def main(config_dict: dict):
    notion_api_key = config_dict["api_key"]

    notion_databases = {}
    for db in config_dict["databases"]:
        if len(db) != 1:
            log.error(f"Database entry {db} is not formatted correctly")
            continue
        label = list(db.keys())[0]
        notion_databases[label] = db[label]

    reader = NotionDatabaseRead(notion_api_key, notion_databases)

    for db_label in notion_databases:
        reader.query_db(db_label)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    with open("config.yaml", "r") as yml:
        config = load(yml, Loader=Loader)
    main(config)
