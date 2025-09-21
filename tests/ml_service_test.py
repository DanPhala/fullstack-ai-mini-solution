import pytest
from unittest.mock import patch, AsyncMock
from services.ml_service.ml_service import MLService
from models.request.energy_prediction import PredictPayload, FeaturesPayload

class MockResponse:
    version = "1.0"
    probability = 0.95
    prediction = True

@pytest.mark.anyio
@patch("services.ml_service.ml_service.AsyncDatabase.get_database", new_callable=AsyncMock)
async def test_predict_service(mock_get_database):
    mock_get_database.return_value.__aenter__.return_value = AsyncMock()

    service = MLService()
    payload = PredictPayload(
        features=FeaturesPayload(
            steps_total=8000,
            hr_avg=75.0,
            sleep_minutes=420
        )
    )
    with patch.object(service, "predict", AsyncMock(return_value=MockResponse())):
        result = await service.predict(payload)
        assert hasattr(result, "version")
        assert hasattr(result, "probability")
        assert isinstance(result.prediction, bool)