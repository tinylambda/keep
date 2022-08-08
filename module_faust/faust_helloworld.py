import faust

app = faust.App("hello-world", broker="kafka://locahost:30092", value_serializer="raw")

greetings_topic = app.topic("greetings")


@app.agent(greetings_topic)
async def greet(greetings):
    async for greeting in greetings:
        print(greeting)
