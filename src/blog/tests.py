from django.test import TestCase
from .models import Author, Note, Article, Tag

# Create your tests here.
class URLTests(TestCase):
    def setUp(self):
        test_note = Note.objects.create(content='TEST CONTENT')
        test_note.save()

        test_author = Author.objects.create(name='test_name', surname='test_surname', note=test_note)
        test_author.save()

        test_tag = Tag.objects.create(name='test_tag')
        test_tag.save()

        test_article = Article.objects.create(title='test_title', content='test_content', author=test_author)
        test_article.save()

    def test_home_page_responding(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_tags_page_responding(self):
        response = self.client.get('/tags/')
        self.assertEqual(response.status_code, 200)

    def test_author_detail_page_responding(self):
        author = Author.objects.get(name='test_name')
        response = self.client.get(f'/author/{author.slug}')
        self.assertEqual(response.status_code, 200)

    def test_article_detail_page_responding(self):
        article = Article.objects.get(title='test_title')
        response = self.client.get(f'/article/{article.slug}')
        self.assertEqual(response.status_code, 200)

class ModelsTests(TestCase):
    def setUp(self):
        test_note = Note.objects.create(content='TEST CONTENT')
        test_note.save()

        test_author = Author.objects.create(name='test_name', surname='test_surname', note=test_note)
        test_author.save()

        test_tag = Tag.objects.create(name='test_tag')
        test_tag.save()

        test_article = Article.objects.create(title='test_title', content='test_content', author=test_author)
        test_article.save()

    def test_note_content_correct(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'TEST CONTENT')

    def test_author_content_correct(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.name, 'test_name')
        self.assertEqual(author.surname, 'test_surname')

    def test_tag_content_correct(self):
        tag = Tag.objects.get(id=1)
        self.assertEqual(tag.name, 'test_tag')

    def test_article_content_correct(self):
        article = Article.objects.get(id=1)
        author = Author.objects.get(id=1)
        self.assertEqual(article.title, 'test_title')
        self.assertEqual(article.content, 'test_content')
        self.assertEqual(article.author, author)
