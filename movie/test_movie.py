from django.test import TestCase
from .models import Movie
from datetime import date
from datetime import timedelta
from django.utils.text import slugify

class MovieModelTest(TestCase):

    def setUp(self):
        # Create a movie instance
        self.movie = Movie.objects.create(
            title="Inception",
            screening_datetime=None,
            release_date=date(2010, 7, 16),
            description="A mind-bending thriller by Christopher Nolan.",
            duration="01:48:00",
            director="Christopher Nolan",
            poster="posters/inception-poster.jpg",
            cost=14.99
        )

    def test_movie_creation(self):
        # Test if movie instance is created correctly
        movie = self.movie
        self.assertEqual(movie.title, "Inception")
        self.assertEqual(movie.director, "Christopher Nolan")
        self.assertEqual(str(movie), "Inception")

    def test_slug_auto_generation(self):
        # Test that the slug field is auto-generated based on the movie's title
        movie = self.movie
        self.assertEqual(movie.slug, "inception")


class MovieTest(TestCase):

    def setUp(self):
        # Setup a movie instance with necessary fields
        self.movie = Movie.objects.create(
            title="Test Movie",
            release_date="2025-02-05",
            director="Test Director",
            description="Test Description"
        )

    def test_movie_creation(self):
        # Test if movie is correctly created
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.director, "Test Director")
        self.assertEqual(self.movie.description, "Test Description")
        self.assertEqual(str(self.movie), "Test Movie")

    def test_slug_auto_generation(self):
        # Test if slug is auto-generated when the movie is saved
        movie = Movie.objects.create(
            title="Test Slug Movie",
            release_date="2025-02-05",
            director="Test Director",
            description="Test Description"
        )
        expected_slug = slugify("Test Slug Movie")
        self.assertEqual(movie.slug, expected_slug)

    def test_default_duration(self):
        # Test if the default value for 'duration' is 90 minutes
        movie = Movie.objects.create(
            title="Test Movie with Duration",
            release_date="2025-02-05",
            director="Test Director",
            description="Test Description"
        )
        expected_duration = timedelta(minutes=90)
        self.assertEqual(movie.duration, expected_duration)