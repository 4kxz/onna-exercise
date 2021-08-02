from httpx import AsyncClient
from main import app
from pytest import fixture
from pytest import mark


@fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@mark.asyncio
async def test_health_returns_200(client):
    response = await client.get('/health')
    assert response.status_code == 200
