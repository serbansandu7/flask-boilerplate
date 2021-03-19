from sqlalchemy import or_


class Crud:
    @classmethod
    def add_search(cls, query, search):
        if not search:
            return query
        table = cls.__table__
        search_fields = cls.get_search_fields()
        filters_list = [table.c[column].ilike(f"%{search.lower()}%") for column in search_fields]
        return query.filter(or_(*filters_list))

    @classmethod
    def add_pagination(cls, query, page, limit):
        if not page or not limit:
            return query
        offset = (int(page) - 1) * int(limit)
        return query.offset(offset).limit(limit)

    @classmethod
    def get_search_fields(cls):
        raise NotImplementedError("The search list should be implemented in models")
