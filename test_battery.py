import pytest
from battery import Battery
from unittest.mock import Mock

@pytest.fixture
def charged_battery():
    return Battery(100)

@pytest.fixture
def partially_charged_battery():
    b = Battery(100)
    b.mCharge = 70
    return b

def describe_Battery():

    def it_initializes_with_capacity():
        b = Battery(100)
        assert b.mCapacity == 100
    
    def it_initializes_with_charge():
        b = Battery(100)
        assert b.mCharge == 100
    
    def it_initializes_with_external_monitor():
        monitor = Mock()
        b = Battery(100, monitor)
        assert b.external_monitor == monitor

    def it_recharges_battery_to_capacity(charged_battery):
        charged_battery.recharge(100)
        assert charged_battery.mCharge == 100

    def it_recharges_battery_partially(partially_charged_battery):
        partially_charged_battery.recharge(20)
        assert partially_charged_battery.mCharge == 90

    def it_does_not_overcharge_battery(charged_battery):
        charged_battery.recharge(10)
        assert charged_battery.mCharge == 100

    def it_drains_battery(partially_charged_battery):
        partially_charged_battery.drain(20)
        assert partially_charged_battery.mCharge == 50

    def it_does_not_drain_below_zero(partially_charged_battery):
        partially_charged_battery.drain(80)
        assert partially_charged_battery.mCharge == 0

    def it_notifies_external_monitor_on_recharge(charged_battery):
        monitor = Mock()
        charged_battery.external_monitor = monitor
        charged_battery.mCharge = 50
        charged_battery.recharge(50)
        monitor.notify_recharge.assert_called_once_with(100)

    def it_allows_stubbing_notify_recharge(charged_battery):
        monitor = Mock()
        monitor.notify_recharge.return_value = None
        charged_battery.external_monitor = monitor
        charged_battery.mCharge = 50
        charged_battery.recharge(30)
        monitor.notify_recharge.assert_called_once_with(80)

    def it_notifies_external_monitor_on_drain(partially_charged_battery):
        monitor = Mock()
        partially_charged_battery.external_monitor = monitor
        partially_charged_battery.drain(10)
        monitor.notify_drain.assert_called_once_with(60)

    def it_allows_stubbing_notify_drain(partially_charged_battery):
        monitor = Mock()
        monitor.notify_drain.return_value = None
        partially_charged_battery.external_monitor = monitor
        partially_charged_battery.drain(10)
        monitor.notify_drain.assert_called_once_with(60)