from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import SummarySchema, TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    """Returns created summary id"""
    summary = TextSummary(url=payload.url, summary="test summary")
    await summary.save()
    return summary.id


async def get(id: int) -> dict | None:
    """Returns summary by id or `None` if not found"""
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary

    return None


async def get_all() -> list:
    """Returns all summaries"""
    summaries = await TextSummary.all().values()
    return summaries


async def delete(id: int) -> int:
    """Returns deleted summary id"""
    summary = await TextSummary.filter(id=id).first().delete()
    return summary


async def put(id: int, payload: SummaryPayloadSchema) -> dict | None:
    """Returns updated summary or `None` if not found"""
    summary = await TextSummary.filter(id=id).update(url=payload.url, summary=payload.summary)
    if summary:
        updated_summary = await TextSummary.filter(id=id).first().values()
        return updated_summary
    return None
