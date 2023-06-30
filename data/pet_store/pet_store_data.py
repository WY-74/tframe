from dataclasses import dataclass
from data.pet_store import Pet, Category, Tags, Status


@dataclass
class PetStoreData:
    pet_base_url: str = "https://petstore.swagger.io/v2/pet"
    pet_find_url: str = f"{pet_base_url}/findByStatus"
    pet_delete_url: str = "https://petstore.swagger.io/v2/pet/{}"
    pet: Pet = Pet(id=230631)
    pet_update: Pet = Pet(
        id=230631,
        category=Category(id=230631, name="cat").__dict__,
        name="nn",
        tags=[Tags(id=230631, name="nn").__dict__],
        status=Status.sold,
    )
