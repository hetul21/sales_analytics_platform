from sqlalchemy import Integer, String, Float, ForeignKey, create_engine, column
from sqlalchemy.orm import declarative_base, relationship

Base =  declarative_base()

class Customer(Base):
    __tablename__ = "customers"

    id = column(Integer, primary_key = True)
    name = column(String, nullable = False)
    email = column(String)
    city = column(String)

    orders = relationship('Order', backpopulates = 'customers')

class Product(Base):

    __tablename__ = "products"

    id  = column(Integer, primarykey = True)
    name = column(String, nullable = False)
    category = column(String)
    price = column(Float, nullable=False)

class Order(Base):
    __tablename__ = "orders"

    id = column(Integer, primarykey = True)
    customer_id = column(Integer, ForeignKey(Customer.id))
    order_date = column(String)

    customer = relationship("Customer", back_populates="orders")


