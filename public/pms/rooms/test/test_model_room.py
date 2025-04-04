from django.core.exceptions import ValidationError
from django.test import TestCase

from rooms.models import Room


class RoomModelTest(TestCase):
    def setUp(self):
        # Configuración común para las pruebas
        self.room = Room.objects.create(
            name="Room 101",
            room_type="PRIVATE_ROOM",
            capacity=2,
            description="A nice private room.",
        )

    def test_create_room(self):
        self.assertEqual(self.room.name, "Room 101")
        self.assertEqual(
            self.room.get_room_type_display(), "Habitación privada"
        )  # noqa

    def test_room_name_unique(self):
        with self.assertRaises(ValidationError):
            room = Room(name="Room 101", room_type="PRIVATE_ROOM")
            room.full_clean()

    def test_modify_room(self):
        # Modificar la habitación
        self.room.name = "Room 102"
        self.room.save()
        updated_room = Room.objects.get(id=self.room.id)
        self.assertEqual(updated_room.name, "Room 102")

    def test_delete_room(self):
        # Eliminar la habitación
        room_id = self.room.id
        self.room.delete()
        with self.assertRaises(Room.DoesNotExist):
            Room.objects.get(id=room_id)

    def test_room_str_method(self):
        # Verificar el método __str__
        self.assertEqual(
            str(self.room), "Habitación Room 101 (Habitación privada)"
        )  # noqa
