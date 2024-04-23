import asyncio
import aioping


async def test_latency(ip):
    try:
        delay = await aioping.ping(ip)
        print(f"IP {ip}: Latency is {delay * 1000:.2f} ms")
    except TimeoutError:
        print(f"IP {ip}: Timeout")


async def main():
    ip_ranges = [
        "162.159.192.",
        "162.159.193.",
        "162.159.195.",
        "162.159.204.",
        "188.114.96.",
        "188.114.97.",
        "188.114.98.",
        "188.114.99."
    ]
    for ip_range in ip_ranges:
        tasks = ([test_latency(ip_range + str(i)) for i in range(1, 255)])
        await asyncio.gather(*tasks)
        tasks.clear()


if __name__ == "__main__":
    asyncio.run(main())
