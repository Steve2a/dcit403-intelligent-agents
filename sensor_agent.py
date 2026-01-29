import asyncio
import random
from datetime import datetime

from spade.agent import Agent
from spade.behaviour import CyclicBehaviour


def sense_env():
    disaster_types = ["Flood", "Fire", "Earthquake"]
    severity_levels = ["Low", "Medium", "High"]

    disaster = random.choice(disaster_types)
    severity = random.choice(severity_levels)

    return disaster, severity


class SensorBhv(CyclicBehaviour):
    async def run(self):
        disaster, severity = sense_env()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        message = f"[{timestamp}] Disaster Detected: {disaster} | Severity: {severity}"
        print(message)

        
        with open("logs/events.log", "a") as log_file:
            log_file.write(message + "\n")

        await asyncio.sleep(5)



class SensorAgent(Agent):
    async def setup(self):
        print("SensorAgent started and monitoring environment...")
        self.add_behaviour(SensorBhv())


async def main():
    agent = SensorAgent(
        "stephenagyemang@xmpp.jp",
        "026861",                 # replace if your password is different
        verify_security=False
    )

    await agent.start()

    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await agent.stop()
        print("SensorAgent stopped.")


if __name__ == "__main__":
    asyncio.run(main())
