from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
import asyncio


class GreetingBehaviour(CyclicBehaviour):
    async def run(self):
        print("Hello! I am a running SPADE agent.")
        await asyncio.sleep(5)


class Lab1Agent(Agent):
    async def setup(self):
        print("Agent started")
        self.add_behaviour(GreetingBehaviour())


async def main():
    agent = Lab1Agent(
        "stephenagyemang@xmpp.jp",      
        "026861"  
    )

    await agent.start()
    print("Agent is running...")
    await asyncio.sleep(30)
    await agent.stop()


if __name__ == "__main__":
    asyncio.run(main())
