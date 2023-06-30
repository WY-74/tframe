import inspect
from pages.pet_store import BASE
from utils.data_sets import Methods
from data.pet_store import Pet
from data.pet_store.pet_store_data import PetStoreData


class PetStorePages(BASE):
    def __init__(self, driver):
        super().__init__(driver)
        self.data = PetStoreData()

    def _get_url_from_data(self):
        fun = inspect.stack()[1].function
        todo = "base" if fun in ["pet_add", "pet_update"] else fun.split("_")[-1]
        url = getattr(self.data, f"pet_{todo}_url")
        return url

    def pet_add(self, pet: Pet):
        url = self._get_url_from_data()
        r = self.http_methods(Methods.post, url, json_params=pet)

        self.assert_status_code(r)
        self.assert_json_response(r, pet, overall=True)

    def pet_find(self, pet: Pet, has_no: bool = False):
        url = self._get_url_from_data()
        r = self.http_methods(Methods.get, url, params={"status": pet.status})

        self.assert_status_code(r)
        expr = "$..id" if has_no else f"$.[?(@.id=={pet.id})].id"
        self.assert_json_response(r, pet.id, expr, has_no=has_no)

    def pet_update(self, pet: Pet):
        url = self._get_url_from_data()
        r = self.http_methods(Methods.put, url, json_params=pet)

        self.assert_status_code(r)
        self.assert_json_response(r, pet, overall=True)

    def pet_delete(self, pet: Pet):
        url = self._get_url_from_data()
        r = self.http_methods(Methods.delete, url.format(pet.id))

        self.assert_status_code(r)
        self.assert_json_response(r, str(pet.id), "$.message")
