from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, delete, select
from db.models import Product



async def orm_add_product(session: AsyncSession, data: dict):
    obj = Product(
        name=data["name"],
        description=data["description"],
        price=float(data["price"]),
        image=data["image"]
    )
    session.add(obj)
    await session.commit()

async def orm_get_productsClothes(session: AsyncSession):
    query = select(Product).where(Product.type == 1)
    result = await session.execute(query)
    return result.scalars().all()

async def orm_get_productsBizh(session: AsyncSession):
    query = select(Product).where(Product.type == 2)
    result = await session.execute(query)
    return result.scalars().all()

async def orm_get_productKolye(session: AsyncSession):
    query = select(Product).where(Product.name == "колье")
    result = await session.execute(query)
    return result.scalars().all()

async def orm_get_productChoker(session: AsyncSession):
    query = select(Product).where(Product.name == "чокер")
    result = await session.execute(query)
    return result.scalars().all()

async def orm_get_productRing(session: AsyncSession):
    query = select(Product).where(Product.name == "кольцо")
    result = await session.execute(query)
    return result.scalars().all()

async def orm_get_productPodveska(session: AsyncSession):
    query = select(Product).where(Product.name == "подвеска")
    result = await session.execute(query)
    return result.scalars().all()

async def orm_get_productBraslet(session: AsyncSession):
    query = select(Product).where(Product.name == "браслет")
    result = await session.execute(query)
    return result.scalars().all()

async def orm_get_productSergy(session: AsyncSession):
    query = select(Product).where(Product.name == "серьги")
    result = await session.execute(query)
    return result.scalars().all()

async def orm_get_product(session: AsyncSession, product_id: int):
    query = select(Product).where(Product.id == product_id)
    result = await session.execute(query)
    return result.scalar()

async def orm_get_products(session: AsyncSession):
    query = select(Product)
    result = await session.execute(query)
    return result.scalars().all()

async def orm_update_product(session: AsyncSession, product_id: int, data):
    query = update(Product).where(Product.id == product_id).values(
        name=data["name"],
        description=data["description"],
        price=float(data["price"]),
        image=data["image"],
    )
    await session.execute(query)
    await session.commit()


async def orm_delete_product(session: AsyncSession, product_id: int):
    query = delete(Product).where(Product.id == product_id)
    await session.execute(query)
    await session.commit()