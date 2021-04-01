from sqlalchemy import Column, Integer, String
from src.models.base import Base
from src.adapters.company import CompanyAdapter
from src.utils.validators import validate_company_body, validate_company_assignment


class Company(Base, CompanyAdapter):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    street = Column(String(200))
    city = Column(String(100))
    country = Column(String(100))

    @classmethod
    def get_companies(cls, context):
        results = context.query(cls).all()
        return cls.to_json(results)

    @classmethod
    def create_company(cls, context, body):
        validate_company_body(body)

        company = Company()
        company.to_object(body)
        context.add(company)
        context.commit()

    @classmethod
    def delete_company(cls, context, company_id):
        company = cls.get_company_by_id(context, company_id)
        context.delete(company)
        context.commit()

    @classmethod
    def get_company_by_id(cls, context, company_id):
        return context.query(cls).filter_by(id=company_id).first()