from category import Category
from topic import Topic


class Document:
    def __init__(self, d_id: int, category_id: int, topic_id: int,
                 file_name: str):
        self.id = d_id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    @classmethod
    def from_instances(cls, d_id: int, category: Category, topic: Topic,
                       file_name: str):
        cat_id = category.id
        top_id = topic.id

        return cls(d_id, cat_id, top_id, file_name)

    def add_tag(self, tag_content: str):
        if tag_content not in self.tags:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content: str):
        if tag_content in self.tags:
            self.tags.remove(tag_content)

    def edit(self, file_name: str):
        self.file_name = file_name

    def __repr__(self):
        return f"Document {self.id}: {self.file_name}; " \
               f"category {self.category_id}, topic {self.topic_id}, " \
               f"tags: {', '.join(self.tags)}"
