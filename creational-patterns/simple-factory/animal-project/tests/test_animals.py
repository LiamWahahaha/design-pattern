import animals

class TestAnimals:
    def test_cat_init(self, capsys):
        cat_instance = animals.grab('cat', name='kitty')

        cat_instance.make_sound()
        out, err = capsys.readouterr()
        assert out == 'meowww! :3\n'

        cat_instance.move()
        out, err = capsys.readouterr()
        assert out == 'the cat walks\n'

        cat_instance.purr()
        out, err = capsys.readouterr()
        assert out == 'purrrr!<3\n'

    def test_dog_init(self, capsys):
        dog_instance = animals.grab('dog')

        dog_instance.make_sound()
        out, err = capsys.readouterr()
        assert out == 'woof, woof! :3\n'

        dog_instance.move()
        out, err = capsys.readouterr()
        assert out == 'the dog walks\n'
