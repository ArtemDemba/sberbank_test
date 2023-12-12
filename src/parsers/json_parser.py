from src.parsers.interfaces import Parser


class JsonHandler(Parser):
    @classmethod
    def merge_trees(cls, trees: list) -> dict:
        """
        Метод, принимающий список словарей и объединяющий их в результирующий словарь (дерево)
        """
        result_dict = {}
        for tree in trees:
            for key, value in tree.items():
                if key in result_dict:
                    if isinstance(value, dict) and isinstance(result_dict[key], dict):
                        # Если значение - словарь и такой ключ уже есть в результирующем словаре, то
                        # рекурсивно обновляем словарь
                        result_dict[key] = cls.merge_trees([result_dict[key], value])
                    else:
                        result_dict[key] = [result_dict[key], value]
                else:
                    result_dict[key] = value
        return result_dict

