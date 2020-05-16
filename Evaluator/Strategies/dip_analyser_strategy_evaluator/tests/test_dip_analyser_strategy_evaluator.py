#  Drakkar-Software OctoBot
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
import pytest

from tests.functional_tests.strategy_evaluators_tests.abstract_strategy_test import AbstractStrategyTest
from tentacles.Evaluator.Strategies import DipAnalyserStrategyEvaluator
from tentacles.Trading.Mode import DipAnalyserTradingMode


# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


@pytest.fixture()
def strategy_tester():
    strategy_tester_instance = DipAnalyserStrategiesEvaluatorTest()
    strategy_tester_instance.initialize(DipAnalyserStrategyEvaluator, DipAnalyserTradingMode)
    return strategy_tester_instance


class DipAnalyserStrategiesEvaluatorTest(AbstractStrategyTest):
    """
    About using this test framework:
    To be called by pytest, tests have to be called manually since the cythonized version of AbstractStrategyTest
    creates an __init__() which prevents the default pytest tests collect process
    """

    # Careful with results here, unlike other strategy tests, this one uses only the 4h timeframe, therefore results
    # are not comparable with regular 1h timeframes strategy tests

    # Cannot use bittrex data since they are not providing 4h timeframe data

    # test_full_mixed_strategies_evaluator.py with only 4h timeframe results are provided for comparison:
    # format: results: (bot profitability, market average profitability)

    async def test_default_run(self):
        # market: -49.40503432494279
        await self.run_test_default_run(-25.195)

    async def test_slow_downtrend(self):
        # market: -49.40503432494279
        # market: -47.12918660287082
        await self.run_test_slow_downtrend(-25.195, -33.975, None, None, skip_extended=True)

    async def test_sharp_downtrend(self):
        # market: -35.18599161146891
        await self.run_test_sharp_downtrend(-22.231, None, skip_extended=True)

    async def test_flat_markets(self):
        # market: -38.1194997684113
        # market: -54.67676179382644
        await self.run_test_flat_markets(-21.13, -32.759, None, None, skip_extended=True)

    async def test_slow_uptrend(self):
        # market: 6.6732347206625064
        # market: -38.74673629242821
        await self.run_test_slow_uptrend(6.673, -14.477)

    async def test_sharp_uptrend(self):
        # market: -18.00341296928329
        # market: -20.128373930217265
        await self.run_test_sharp_uptrend(2.64, 10.578)

    async def test_up_then_down(self):
        await self.run_test_up_then_down(None, skip_extended=True)


async def test_default_run(strategy_tester):
    await strategy_tester.test_default_run()


async def test_slow_downtrend(strategy_tester):
    await strategy_tester.test_slow_downtrend()


async def test_sharp_downtrend(strategy_tester):
    await strategy_tester.test_sharp_downtrend()


async def test_flat_markets(strategy_tester):
    await strategy_tester.test_flat_markets()


async def test_slow_uptrend(strategy_tester):
    await strategy_tester.test_slow_uptrend()


async def test_sharp_uptrend(strategy_tester):
    await strategy_tester.test_sharp_uptrend()


async def test_up_then_down(strategy_tester):
    await strategy_tester.test_up_then_down()
