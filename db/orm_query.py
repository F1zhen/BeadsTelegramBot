from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Product



async def orm_add_product(session: AsyncSession, data: dict):
    obj = Product(
        name=data["name"],
        description=data["description"],
        price=float(data["price"]),
        type=int(data["type"]),
        image=data["image"]
    )
    session.add(obj)
    await session.commit()

async def orm_get_products(session: AsyncSession):
    query = select(Product)
    result = await session.execute(query)
    return result.scalars().all()

async def orm_get_product(session: AsyncSession, product_id: int):
    query = select(Product).where(Product.id == product_id)
    result = await.session.execute(query)
    return result.scalar()

async def orm_update_product(session: AsyncSession, product_id: int