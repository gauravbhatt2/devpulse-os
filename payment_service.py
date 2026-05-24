# Payment Service — refactored to use async client
# SCRUM-2: PR for code review

import httpx

async def charge_customer(user_id, amount):
    async with httpx.AsyncClient() as client:
        resp = await client.post("/api/charge", json={"user": user_id, "amount": amount})
        return resp.json()
