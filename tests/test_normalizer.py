import pytest

from src.normalizers.date_normalizer import DateNormalizer


@pytest.mark.parametrize('need_to_normalize, normalized', (
        ({'дата': '10 ноября 2019 года'}, {'дата': '10.11.2019'}),
        ({'дата': '20 сентября 2022'}, {'дата': '20.09.2022'}),
        ({'СрокОплаты': 'через 2 дня'}, {'СрокОплаты': '0_0_0_2'}),
        ({'СрокОплаты': 'один год две недели'}, {'СрокОплаты': '1_0_2_0'}),
        ({'СрокОплаты': '5 лет четыре дня'}, {'СрокОплаты': '5_0_0_4'}),
        ({'СрокОплаты': 'полгода'}, {'СрокОплаты': '0_6_0_0'}),
        ({'СрокОплаты': 'полтора года двенадцать дней'}, {'СрокОплаты': '1_6_0_12'})
))
@pytest.mark.asyncio
async def test_normalizer(need_to_normalize, normalized):
    await DateNormalizer.normalize(need_to_normalize)
    assert need_to_normalize == normalized


