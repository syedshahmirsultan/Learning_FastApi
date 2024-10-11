from pydantic import BaseModel

class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str

# I have passed the keyword arguments because Pydantic's BaseModel enforces it
thing = Creature(
   name="yeti",
   country="Pakistan",
   area="Himalayas",
   description="Hirsute Himalayan",
   aka="Snowman"
)

print(thing.name)
print(thing.country)
print(thing.area)
print(thing.description)
print(thing.aka)