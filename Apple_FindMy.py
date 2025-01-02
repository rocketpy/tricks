# FindMy - The all-in-one library that provides everything you need to query Apple's FindMy network!

# https://github.com/malmeloo/FindMy.py

# https://pypi.org/project/FindMy/

# Installation:
# pip install FindMy


# Important !!!

# This project is currently in Alpha. While existing functionality will likely not change much, the API design is subject to change without prior warning.
# You are encouraged to report any issues you can find on the issue tracker - https://github.com/malmeloo/FindMy.py/issues/


# Features:
"""
 Cross-platform: no Mac needed
 Fetch and decrypt location reports
 Official accessories (AirTags, iDevices, etc.)
 Custom AirTags (OpenHaystack)
 Apple account sign-in
 SMS 2FA support
 Trusted Device 2FA support
 Scan for nearby FindMy-devices
 Decode their info, such as public keys and status bytes
 Import or create your own accessory keys
 Both async and sync APIs
"""

# Examples
# https://github.com/malmeloo/FindMy.py/tree/main/examples

# device_scanner
"""
import asyncio
import logging

from findmy import KeyPair
from findmy.scanner import (
    NearbyOfflineFindingDevice,
    OfflineFindingScanner,
    SeparatedOfflineFindingDevice,
)

logging.basicConfig(level=logging.INFO)

# Set if you want to check whether a specific key (or accessory!) is in the scan results.
# Make sure to enter its private key!
# Leave empty (= None) to not check.
CHECK_KEY = KeyPair.from_b64("")


def _print_nearby(device: NearbyOfflineFindingDevice) -> None:
    print(f"NEARBY Device - {device.mac_address}")
    print(f"  Status byte:  {device.status:x}")
    print("  Extra data:")
    for k, v in sorted(device.additional_data.items()):
        print(f"    {k:20}: {v}")
    print()


def _print_separated(device: SeparatedOfflineFindingDevice) -> None:
    print(f"SEPARATED Device - {device.mac_address}")
    print(f"  Public key:   {device.adv_key_b64}")
    print(f"  Lookup key:   {device.hashed_adv_key_b64}")
    print(f"  Status byte:  {device.status:x}")
    print(f"  Hint byte:    {device.hint:x}")
    print("  Extra data:")
    for k, v in sorted(device.additional_data.items()):
        print(f"    {k:20}: {v}")
    print()


async def scan() -> None:
    scanner = await OfflineFindingScanner.create()

    print("Scanning for FindMy-devices...")
    print()

    scan_device = None

    async for device in scanner.scan_for(10, extend_timeout=True):
        if isinstance(device, NearbyOfflineFindingDevice):
            _print_nearby(device)
        elif isinstance(device, SeparatedOfflineFindingDevice):
            _print_separated(device)
        else:
            print(f"Unknown device: {device}")
            print()
            continue

        if CHECK_KEY and device.is_from(CHECK_KEY):
            scan_device = device

    if scan_device:
        print("Key or accessory was found in scan results! :D")
    elif CHECK_KEY:
        print("Selected key or accessory was not found in scan results... :c")


if __name__ == "__main__":
    asyncio.run(scan())
"""
